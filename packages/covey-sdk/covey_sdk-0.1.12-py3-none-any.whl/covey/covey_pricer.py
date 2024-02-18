import os
import time
import asyncio
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime, timedelta
from alpaca.data.timeframe import TimeFrame
from alpaca.data.requests import CryptoBarsRequest, StockBarsRequest
from alpaca.data import CryptoHistoricalDataClient, StockHistoricalDataClient

# for packaging
from covey import get_data, get_segments

# # for internal testing
# from utils import get_data, get_checks


# Pricer class using the new alpaca-SDK (alpaca-py) package
class Pricer:
    def __init__(self, **kwargs):
        # load environment variables (aplaca private and public keys)
        load_dotenv()

        # initialize the 'df' variable, the data frame with final output depending on what we ask (prices, quotes)
        self.prices = pd.DataFrame(columns=['symbol','timestamp','vwap', 'open', 'high', 'low', 'close', 'volume', 'trade_count'])

        # set the index to be symbol & timestamp - this is the native format for new alpaca
        self.prices.set_index(['symbol','timestamp'], inplace=True)

        # set the start date (if not provided)
        self.start = kwargs.get('start',pd.Timestamp('2022-01-01', tz=None).date().isoformat())

        # set the end date (if not provided) - None defaults to latest possible date
        self.end = kwargs.get('end', pd.Timestamp(datetime.now().strftime('%Y-%m-%d'),
                                                  tz=None).date().isoformat())

        # set the time frame - default to Hour
        self.timeframe = kwargs.get('timeframe',TimeFrame.Hour)

        # the entire symbol list
        self.symbols = kwargs.get('symbols', ['AAPL', 'ETHUSDT'])

        # hard crypto exclusions
        self.crypto_exclusions = kwargs.get('crypto_exclusions', ['1INCHUSDT'])

        # hard us equity exclusions - no exclusions by default
        self.us_equity_exclusions = kwargs.get('us_equity_exclusions', [])

        # us equity Tickers - set upon initialization
        self.us_equity_symbols = self.get_us_equity_symbols()

        # crypto Tickers - set upon initialization
        self.crypto_symbols = self.get_crypto_symbols()

        # gather the trades
        loop = asyncio.get_event_loop()
        asyncio.run_coroutine_threadsafe(self.gather_prices(),loop)
        # self.gather_prices()
        # generate price key
        self.price_key = self.get_price_key()

    # extracting us equity symbols from symbols list
    def get_us_equity_symbols(self):
        # remove tickers ending in USDT - which is how web3 delivers crypto tickers
        return [e for e in self.symbols if not e.endswith('USDT') and e not in self.us_equity_exclusions]

    # extracting crypto symbols from symbols list
    def get_crypto_symbols(self):
        # replace USDT with /USD - in new alpaca SDK
        return [c.replace('USDT', '/USD') for c in self.symbols if c.endswith('USDT')
                and c not in self.crypto_exclusions]

    # pulling equity prices
    async def get_prices_equity(self):
        # make sure we have equity symbols
        if len(self.us_equity_symbols) > 0:
            # initialize the client - need to authenticate for equities

            # not so fast check for ticker changes
            self.us_equity_symbols = self.check_ticker_change(self.us_equity_symbols)

            client = StockHistoricalDataClient(os.environ.get('APCA_API_KEY_ID'),  
                                                os.environ.get('APCA_API_SECRET_KEY'))
            
            # set the request parameters (i.e. start, frequency, symbols)
            request_params = StockBarsRequest(
                            symbol_or_symbols=self.us_equity_symbols,
                            timeframe=self.timeframe,
                            start=datetime.strptime(self.start,'%Y-%m-%d')
                    )

            # capture the bars list
            bars = client.get_stock_bars(request_params)

            # perform dataframe operatios only if we have any bars
            if len(bars.data) > 0:

                # convert the bars list 
                bars_df = bars.df

                bars_df['vwap'] = bars_df.groupby('symbol')['vwap'].shift()

                # append to the initial price df - we only need vwap 
                self.prices = pd.concat([self.prices, bars_df])
        
        return 0


    async def get_single_equity_prices(self, symbol, client, start, end):
        # set the request parameters (i.e. start, frequency, symbols)
        
        request_params = StockBarsRequest(
                        symbol_or_symbols=symbol,
                        timeframe=self.timeframe,
                        start=start,
                        end = end
                )
        try:
            # capture the bars list
            bars = client.get_stock_bars(request_params)

            # append to the initial price df - we only need vwap 
            self.prices = pd.concat([self.prices, bars.df])
        except AttributeError:
            print("Could not find prices for {} between {} and {}".format(symbol,start,end))
        

    async def get_equity_historic_database(self):
        # make sure we have equity symbols
        if len(self.us_equity_symbols) > 0:
            # initialize the client - need to authenticate for equities

            # not so fast check for ticker changes
            self.us_equity_symbols = self.check_ticker_change(self.us_equity_symbols)

            client = StockHistoricalDataClient(os.environ.get('APCA_API_KEY_ID'),  
                                                os.environ.get('APCA_API_SECRET_KEY'))

            # break up the dates into segments 
            segments = get_segments(self.start, self.end)


            # loop through the symbols and create a task group/coroutine
            for symbol in self.us_equity_symbols:
                for segment in segments:
                    await asyncio.gather(self.get_single_equity_prices(symbol, client, 
                                    pd.Timestamp(segment[0], tz=None).date().isoformat(), 
                                    pd.Timestamp(segment[1], tz=None).date().isoformat())
                    )

   
    # pulling crypto prices (no need to authenticate with public/private keys here)
    async def get_prices_crypto(self):
        # make sure we have crypt symbols
        if len(self.crypto_symbols) > 0:
            # initialize the client
            client = CryptoHistoricalDataClient()
            
            # set the request parameters (i.e. start, frequency, symbols)
            request_params = CryptoBarsRequest(
                            symbol_or_symbols=self.crypto_symbols,
                            timeframe=self.timeframe,
                            start=datetime.strptime(self.start,'%Y-%m-%d')
                    )

            # capture the bars list
            bars = client.get_crypto_bars(request_params)

             # perform dataframe operatios only if we have any bars
            if len(bars.data) > 0:

                # convert the bars list 
                bars_df = bars.df

                # append to the initial price df - we only need vwap 
                self.prices = pd.concat([self.prices, bars_df])

        return 0

    # gather prices into one dataframe
    async def gather_prices(self):
        await asyncio.gather(self.get_prices_equity(), self.get_prices_crypto())

    # generate the final clean price key to be used by trade and portfolio files
    def get_price_key(self):
        # make a copy of original df
        price_key = self.prices.copy()

        # reset the index because we'll need to work with the data and ticker columns
        price_key.reset_index(inplace=True)

         # conversion for future date operations
        price_key['timestamp'] = pd.to_datetime(price_key['timestamp'])

        # remove time zone awareness
        price_key['timestamp'] = price_key['timestamp'].dt.tz_localize(None)

        # add in the delayed trade date column for future joining
        price_key['delayed_trade_date'] = price_key['timestamp'].dt.strftime('%Y-%m-%d')

        # conversion for merge
        price_key['delayed_trade_date'] = pd.to_datetime(price_key['delayed_trade_date'])

        # set price key index to symbol + timestamp for easier join with the date symbol cross df later
        price_key.set_index(['timestamp','symbol'], inplace=True)

        # create date range between start and end with one hour frequency
        date_range = pd.date_range(self.start, datetime.strptime(self.end,'%Y-%m-%d') + timedelta(days=1),freq = 'h')

        # filter date range above to be between 13:00 - 21:00 (UTC market hours)
        date_range_market_hours = pd.DataFrame(date_range[(date_range.hour >= 13) & (date_range.hour <= 21)], columns = ['timestamp']) 

        # get the ticker list - counter for no symbols due to no trades providing the DUMMY ticker - price will be 0$
        ticker_list = self.crypto_symbols + self.us_equity_symbols if len(self.crypto_symbols + self.us_equity_symbols) > 0 else ['DUMMY']

        # cross with symbol list - set the index to symbol and timestamp for easier join with price key
        date_symbol_cross = date_range_market_hours.merge(pd.DataFrame(list(set(ticker_list)), 
                                columns =['symbol']), how='cross').set_index(['timestamp','symbol'])

        # merge with date range so that I can say for sure we have prices 13:00 - 21:00
        price_key_full = date_symbol_cross.merge(price_key,how='left', left_index=True, right_index=True)

        # forward fill and backfill and unpriced time stamps (i.e. daylight savings time oscillating between 20:00 vs
        # 21:00 closing and 13:00 vs 14:00 open)
        price_key_full.reset_index(inplace=True)
        price_key_full.sort_values(by='timestamp', ascending=True, inplace=True)
        price_key_full['vwap'] = price_key_full.groupby('symbol')['vwap'].transform(lambda x: x.ffill().bfill())

        # fill in the weekend delayed trade dates
        price_key_full['delayed_trade_date'].fillna(value = pd.to_datetime(price_key_full['timestamp'].dt.floor('D')), inplace=True)

        # remove tickers that absolutely have never been priced - then it's just an alpaca issue
        checks_df = pd.DataFrame(price_key_full.vwap.notnull().groupby(price_key_full['symbol']).sum().reset_index())
        checks_df = checks_df[checks_df.vwap !=0]

        # make sure the remaining things that are priced have no nulls - so all the priced counts should be the same per symbol
        assert(len(checks_df['vwap'].unique()) == 1 or checks_df.isnull().sum().sum() == 0)

        # fill in the rest of prices with 0 so it doesn't affect portfolio math / cash used
        price_key_full['vwap'].fillna(0, inplace=True)

        # put back the USDT instead of the USD so it doesn't cause problems later in posting the trades
        price_key_full['symbol'] = price_key_full.apply(lambda x : x['symbol'].replace('/USD', 'USDT') if x['symbol'].endswith('/USD') 
                                                                and x['symbol'] in self.crypto_symbols else x['symbol'], axis=1)


        # check for ticker changes - grab the old symbol 
        #price_key_full = self.check_ticker_change(price_key_full)

        # map back to initial ticker if there was a ticker change (i.e. map PARA back to VIAC before 2/16/2022)
        ticker_change_df = pd.read_csv(get_data('ticker_changes.csv'))
        ticker_change_df['record_date'] = pd.to_datetime(ticker_change_df['record_date'])
        price_key_full = pd.merge(left = price_key_full, right=ticker_change_df, left_on = 'symbol', right_on='new_symbol', how = 'left')

        price_key_full['symbol'] = price_key_full.apply(lambda x : x['symbol_y'] if not(pd.isna(x['symbol_y']))
                                                                 and x['timestamp'] < x['record_date'] else x['symbol_x'],axis=1)
   
        # desired columns 
        output_columns = ['timestamp','symbol','vwap','delayed_trade_date']
        
        return price_key_full[output_columns]

# check for ticker changes, i.e. CREE -> WOLF on 10/1/2021
    def check_ticker_change(self,equity_symbols):
        ticker_change_df = pd.read_csv(get_data('ticker_changes.csv'))

        # grab the latest ticker change per original ticker, just in case
        ticker_change_df = ticker_change_df.sort_values('record_date').groupby('symbol').tail(1)

        # merge the equity symbols with the ticker change df -  see what remains
        df = pd.merge(left = pd.DataFrame(equity_symbols, columns=['symbol']), right = ticker_change_df, how = 'inner', on  = 'symbol')
       
        # all that remains are the old tickers and the new tickers, drop the old symbols from the equity symbols list
        [equity_symbols.remove(l) for l in df['symbol'].to_list()]

        # append the new symbols to equity symbols 
        equity_symbols.extend(df['new_symbol'].to_list())

        print(equity_symbols)

        return equity_symbols



if __name__ == '__main__':
    # start the timer
    start_time = time.time()

    # initialize 'the pricer' (naming done by VS it may not be his best work, open to changing!)
    # the class has default variables for required start,end,tickers,timeframe 
    # so we don't need to pass anything to test

    symbols = ['VIAC']

    p = Pricer(symbols=symbols , start = '2022-01-01', end = '2022-09-15')

    print(p.price_key)

    # print how long it took
    print(f"took {time.time() - start_time} sec")





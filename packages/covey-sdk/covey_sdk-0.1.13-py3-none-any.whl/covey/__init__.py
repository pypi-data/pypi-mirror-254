import os
import datetime

_ROOT = os.path.abspath(os.path.dirname(__file__))

def get_data(path):
    return os.path.join(_ROOT, 'data', path)

def get_output(path):
    return os.path.join(_ROOT, 'output', path)

def get_checks(path):
    return os.path.join(_ROOT, 'checks', path)

def get_segments(start_date, end_date):
    """
    Divides input date range into associated months periods

    Example:
        Input: start_date = 2018-02-15
               end_date   = 2018-04-23
        Output:
            ["2018-02-15 - 2018-02-28", 
             "2018-03-01 - 2018-03-31", 
             "2018-04-01 - 2018-04-23"]
    """

    start_date = datetime.datetime.strptime(start_date,'%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date,'%Y-%m-%d')


    curr_date = start_date
    curr_month = start_date.strftime("%m")
    segments = []

    loop = (curr_date!=end_date) 
    days_increment = 1

    while loop:
        # Get incremented date with 1 day
        curr_date = start_date + datetime.timedelta(days=days_increment)
        # Get associated month
        prev_month = curr_month
        curr_month = curr_date.strftime("%m")
        # Add to segments if new month
        if prev_month!=curr_month:
            # get start of segment
            if not segments:
                start_segment = start_date
            else:
                start_segment = segments[-1][1] + datetime.timedelta(days=1)
            # get end of segment
            end_segment = curr_date - datetime.timedelta(days=1)
            # define and add segment
            segment = [start_segment, end_segment]
            segments.append(segment)
        # stop if last day reached
        loop = (curr_date!=end_date) 
        # increment added days
        days_increment += 1

    if not segments or segments[-1][1]!=end_date:
        if not segments:
            start_last_segment = start_date
        else:
            start_last_segment = segments[-1][1] + datetime.timedelta(days=1)
        last_segment = [start_last_segment, end_date]
        segments.append(last_segment)

    for i in range(len(segments)):
        segments[i][0] = segments[i][0].strftime("%Y-%m-%d")
        segments[i][1] = segments[i][1].strftime("%Y-%m-%d")

    return segments


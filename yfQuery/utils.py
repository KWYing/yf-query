import pandas as pd
from datetime import datetime

def get_timestamp(date, is_end=False):
    # Changing date to unix seconds
    # if is_end change time to end of the day
    # else time is 4 am
    is_end = " 23:59:59" if is_end else " 04:00:00"
    # Change date to Pandas.Datetime format
    dti = pd.to_datetime(date + is_end)
    # Set the localize of the datetime to US/Eastern
    dti = dti.tz_localize('US/Eastern')
    # Convert the datetime in unix seconds
    # and return as an integer
    return int(datetime.timestamp(dti))
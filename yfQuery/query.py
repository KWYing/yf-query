import pandas as pd
from .utils import get_timestamp

# Base Yahoo Finance Query API URL
query_url = "https://query1.finance.yahoo.com/v7/finance/download/"
query_end = "&includeAdjustedClose=true"

def load_csv(symbol, start, end, interval, event, is_multi=False):
    # Check if interval is correct
    assert interval in ['1d', '1wk',
                        '1mo'], "interval can only be '1d', '1wk', or '1mo'"
    assert event in ['history', 'dividend',
                     'split'], "event can only be 'history', 'dividend', or 'split'"
    # Change start and end date to unix seconds
    p1 = get_timestamp(start)
    p2 = get_timestamp(end, True)
    # Applying querys to yahoo finance api
    url = f"{query_url}{symbol}?period1={p1}&period2={p2}&interval={interval}&events={event}{query_end}"
    # Downlading the data to pandas
    df = pd.read_csv(url)
    # Changing index to datetime
    df.Date = pd.to_datetime(df.Date)
    df = df.set_index('Date')
    # If going to do multi download
    if is_multi:
        # Set pandas DataFrame columns to MultiIndex
        iter = [[symbol], df.columns.to_list()]
        df.columns = pd.MultiIndex.from_product(iter, names=["Symbol", ""])
    return df

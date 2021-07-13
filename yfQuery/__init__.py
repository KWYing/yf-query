import time, logging
import pandas as pd
from .query import load_csv

# Using Yahoo Finance Query to download price data

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logging.debug('Testing')

def datareader(symbols, start, end, interval='1d', event='history'):
  # Check if downloading multi data, or if symbols is a list
  is_multi = True if not isinstance(symbols, str) else False
  if is_multi:
    df = None
    i = 0
    while True:
      try:
        if df is None:
          df = load_csv(symbols[i], start, end, interval, event, is_multi)
        else:
          df2 = load_csv(symbols[i], start, end, interval, event, is_multi)
          # Concat or append DataFrame
          df = pd.concat([df, df2], axis=1)
        logging.info('Price Data for :{:5}: from {} to {} downloaded SUCCESSFULLY'.format(symbols[i], start, end))
        i += 1
        if i >= len(symbols):
            break
      except Exception as e:
        if str(e) == 'HTTP Error 401: Unauthorized':
          # Wait 1 minute when API Timeout then retry
          logging.warning('API Timeout : ' + str(e))
          time.sleep(60)
          continue
        # Continue when symbol not find
        logging.warning(str(e) + ' : ' + str(symbols[i]))
        i += 1
        continue
    # Return multi symbol DataFrame
    return df
  # Return single DataFrame
  return load_csv(symbols, start, end, interval, event)
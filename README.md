# Yahoo Finance Query Module

**Simple python package for downloading price data from Yahoo Finance**

**Requires Pandas

Using the Yahoo Finance Query API to download past price data for stocks in interval of 1 day, 1 week, and 1 month for history price data, dividend or split. Software can download a single stock or a list of stocks, then store all price data into a Pandas DataFrame.

Installation
```bash
pip install git+https://github.com/KWYing/yf-query.git#yfQuery
```

Use:
Getting single ticker daily historical price data
```python
from yfQuery import datareader

datareader('AAPL', '2010-01-01', '2020-12-31, interval='1d', event='history')
```

Getting multiply tickers daily historical price data
```python
tickers = ['AAPL', 'TSLA', 'AMD', 'NVDA']
datareader(tickers, '2010-01-01', '2020-12-31', interval='1d', evernt='history')
```

- interval : '1d', '1wk' or '1mo'
- event: 'history', 'dividend', or 'split'

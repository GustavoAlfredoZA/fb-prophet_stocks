import pandas_datareader.data as web
from datetime import date, datetime
import datetime as dt
from fbprophet import Prophet
from fbprophet.plot import plot
import time
import random
import subprocess

now = datetime.now()

def analisys(ticker, opvYear, opvMonth, opvDay):
    start_hist = dt.datetime(opvYear, opvMonth, opvDay)
    end_hist = dt.datetime(now.year, now.month, now.day)
    print(ticker, 'yahoo', start_hist, end_hist)
    df_hist = web.DataReader(ticker, 'yahoo', start_hist, end_hist)

    df_hist.reset_index(level = 0, inplace = True)

    df_prophet = df_hist[['Date','Close']]
    df_prophet.columns = ['ds','y']

    prophet = Prophet()
    prophet.fit(df_prophet)

    future = prophet.make_future_dataframe(periods = 365)

    forecast = prophet.predict(future)
    forecast[['ds','yhat','yhat_lower','yhat_upper']].tail(20)

    #prophet.plot(forecast, figsize = (30,10))
    prophet.plot(forecast).savefig(ticker+'0.png')

    #prophet.plot_components(forecast, figsize = (30,10))
    prophet.plot_components(forecast).savefig(ticker+'1.png')

stockL=[['FB',   2012,  5, 12],
        ['TRVG', 2016, 12, 16],
        ['SPHD', 2012, 10, 26],
        ['TRIP', 2011, 12,  7],
        ['EWW',  1993,  3, 18],
        ['MSFT', 1986,  3, 13],
        ['COST', 1986,  7,  9],
        ['AMZN', 1997,  5, 15],
        ['WMT',  1972,  8, 25],
        ['DDD',  1988,  3, 10],
        ['KMB',  1980, 10, 17],
        ['TSLA', 2010,  6, 29],
        ['SONY', 1973,  2, 21],
        ['ATVI', 1993, 10, 25],
        ['CSCO', 1990,  2, 16],
        ['ABNB', 2020, 12, 10],
        ['NDAQ', 2002,  7,  1],
        ['INTC', 1980,  3, 17],
        ['IBM',  1962,  1,  2],
        ['ORCL', 1986,  3, 12],
        ['DELL', 2016,  8, 17],
        ['QCOM', 1991, 12, 13],
        ['NVDA', 1999,  1, 22],
        ['AMD',  1980,  3, 17],
        ['HPQ',  1962,  1,  2],
        ['HPE',  2015, 10, 19],
        ['AAPL', 1980, 12, 12]]

for s in stockL:
    s.append(date(s[1],s[2],s[3]))

def runAnalisys():
    for stock in stockL:
        analisys(stock[0], stock[1], stock[2], stock[3])
        time.sleep(random.randint(0,1))
    subprocess.call("mv *.png static/img/", shell=True)
    subprocess.call("ls", shell=True)
    subprocess.call("ls static", shell=True)

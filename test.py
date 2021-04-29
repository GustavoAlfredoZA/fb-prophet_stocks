import pandas_datareader.data as web
from datetime import datetime
import datetime as dt
from fbprophet import Prophet
from fbprophet.plot import plot


# Establecer el tiempo de consulta
now = datetime.now()

# Primer registro de yahoo finance
start_hist = dt.datetime(2002, 5,23)
end_hist = dt.datetime(now.year, now.month, now.day)

df_hist = web.DataReader('NFLX', 'yahoo', start_hist, end_hist)

df_hist.reset_index(level = 0, inplace = True)

df_prophet = df_hist[['Date','Close']]
df_prophet.columns = ['ds','y']

prophet = Prophet()
prophet.fit(df_prophet)

future = prophet.make_future_dataframe(periods = 365)

forecast = prophet.predict(future)
forecast[['ds','yhat','yhat_lower','yhat_upper']].tail(20)

prophet.plot(forecast, figsize = (30,10))
prophet.plot(forecast).savefig('2.png')

prophet.plot_components(forecast, figsize = (30,10))

prophet.plot_components(forecast).savefig('1.png')

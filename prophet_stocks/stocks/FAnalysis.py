import yfinance as yf

def FA(ticker):
    stock = yf.Ticker(ticker)
    #Response =
    return stock.history(period="max")

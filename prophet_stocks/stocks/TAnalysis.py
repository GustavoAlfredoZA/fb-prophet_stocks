import yfinance as yf
import yahoo_fin.stock_info as si
import pandas as pd

def FA(ticker):
    stock = yf.Ticker(ticker)

    return stock.history(period="max")

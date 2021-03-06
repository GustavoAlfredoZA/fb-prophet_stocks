import yfinance as yf
import yahoo_fin.stock_info as si
import pandas as pd

def FA(stocks):
    quoteTable = {}
    for ticker in stocks:
        quoteTable = si.get_quote_table(ticker)
        quoteTable['Ticker'] = ticker
    return quoteTable

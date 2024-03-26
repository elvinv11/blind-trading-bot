
import yfinance as yf
import talib

def Ma7(parametro):
    data = yf.download(parametro, period="1mo", interval="1d")
    sma = talib.MA(data["Close"], timeperiod=7)
    ma_7 = round(sma[-1], 2)
    return ma_7


def Ma21(parametro):
    data = yf.download(parametro, period="1mo", interval="1d")
    sma = talib.MA(data["Close"], timeperiod=21)
    ma_20 = round(sma[-1], 2)
    return ma_20


def Ma30(parametro):
    data = yf.download(parametro, period="1mo", interval="1d")
    sma = talib.MA(data["Close"], timeperiod=30)
    ma_30 = round(sma[-1], 2)
    return ma_30


def Ma50(parametro):
    data = yf.download(parametro, period="2mo", interval="1d")["Close"]
    sma = talib.MA(data, timeperiod=50)
    ma_50 = round(sma[-1], 2)
    return ma_50


def Ma100(parametro):
    data = yf.download(parametro, period="4mo", interval="1d")
    sma = talib.MA(data["Close"], timeperiod=100)
    ma_100 = round(sma[-1], 2)
    return ma_100



def PrecioActual(parametro):
    precios = yf.Ticker(parametro)
    precio = round(precios.history(period="1d")["Close"].iloc[-1], 2)
    return precio



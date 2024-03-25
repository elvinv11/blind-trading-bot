
import yfinance as yf
import talib

def Ema7(parametro):
    data = yf.download(parametro, period="1mo", interval="1d")
    sma = talib.MA(data["Close"], timeperiod=7)
    #print("la SMA7 es:", sma[-1])
    ema_7 = round(sma[-1], 2)
    return ema_7

#print("la Ema de 7 es:", Ema7("BTC-USD"))

def Ema20(parametro):
    data = yf.download(parametro, period="1mo", interval="1d")
    sma = talib.MA(data["Close"], timeperiod=20)
    ema_20 = round(sma[-1], 2)
    return ema_20

#print("la Ema de 20 es:", Ema20("BTC-USD"))

def Ema30(parametro):
    data = yf.download(parametro, period="1mo", interval="1d")
    sma = talib.MA(data["Close"], timeperiod=30)
    ema_30 = round(sma[-1], 2)
    return ema_30

#print("la Ema de 30 es:", Ema30("BTC-USD"))

def Ema50(parametro):
    data = yf.download(parametro, period="1mo", interval="1d")["Close"]
    sma = talib.MA(data, timeperiod=50)
    ema_50 = sma[-1]
    return ema_50

#print("la Ema de 50 es:", Ema50("BTC-USD"))

def Ema100(parametro):
    data = yf.download(parametro, period="1mo", interval="1d")
    sma = talib.MA(data["Close"], timeperiod=100)
    ema_100 = sma[-1]
    return ema_100

#print("la Ema de 100 es:", Ema100("BTC-USD"))


def PrecioActual(parametro):
    precios = yf.Ticker(parametro)
    precio = round(precios.history(period="1d")["Close"].iloc[-1], 2)
    return precio

#pr = "BTC-USD"
#print("el precio actual es:", PrecioActual(pr))


import yfinance as yf
import talib

def Ma7(parametro, intervalo="1d"):
    """  Calcula la media movil de 7 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    intervalo (str) el intervalo de tiempo 1m, 2m, 5m, 15m, 30m, 
    60m, 90m, 1h,
    """
    try:
        data = yf.download(parametro, period="1mo", interval=intervalo)
        close = data["Close"].values
        close = close.flatten()
        sma = talib.MA(close, timeperiod=7)
        ma_7 = round(sma[-1], 2)
        return ma_7
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None

# print("la Ma de 7 es =", Ma7("BTC-USD"))

def Ma21(parametro, intervalo="1d"):
    """  Calcula la media movil de 21 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    try:
        data = yf.download(parametro, period="1mo", interval=intervalo)
        close = data["Close"].values
        close = close.flatten()
        sma = talib.MA(close, timeperiod=21)
        ma_20 = round(sma[-1], 2)
        return ma_20
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None

# print("la Ma 21 es =", Ma21("BTC-USD"))

def Ma30(parametro, intervalo="1d"):
    """  Calcula la media movil de 30 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    try:
        data = yf.download(parametro, period="2mo", interval=intervalo)
        close = data["Close"].values
        close = close.flatten()
        sma = talib.MA(close, timeperiod=30)
        ma_30 = round(sma[-1], 2)
        return ma_30
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None

# print("La de 30 es =", Ma30("BTC-USD"))

def Ma50(parametro, intervalo="1d"):
    """  Calcula la media movil de 50 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    try:
        data = yf.download(parametro, period="3mo", interval=intervalo)
        close = data["Close"].values
        close = close.flatten()
        sma = talib.MA(close, timeperiod=50)
        ma_50 = round(sma[-1], 2)
        return ma_50
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None

# print("la Ma de 50 es =", Ma50("BTC-USD"))

def Ma100(parametro, intervalo="1d"):
    """  Calcula la media movil de 100 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    try:
        data = yf.download(parametro, period="5mo", interval=intervalo)
        close = data["Close"].values
        close = close.flatten()
        sma = talib.MA(close, timeperiod=100)
        ma_100 = round(sma[-1], 2)
        return ma_100
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None

# print("la Ma de 100 es =", Ma100("BTC-USD"))

def Ema200(parametro, intervalo="1d"):
    """  Calcula la media movil de 200 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    try:
        data = yf.download(parametro, period="10mo", interval=intervalo)
        close = data["Close"].values
        close = close.flatten()
        sma = talib.EMA(close, timeperiod=200)
        ema_200 = round(sma[-1], 2)
        return ema_200
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None

# print("la ema de 200 es =", Ema200("BTC-USD"))

def PrecioActual(parametro, intervalo="1d"):
    """ Octiene el precio actual de un activo financiero y lo retorna"""
    try:
        precios = yf.Ticker(parametro)
        precio = round(precios.history(period=intervalo)["Close"].values[-1], 2)
        return precio
    except Exception as e:
        print(f"Error al obtener el precio actual de ticker: {e}")
        return None

# print("el precio actual es =", PrecioActual("GC=F"))

def BandasBollinger(parametro, intervalo="1d"):
    """
    Calcula las Bandas de Bollinger para un activo financiero.
    Esta función descarga los datos de cierre de un activo financiero del último mes
    y calcula las Bandas de Bollinger utilizando la biblioteca TA-Lib.
    Args:
        parametro (str): El ticker del activo financiero (por ejemplo, 'AAPL').
    Returns:
          una lista que contiene las bandas superior, media y inferior.
    """
    data = yf.download(parametro, period="1mo", interval=intervalo)
    close = data["Close"].values
    close = close.flatten()
    bandas_bollinger = talib.BBANDS(close, 20, nbdevup=2, nbdevdn=2)
    return bandas_bollinger

# print("las bandas de bolinger son =", BandasBollinger("BTC-USD"))
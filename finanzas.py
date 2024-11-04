
import yfinance as yf
import talib

def Ma7(parametro):
    """  Calcula la media movil de 7 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    try:
        data = yf.download(parametro, period="1mo", interval="1d")
        sma = talib.MA(data["Close"], timeperiod=7)
        ma_7 = round(sma.iloc[-1], 2)
        return ma_7
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None

def Ma21(parametro):
    """  Calcula la media movil de 21 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    try:
        data = yf.download(parametro, period="1mo", interval="1d")
        sma = talib.MA(data["Close"], timeperiod=21)
        ma_20 = round(sma.iloc[-1], 2)
        return ma_20
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None


def Ma30(parametro):
    """  Calcula la media movil de 30 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    try:
        data = yf.download(parametro, period="2mo", interval="1d")
        sma = talib.MA(data["Close"], timeperiod=30)
        ma_30 = round(sma.iloc[-1], 2)
        return ma_30
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None


def Ma50(parametro):
    """  Calcula la media movil de 50 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    try:
        data = yf.download(parametro, period="3mo", interval="1d")["Close"]
        sma = talib.MA(data, timeperiod=50)
        ma_50 = round(sma.iloc[-1], 2)
        return ma_50
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None


def Ma100(parametro):
    """  Calcula la media movil de 100 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    try:
        data = yf.download(parametro, period="5mo", interval="1d")
        sma = talib.MA(data["Close"], timeperiod=100)
        ma_100 = round(sma.iloc[-1], 2)
        return ma_100
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None


def Ema200(parametro):
    """  Calcula la media movil de 200 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    try:
        data = yf.download(parametro, period="10mo", interval="1d")
        sma = talib.EMA(data["Close"], timeperiod=200)
        ema_200 = round(sma.iloc[-1], 2)
        return ema_200
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None


def PrecioActual(parametro):
    """ Octiene el precio actual de un activo financiero y lo retorna"""
    try:
        precios = yf.Ticker(parametro)
        precio = round(precios.history(period="1d")["Close"].iloc[-1], 2)
        return precio
    except Exception as e:
        print(f"Error al obtener el precio actual de {ticker}: {e}")
        return None


def BandasBollinger(parametro):
    """
    Calcula las Bandas de Bollinger para un activo financiero.
    Esta función descarga los datos de cierre de un activo financiero del último mes
    y calcula las Bandas de Bollinger utilizando la biblioteca TA-Lib.
    Args:
        parametro (str): El ticker del activo financiero (por ejemplo, 'AAPL').
    Returns:
        numpy.ndarray: Un array de NumPy que contiene las bandas superior, media y inferior.
    """
    data = yf.download(parametro, period="1mo", interval="1d")
    bandas_bollinger = talib.BBANDS(data["Close"], 20, nbdevup=2, nbdevdn=2)
    return bandas_bollinger




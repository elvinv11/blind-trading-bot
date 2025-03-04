
import yfinance as yf
import talib

def Ma7(parametro, intervalo="1d"):
    """  Calcula la media movil de 7 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    intervalo (str) el intervalo de tiempo 1m, 2m, 5m, 15m, 30m, 
    60m, 90m, 1h,
    """
    match intervalo:
        case "1wk":
            periodo = "3mo"
        case "1mo":
            periodo = "1y"
        case _:
            periodo = "1mo"
    try:
        data = yf.download(parametro, period=periodo, interval=intervalo)
        close = data["Close"].values
        close = close.flatten()
        sma = talib.MA(close, timeperiod=7)
        ma_7 = round(sma[-1], 2)
        return ma_7
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None

# print("la Ma de 7 es =", Ma7("BTC-USD", "5m"))

def Ma21(parametro, intervalo="1d"):
    """  Calcula la media movil de 21 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    match intervalo:
        case "1wk":
            periodo = "6mo"
        case "1mo":
            periodo = "2y"
        case _:
            periodo = "1mo"
    try:
        data = yf.download(parametro, period=periodo, interval=intervalo)
        close = data["Close"].values
        close = close.flatten()
        sma = talib.MA(close, timeperiod=21)
        ma_20 = round(sma[-1], 2)
        return ma_20
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None

# print("la Ma 21 es =", Ma21("BTC-USD", "5m"))

def Ma30(parametro, intervalo="1d"):
    """  Calcula la media movil de 30 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    match intervalo:
        case "1wk":
            periodo = "8mo"
        case "1mo":
            periodo = "3y"
        case _:
            periodo = "1mo"
    try:
        data = yf.download(parametro, period=periodo, interval=intervalo)
        close = data["Close"].values
        close = close.flatten()
        sma = talib.MA(close, timeperiod=30)
        ma_30 = round(sma[-1], 2)
        return ma_30
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None

# print("La de 30 es =", Ma30("BTC-USD", "5m"))

def Ma50(parametro, intervalo="1d"):
    """  Calcula la media movil de 50 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    match intervalo:
        case "1wk":
            periodo = "1y"
        case "1mo":
            periodo = "5y"
        case _:
            periodo = "1mo"
    try:
        data = yf.download(parametro, period=periodo, interval=intervalo)
        close = data["Close"].values
        close = close.flatten()
        sma = talib.MA(close, timeperiod=50)
        ma_50 = round(sma[-1], 2)
        return ma_50
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None

# print("la Ma de 50 es =", Ma50("BTC-USD", "5m"))

def Ma100(parametro, intervalo="1d"):
    """  Calcula la media movil de 100 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    match intervalo:
        case "1wk":
            periodo = "2y"
        case "1mo":
            periodo = "10y"
        case _:
            periodo = "1mo"
    try:
        data = yf.download(parametro, period=periodo, interval=intervalo)
        close = data["Close"].values
        close = close.flatten()
        sma = talib.MA(close, timeperiod=100)
        ma_100 = round(sma[-1], 2)
        return ma_100
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None

# print("la Ma de 100 es =", Ma100("BTC-USD", "5m"))

def Ema200(parametro, intervalo="1d"):
    """  Calcula la media movil de 200 días del activo 
    Args: 
    parametro (str): tiker (símbolo del activo financiero).
    """
    match intervalo:
        case "1wk":
            periodo = "4y"
        case "1mo":
            periodo = "20y"
        case _:
            periodo = "1mo"
    try:
        data = yf.download(parametro, period=periodo, interval=intervalo)
        close = data["Close"].values
        close = close.flatten()
        sma = talib.EMA(close, timeperiod=200)
        ema_200 = round(sma[-1], 2)
        return ema_200
    except Exception as e:
        print(f"Error al calcular la media móvil: {e}")
        return None

# print("la ema de 200 es =", Ema200("BTC-USD", "5m"))

def PrecioActual(parametro, intervalo="1d"):
    """Obtiene el precio actual de un activo financiero y lo retorna"""
    try:
        precios = yf.Ticker(parametro)
        history = precios.history(period="1d")

        if history.empty:
            # Captura el mensaje de error específico de Yahoo Finance
            return f"{parametro}: possibly delisted; no price data found (period=1d) (Yahoo error = 'No data found, symbol may be delisted')"

        precio = round(history["Close"].values[-1], 2)
        return precio
    except Exception as e:
        return f"Error al obtener el precio: {e}"

# print("el precio actual es =", PrecioActual("BTC-USD", "5m"))

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
    match intervalo:
        case "1wk":
            periodo = "6mo"
        case "1mo":
            periodo = "2y"
        case _:
            periodo = "1mo"
    data = yf.download(parametro, period=periodo, interval=intervalo)
    close = data["Close"].values
    close = close.flatten()
    bandas_bollinger = talib.BBANDS(close, 20, nbdevup=2, nbdevdn=2)
    return bandas_bollinger

# print("las bandas de bolinger son =", BandasBollinger("BTC-USD", "1mo"))
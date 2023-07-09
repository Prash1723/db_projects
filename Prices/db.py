import yfinance as yf
import pandas as pd

def generate_KPIs(name):
    """
    Generate chart for popular KPIs:
    1. RSI
    2. MACD
    3. EMA200
    4. EMA50
    5. Bollinger bands 
    """
    df = yf.download()

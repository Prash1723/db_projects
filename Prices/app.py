import yfinance as yf
import time
import talib
import logging

from rich.panel import Panel
from rich.console import Console
from rich import print as rprint
from rich.live import Live
from rich.table import Table
from rich.layout import Layout
from rich.columns import Columns

# Call the console
rc = Console()

products = {"Gold": "GC=F", "Silver": "SI=F"}

organisations = {"Adani": "ADANIENT.NS", "Tata Steel": "TATASTEEL.NS"}

int_coins = {"bicoin": "BTC-INR", "etherium": "ETH-INR"}

currency = {"Indian Rupees": "INR=X", "Japanese Yen": "JPY=X"}

# Configuration for logging
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

# Assign logger
log = logging.getlogger('rich')

# File output settings
FileOut = logging.FileHandler("app.log")

log.addHandler(FileOut)

def generate_protable():
    """Generates the prices of securities available in the market"""
    try:
        table = Table(title="Securities Price", style='bold yellow')
        table.add_column("Security")
        table.add_column("Current Price")
        
        tab1 = table

        for k,v in products.items():
            product = yf.Ticker(v)
            price = product.info['previousClose']
            table.add_row(f"{k}", f"{price}")

    except Exception as e:
        log.error(f"Error: {e}")

    return table

def generate_orgtable():
    """Generates the current share price of organizations"""
    try:
        table = Table(title="Share Price", style="bold green")
        table.add_column("Share")
        table.add_column("Current Price")

        for k,v in organisations.items():
            product = yf.Ticker(v)
            price = product.info['currentPrice']

            table.add_row(f"{k}", f"{price}")

    except Exception as e:
        log.errot(f"Error: {e}")

    return table

def generate_coin():
    """Generates the current crypto currency to Indian rupees exchange rate"""
    try:
        table = Table(title="Coin Price", style="bold red")
        table.add_column("Coin")
        table.add_column("Exchange rate")

        for k,v in int_coins.items():
            product = yf.Ticker(v)
            price = product.info['previousClose']

            table.add_row(f"{k}", f"{price}")

        except Exception as e:
            log.errot(f"Error: {e}")

    return table

def generate_currency():
    """Generates the current exchange rate of currencies to US Dollars"""
    try:
        table = Table(title="Currency compared to USD", style="bold blue")
        table.add_column("Currency")
        table.add_column("Exchange rate")

        for k,v in currency.items():
            product = yf.Ticker(v)
            price = product.info['previousClose']

            table.add_row(f"{k}", f"{price}")

    except Exception as e:
        log.errot(f"Error: {e}")

    return table

# Add all the tables to a panel
pan = Panel.fit(
    Columns([generate_protable(), generate_orgtable(), generate_coin(), generate_currency()]),
    title="Pricing panel",          # Title of the panel
    width=80,                       # Width of the panel
    border_style="red",             # Adding border panel
    padding=(1,2)                   # Space between tables
)

def update_table():
    """Updates the table with live data"""
    # Clear console
    rc.clear()
    # Print the tables
    with Live(pan, refresh_per_second=60) as live:
        while True:
            live.update(pan)
            time.sleep(1)


update_table()

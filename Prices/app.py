import yfinance as yf
import time

from rich.panel import Panel
from rich.console import Console
from rich import print as rprint
from rich.live import Live
from rich.table import Table
from rich.layout import Layout
from rich.columns import Columns

rc = Console()

products = {"Gold": "GC=F", "Silver": "SI=F"}

organisations = {"Adani": "ADANIENT.NS", "Tata Steel": "TATASTEEL.NS"}

int_coins = {"bicoin": "BTC-INR", "etherium": "ETH-INR"}

currency = {"Indian Rupees": "INR=X", "Japanese Yen": "JPY=X"}

def generate_protable():
    table = Table(title="Securities Price", style='bold yellow')
    table.add_column("Security")
    table.add_column("Current Price")
    
    tab1 = table

    for k,v in products.items():
        product = yf.Ticker(v)
        price = product.info['previousClose']
        table.add_row(f"{k}", f"{price}")

    return table

def generate_orgtable():
    table = Table(title="Share Price", style="bold green")
    table.add_column("Share")
    table.add_column("Current Price")

    for k,v in organisations.items():
        product = yf.Ticker(v)
        price = product.info['currentPrice']

        table.add_row(f"{k}", f"{price}")

    return table

def generate_coin():
    table = Table(title="Coin Price", style="bold red")
    table.add_column("Coin")
    table.add_column("Current Price")

    for k,v in int_coins.items():
        product = yf.Ticker(v)
        price = product.info['previousClose']

        table.add_row(f"{k}", f"{price}")

    return table

def generate_currency():
    table = Table(title="Currency compared to USD", style="bold blue")
    table.add_column("Currency")
    table.add_column("Current Price")

    for k,v in currency.items():
        product = yf.Ticker(v)
        price = product.info['previousClose']

        table.add_row(f"{k}", f"{price}")

    return table

pan = Panel.fit(
    Columns([generate_protable(), generate_orgtable(), generate_coin(), generate_currency()]),
    title="Pricing panel",
    width=80,
    border_style="red",
    padding=(1,2)
        )

def update_table():

    # Clear console
    rc.clear()

    # Print the tables
    with Live(console=rc, refresh_per_second=60) as live:
        while True:
            live.update(pan)
            time.sleep(1)


update_table()

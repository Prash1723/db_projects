import python_weather
import asyncio
from python_weather import Client
import logging

from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from rich.columns import Columns
from rich.panel import Panel
from rich.spinner import Spinner
from rich.logging import RichHandler

rc = Console()
layout = Layout()
status = Spinner(name="dots")

# Format for logging
FORMAT='%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Configuration for logging
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

# Assign logger
log = logging.getLogger("rich")

# File output settings
FileOut = logging.FileHandler('app.log')

log.addHandler(FileOut)

async def get_weather(city):
    """Function to call weather data for world cities"""
    try:
        client = python_weather.Client(python_weather.METRIC)
        weather = await client.get(city)
        rc.print("Loading...", status)
        temperature = weather.current.temperature
        humidity = weather.current.humidity
        wind_speed = weather.current.wind_speed

        await client.close()

        # Dictionary data
        x = {
        "City": city, 
        "Temperature": str(temperature)+"°C", 
        "Humidity": str(humidity)+"%", 
        "Wind Speed": str(wind_speed)+"km/h"
        }
    
        stats = Table(title="Weather stats", style="bold yellow")
        stats.add_column('Metrics')
        stats.add_column('Values')

        for key, value in x.items():
            stats.add_row(f"{key}", f"{value}")

        rc.print(stats)

    except Exception as e:
        log.error(f"Error : {e}")

if __name__ == "__main__":
    city = input("Enter city name :")

    asyncio.run(get_weather(city))

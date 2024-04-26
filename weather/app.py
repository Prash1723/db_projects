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
#pan = Panel()
status = Spinner(name="dots")

FORMAT='%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")

async def get_weather(city):
    try:
        client = python_weather.Client(python_weather.METRIC)
        weather = await client.get(city)
        rc.print("Loading...", status)
        temperature = weather.current.temperature
        humidity = weather.current.humidity
        wind_speed = weather.current.wind_speed

        await client.close()

        x = {"City": city, "Temperature": str(temperature)+"°C", "Humidity": str(humidity)+"%", "Wind Speed": str(wind_speed)+"km/h"}
    
        stats = Table(title="Weather stats", style="bold yellow")
        stats.add_column('Metrics')
        stats.add_column('Values')

        for key, value in x.items():
            stats.add_row(f"{key}", f"{value}")

        rc.print(stats)
    except Exception as e:
        log.error(f"Error : {e}", style='red')

city = input("Enter city name :")

asyncio.run(get_weather(city))

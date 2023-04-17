import python_weather
import asyncio
from python_weather import Client

from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from rich.columns import Columns
from rich.panel import Panel
from rich.spinner import Spinner

rc = Console()
layout = Layout()
#pan = Panel()
status = Spinner(name="dots")

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

        rc.log(stats)
    except:
        rc.print("Error : Please Enter a valid city name", style='red')

city = input("Enter city name :")

asyncio.run(get_weather(city))

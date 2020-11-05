from __future__ import annotations

from datetime import datetime
import json
import os

import requests
import typer

app = typer.Typer()
OWM_BASE_URL: str = "https://api.openweathermap.org/data/2.5/"
OWM_API_KEY: str = os.environ["OWM_API_KEY"]


class CurrentWeather:
    """Class that holds basic info for displaying current weather"""

    def __init__(
        self,
        location: str,
        datetime: datetime,
        main: str,
        description: str,
        temp: float,
        feels_like: float,
        pressure: int,
        humidity: int,
        wind_speed: float,
        wind_direction: int,
    ) -> None:
        self.location = location
        self.datetime = datetime
        self.main = main
        self.description = description
        self.temp = temp
        self.feels_like = feels_like
        self.pressure = pressure
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction

    def __str__(self) -> str:
        return (
            f"Loc: {self.location}, Time: {self.datetime} "
            f"Conditions: {self.main}, Temp: {self.temp}"
        )

    @classmethod
    def fromJson(cls, json: dict) -> CurrentWeather:
        return cls(
            location=json["name"],
            datetime=datetime.now(),
            main=json["weather"][0]["main"],
            description=json["weather"][0]["description"],
            temp=json["main"]["temp"],
            feels_like=json["main"]["feels_like"],
            pressure=json["main"]["pressure"],
            humidity=json["main"]["humidity"],
            wind_speed=json["wind"]["speed"],
            wind_direction=json["wind"]["deg"],
        )

    def display(self):
        pass


def get_current_weather(zip_code: str) -> None:
    response = requests.get(
        f"{OWM_BASE_URL}weather?zip={zip_code},us"
        f"&appid={OWM_API_KEY}&units=imperial"
    )
    # for j in response.json():
    typer.echo(json.dumps(response.json(), indent=2))
    weather = CurrentWeather.fromJson(response.json())
    typer.echo(weather)


@app.command()
def main(
    zip_code: str = typer.Option(
        ...,
        "--zip",
        "-z",
        prompt=True,
        help="Zip code to get the weather for.",
    ),
):
    get_current_weather(zip_code=zip_code)


if __name__ == "__main__":
    app()

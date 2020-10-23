import json
import os

import requests
import typer

app = typer.Typer()
OWM_BASE_URL: str = "https://api.openweathermap.org/data/2.5/"
OWM_API_KEY: str = os.environ["OWM_API_KEY"]


def get_current_weather(zip_code: str) -> None:
    response = requests.get(
        f"{OWM_BASE_URL}weather?zip={zip_code},us&appid={OWM_API_KEY}"
    )
    # for j in response.json():
    typer.echo(json.dumps(response.json(), indent=2))


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

import typer


app = typer.Typer()


def get_current_weather(zip_code: str) -> None:
    pass


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

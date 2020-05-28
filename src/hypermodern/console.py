import textwrap

import click
import requests

from . import __version__

API_URL = "https://{}.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
@click.option(
    "--language",
    default="en",
    help="The language of Wikipedia to query"
)
def main(language):
    """
    The Hypermodern python project
    """
    try:
        with requests.get(API_URL.format(language)) as response:
            response.raise_for_status()
            data = response.json()
    except requests.exceptions.HTTPError as e:
        raise click.ClickException(f"An error has occurred:\n{e}")

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))

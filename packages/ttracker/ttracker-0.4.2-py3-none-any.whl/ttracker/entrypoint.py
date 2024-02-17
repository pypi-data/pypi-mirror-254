import os
import click
from ttracker.cli_factory import command_factory


def main():
    c = command_factory()
    try:
        c()
    except Exception as e:
        if os.getenv("TT_DEBUG", False):
            raise e
        else:
            click.secho(f"Error: {str(e)}", fg="red")

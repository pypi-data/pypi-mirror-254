""" Entrypoint of the CLI """
import click
from ptwordfinder.commands.PTWordFinder import calculate_words
from ptwordfinder.commands.PTWordFinder import calculate_single_word


@click.group()
def cli():
    pass


cli.add_command(calculate_words)
cli.add_command(calculate_single_word)
import click

from Planets import commands as planets_commands

PLANETS_TABLE = '.planets.csv'
@click.group()
@click.pass_context
def cli(context):
    context.obj = {}
    ctx.obj['planets_table'] = PLANETS_TABLE

cli.add_command(planets_commands.all)

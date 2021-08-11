import click

from Planets import commands as planets_commands

@click.group()
@click.pass_context
def enter(context):
        context.obj = {}

enter.add_command(planets_commands.all)

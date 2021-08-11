import click

@click.group()
def planets():
    """Manages the planet life cycle"""
    pass


@click.command()
@click.pass_context
def create (context, planet_name, moons, distance to sun, duration):
    """Creates a new planet"""
    pass


@click.command()
@click.pass_context
def list (context):
    """List all planets"""
    pass


@click.command()
@click.pass_context
def update (context, planet_name):
    """Updates a planet"""
    pass


@click.command()
@click.pass_context
def deleate (context, planet_name):
    """Deleate a plenet"""
    pass


all = planets

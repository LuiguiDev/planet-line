import click

from Planets.services import PlanetService
from Planets.models import Planet

@click.group()
def planets ():
    """Manages the planet life cycle"""
    pass


@click.command()
@click.option('-n', '--name',
                type=str,
                promt=True,
                help='The Planet name')
@click.option('-m', '--moons',
                type=str,
                promt=True,
                help='Planets moons')
@click.option('-d', '--distance',
                type=str,
                promt=True,
                help='The Planet distance')
@click.option('-dd', '--duration',
                type=str,
                promt=True,
                help='The Planets day duration')
@click.pass_context
def create(context, planet_name, moons, distance, duration):
    """Creates a new planet"""
    planet = Planet(planet_name, moons, distance, duration)
    planet_service = PlanetService(ctx.obj['planets_table'])

    planet_service.create_planet(planet)


@click.command()
@click.pass_context
def list(context):
    """List all planets"""
    pass


@click.command()
@click.pass_context
def update(context, planet_name):
    """Updates a planet"""
    pass


@click.command()
@click.pass_context
def deleate(context, planet_name):
    """Deleate a plenet"""
    pass


all = planets

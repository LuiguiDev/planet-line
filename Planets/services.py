import csv

from Planets.models import Planet

class PlanetService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_planet(self):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWritter(f, fieldnames=Planet.schema)
            writer.writerow(planet.to_dict())

import uuid

class Planet:

    def __init__(self, planet_name, moons, distance, duration, uid=None):
        self.planet_name = planet_name
        self.moons = moons
        self.distance = distance
        slef.duration = duration
        self.uid = uid or uuid.uuid4()

    def tu_dict(self):
        return vars(self)

    @staticmethod
    def schema():
        return ['planet_name', 'moons', 'distance', 'duration', 'uid']

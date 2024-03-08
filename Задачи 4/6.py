class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving.")


class WaterTransport(Vehicle):
    def __init__(self, name):
        super().__init__(name)


class AirTransport(Vehicle):
    def __init__(self, name):
        super().__init__(name)


class Aviation(AirTransport):
    def __init__(self, name):
        super().__init__(name)


class Airship(AirTransport):
    def __init__(self, name):
        super().__init__(name)


class Dirigible(Airship):
    def __init__(self, name):
        super().__init__(name)


class HotAirBalloon(Airship):
    def __init__(self, name):
        super().__init__(name)


class LandTransport(Vehicle):
    def __init__(self, name):
        super().__init__(name)


class RailwayTransport(LandTransport):
    def __init__(self, name):
        super().__init__(name)


class RoadTransport(LandTransport):
    def __init__(self, name):
        super().__init__(name)


class Car(RoadTransport):
    def __init__(self, name):
        super().__init__(name)


class Bicycle(RoadTransport):
    def __init__(self, name):
        super().__init__(name)


class AnimalPoweredTransport(LandTransport):
    def __init__(self, name):
        super().__init__(name)


class SpaceTransport(Vehicle):
    def __init__(self, name):
        super().__init__(name)


class Spaceship(SpaceTransport):
    def __init__(self, name):
        super().__init__(name)


class Rocket(SpaceTransport):
    def __init__(self, name):
        super().__init__(name)

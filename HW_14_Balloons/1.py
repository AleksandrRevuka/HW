"""Main module of Solar system app"""
import time
from turtle import *
from abc import ABCMeta, abstractmethod
from typing import NamedTuple


class PlanetData(NamedTuple):
    """Planet DTO"""
    planet_size: tuple[float, float]
    planet_color: str | tuple[float, float, float]
    name: str


class Sprite(Turtle, metaclass=ABCMeta):
    """Base sprite"""
    @abstractmethod
    def __init__(self):
        Turtle.__init__(self, shape='circle')


class Planet(Sprite):
    """Planet class"""
    def __init__(self, obj):
        Sprite.__init__(self)
        self.name = obj.name
        self.speed(0)
        self.shapesize(*obj.planet_size)
        self.x = 0
        self.y = 0
        self.color(obj.planet_color)
        self.up()
        self.angle = 0

    def move(self):
        self.goto(self.x, self.y)
        self.x += 1
        self.y += 1


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def make_window():
    """Make window and settings"""
    screen = Screen()
    screen.bgcolor('black')
    screen.title('Solar system')
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.onkey(screen.bye, 'Escape')
    screen.listen()
    screen.tracer(0)
    return screen


def make_planets_data():
    """Planet data"""
    mercury = PlanetData((0.5, 0.5), 'grey', 'mercury')
    venus = PlanetData((0.8, 0.8), 'yellow', 'mercury')

    stars_data = {
        'mercury': mercury,
        'venus': venus,
    }
    return stars_data


def make_planets():
    """Make planets of solar system"""
    planets_data = make_planets_data()
    mercury = Planet(planets_data['mercury'])
    venus = Planet(planets_data['venus'])
    planets = [mercury, venus]
    return planets


def move_objects(objects):
    """Move planets and asteroids"""
    for obj in objects:
        obj.move()


def mainloop():
    """Mainloop of Solar system app"""
    while True:
        move_objects(stars)
        window.update()
        time.sleep(0.05)


if __name__ == '__main__':
    window = make_window()
    stars = make_planets()
    mainloop()

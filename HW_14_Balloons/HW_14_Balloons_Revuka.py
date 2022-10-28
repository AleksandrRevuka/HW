from turtle import *
from abc import ABCMeta, abstractmethod
from typing import NamedTuple
from random import random
import time


class Sprite(Turtle, metaclass=ABCMeta):
    """Base sprite"""
    @abstractmethod
    def __init__(self):
        Turtle.__init__(self, shape='circle')


class BallData(NamedTuple):
    """Ball DTO"""
    planet_size: tuple[float, float]
    planet_color: str | tuple[float, float, float]


class Ball(Sprite):
    """Ball class"""
    def __init__(self, obj,):
        Sprite.__init__(self)
        self.name = obj.name
        self.speed(0)
        self.shapesize(*obj.planet_size)
        self.x = random()
        self.y = random()
        self.color(self.generate_color())
        self.up()
        self.angle = 0

    # def move(self):
    #     self.x = self.radius * cos(self.angle)
    #     self.y = self.radius * sin(self.angle)
    #     self.goto(self.star.xcor() + self.x, self.star.ycor() + self.y)
    #     self.angle += self.increase_angle

    @staticmethod
    def generate_color():
        return random(), random(), random()


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def make_window():
    """Make window and settings"""
    screen = Screen()
    screen.bgcolor('black')
    screen.title('Ball chaos')
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.onkey(screen.bye, 'Escape')
    screen.listen()
    screen.tracer(0)
    return screen


def make_planets_data():
    """Planet data"""
    mercury = BallData((0.5, 0.5), 'grey')
    venus = BallData((0.8, 0.8), 'yellow')

    stars_data = {
        'mercury': mercury,
        'venus': venus,
    }
    return stars_data


def make_planets():
    """Make planets of solar system"""
    planets_data = make_planets_data()
    mercury = Ball(planets_data['mercury'], sun)
    venus = Ball(planets_data['venus'], sun)
    planets = [mercury, venus]
    return planets


def mainloop():
    """Mainloop of Ball chaos app"""
    while True:
        window.update()
        time.sleep(0.01)


if __name__ == '__main__':
    window = make_window()
    mainloop()

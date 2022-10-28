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
    ball_1 = BallData((1, 1), 'grey')
    ball_2 = BallData((1, 1), 'yellow')

    stars_data = {
        'mercury': ball_1,
        'venus': ball_2,
    }
    return stars_data


def make_planets():
    """Make planets of solar system"""
    planets_data = make_planets_data()
    ball_1 = Ball(planets_data['ball_1'], sun)
    ball_2 = Ball(planets_data['ball_2'], sun)
    balls = [ball_1, ball_2]
    return balls


def mainloop():
    """Mainloop of Ball chaos app"""
    while True:
        window.update()
        time.sleep(0.01)


if __name__ == '__main__':
    window = make_window()
    mainloop()

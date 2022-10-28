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
    ball_size: tuple[float, float]
    ball_color: str | tuple[float, float, float]
    ball_name: str


class Ball(Sprite):
    """Ball class"""
    def __init__(self, obj):
        Sprite.__init__(self)
        self.name = obj.ball_name
        self.speed(0)
        self.shapesize(*obj.ball_size)
        self.x = 0
        self.y = 0
        self.color = obj.ball_color
        self.up()

    def move(self):
        self.goto(self.obj.cor() + self.x, self.y)
        self.x += 1
        self.y += 1


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


def make_balls_data():
    """Planet data"""
    ball_1 = BallData((1, 1), 'grey', 'ball_1')
    ball_2 = BallData((1, 1), 'yellow', 'ball_2')

    balls_data = {
        'ball_1': ball_1,
        'ball_2': ball_2,
    }
    return balls_data


def make_balls():
    """Make balls"""
    balls_data = make_balls_data()
    ball_1 = Ball(balls_data['ball_1'])
    ball_2 = Ball(balls_data['ball_2'])
    balls_box = [ball_1, ball_2]
    return balls_box


def move_objects(objects):
    """Move planets and asteroids"""
    for obj in objects:
        obj.move()


def mainloop():
    """Mainloop of Ball chaos app"""
    while True:
        window.update()
        move_objects(balls)
        time.sleep(0.01)


if __name__ == '__main__':
    window = make_window()
    balls = make_balls()
    print(balls)
    mainloop()


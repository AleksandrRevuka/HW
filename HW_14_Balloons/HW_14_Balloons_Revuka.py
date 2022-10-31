"""Ball chaos"""
from turtle import *
from abc import ABCMeta, abstractmethod
from typing import NamedTuple
import time
from random import randint


class BallData(NamedTuple):
    """Ball DTO"""
    ball_size: tuple[float, float]
    ball_color: str
    ball_name: str


class Sprite(Turtle, metaclass=ABCMeta):
    """Base sprite"""
    @abstractmethod
    def __init__(self):
        Turtle.__init__(self, shape='circle')


class Ball(Sprite):
    """Ball class"""
    def __init__(self, obj):
        Sprite.__init__(self)
        self.name = obj.ball_name
        self.speed(0)
        self.shapesize(*obj.ball_size)
        self.seth(randint(0, 360))
        self.color(obj.ball_color)
        self.up()
        self.max_xcor = SCREEN_WIDTH / 2 - 10
        self.min_xcor = - SCREEN_WIDTH / 2 + 10
        self.max_ycor = SCREEN_HEIGHT / 2 - 10
        self.min_ycor = - SCREEN_HEIGHT / 2 + 10

    def move(self):
        self.fd(2)
        if self.xcor() > self.max_xcor and self.ycor() > 0:
            self.lt(randint(35, 55))
        if self.xcor() > self.max_xcor and self.ycor() < 0:
            self.rt(randint(35, 55))
        if self.xcor() < self.min_xcor and self.ycor() > 0:
            self.rt(randint(35, 55))
        if self.xcor() < self.min_xcor and self.ycor() < 0:
            self.lt(randint(35, 55))

        if self.ycor() > self.max_ycor and self.xcor() > 0:
            self.lt(randint(35, 55))
        if self.ycor() > self.max_ycor and self.xcor() < 0:
            self.rt(randint(35, 55))
        if self.ycor() < self.min_ycor and self.xcor() > 0:
            self.rt(randint(35, 55))
        if self.ycor() < self.min_ycor and self.xcor() < 0:
            self.lt(randint(35, 55))


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
    ball_3 = BallData((1, 1), 'red', 'ball_3')
    ball_4 = BallData((1, 1), 'pink', 'ball_4')
    ball_5 = BallData((1, 1), 'white', 'ball_5')
    ball_6 = BallData((1, 1), 'blue', 'ball_6')
    ball_7 = BallData((1, 1), 'green', 'ball_7')
    ball_8 = BallData((1, 1), 'orange', 'ball_8')
    ball_9 = BallData((1, 1), 'purple', 'ball_9')
    ball_10 = BallData((1, 1), 'red', 'ball_10')

    balls_data = {
        'ball_1': ball_1,
        'ball_2': ball_2,
        'ball_3': ball_3,
        'ball_4': ball_4,
        'ball_5': ball_5,
        'ball_6': ball_6,
        'ball_7': ball_7,
        'ball_8': ball_8,
        'ball_9': ball_9,
        'ball_10': ball_10,
    }
    return balls_data


def make_balls():
    """Make balls"""
    balls_data = make_balls_data()
    ball_1 = Ball(balls_data['ball_1'])
    ball_2 = Ball(balls_data['ball_2'])
    ball_3 = Ball(balls_data['ball_3'])
    ball_4 = Ball(balls_data['ball_4'])
    ball_5 = Ball(balls_data['ball_5'])
    ball_6 = Ball(balls_data['ball_6'])
    ball_7 = Ball(balls_data['ball_7'])
    ball_8 = Ball(balls_data['ball_8'])
    ball_9 = Ball(balls_data['ball_9'])
    ball_10 = Ball(balls_data['ball_10'])
    balls_box = [ball_1, ball_2, ball_3, ball_4, ball_5,
                 ball_6, ball_7, ball_8, ball_9, ball_10]
    return balls_box


def move_objects(objects):
    """Move planets and asteroids"""
    for obj in objects:
        obj.move()


def mainloop():
    """Mainloop of Ball chaos app"""
    while True:
        move_objects(balls)
        window.update()
        time.sleep(0.01)


if __name__ == '__main__':
    window = make_window()
    balls = make_balls()
    mainloop()

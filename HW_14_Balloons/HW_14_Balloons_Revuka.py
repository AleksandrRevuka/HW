"""Ball chaos"""
from turtle import *
from abc import ABCMeta, abstractmethod
from time import sleep
from random import randint, random


class Sprite(Turtle, metaclass=ABCMeta):
    """Base sprite"""
    @abstractmethod
    def __init__(self):
        super().__init__(shape='circle')
        self.hideturtle()
        self.up()


class Window:
    """Make window """
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_WIDTH_HALF = SCREEN_WIDTH // 2
    SCREEN_HEIGHT_HALF = SCREEN_HEIGHT // 2

    def __init__(self, screen_title: str = 'Ball chaos'):
        self.canvas = Screen()
        self.canvas.title(screen_title)
        self.canvas.bgcolor('black')
        self.canvas.setup(self.SCREEN_WIDTH, Window.SCREEN_HEIGHT)
        self.canvas.onkey(self.canvas.bye, 'Escape')
        self.canvas.listen()
        self.canvas.tracer(0)


class Ball(Sprite):
    """Ball class"""
    size = 20

    def __init__(self):
        Sprite.__init__(self)
        self.speed(0)
        self.seth(randint(0, 360))
        self.color(self.get_random_color())
        self.goto(self.get_random_position())
        self.showturtle()

    def move(self):
        self.fd(1)

    @staticmethod
    def get_random_color():
        return random(), random(), random()

    @staticmethod
    def get_random_position():
        return randint(-Window.SCREEN_WIDTH_HALF, Window.SCREEN_WIDTH_HALF),\
               randint(-Window.SCREEN_HEIGHT_HALF, Window.SCREEN_HEIGHT_HALF)


class Game:
    __balls_qty = 0

    def __init__(self, balls_qty: int):
        Game.__balls_qty = balls_qty
        self.window = Window()
        self.balls = self.make_balls(balls_qty)

    def run(self):
        while True:
            for ball in self.balls:
                ball.move()
                Game.check_border(ball)
            self.window.canvas.update()
            if Game.__balls_qty < 40:
                sleep(0.0001 * Game.__balls_qty)
            self.check_collision(self.balls)

    @staticmethod
    def check_collision(balls: list[Ball]):
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                if balls[i].distance(balls[j]) < Ball.size:
                    balls[i].rt(180)
                    balls[j].rt(180)

    @staticmethod
    def check_border(ball):
        x = ball.xcor()
        y = ball.ycor()

        if y < -Window.SCREEN_HEIGHT_HALF or y > Window.SCREEN_HEIGHT_HALF:
            ball.lt(randint(35, 55))

        if x > Window.SCREEN_WIDTH_HALF or x < -Window.SCREEN_WIDTH_HALF:
            ball.rt(randint(35, 55))

    @staticmethod
    def make_balls(balls_qty: int):
        return [Ball() for _ in range(balls_qty)]


if __name__ == '__main__':
    game = Game(balls_qty=20)
    game.run()

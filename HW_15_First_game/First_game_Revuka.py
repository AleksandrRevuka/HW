"""Turtle first game"""
from turtle import *
from random import randint, random


class Sprite(Turtle):
    """Base sprite"""
    def __init__(self):
        super().__init__()
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
        # self.canvas.bgcolor('black')
        self.canvas.setup(self.SCREEN_WIDTH, Window.SCREEN_HEIGHT)
        self.canvas.onkey(self.canvas.bye, 'Escape')
        self.canvas.onkeypress(lambda: UserHero.move_user_hero_up(), "Up")
        self.canvas.onkeypress(lambda: UserHero.move_user_hero_down(), "Down")
        self.canvas.listen()
        self.canvas.tracer(0)


class Obstacles(Sprite):
    max_obstacles = Window.SCREEN_HEIGHT_HALF
    cor_box = [cor.append() for cor in range(25, max_obstacles, 25)]

    def __init__(self):
        Sprite.__init__(self)
        self.shape('square')
        self.shapesize(1, 2, 1)
        self.speed(0)
        self.color(self.get_random_color())
        self.goto(self.get_random_position())
        self.seth(180)
        self.showturtle()

    def move_obstacles(self):
        self.fd(5)

    @staticmethod
    def get_random_color():
        return random(), random(), random()

    @staticmethod
    def get_random_position():
        max_obstacles = Window.SCREEN_HEIGHT_HALF
        cor_box = [cor for cor in range(25, max_obstacles, 25)]
        return Window.SCREEN_WIDTH_HALF, randint(-Window.SCREEN_HEIGHT_HALF, Window.SCREEN_HEIGHT_HALF)


class UserHero(Sprite):
    _STEP = 20

    def __init__(self):
        Sprite.__init__(self)
        self.shape('turtle')
        self.goto(0, -Window.SCREEN_HEIGHT_HALF)
        self.seth(90)
        self.showturtle()

    @staticmethod
    def move_user_hero_up():
        y = Game.user_hero.ycor() + UserHero._STEP
        Game.user_hero.sety(y)

    @staticmethod
    def move_user_hero_down():
        y = Game.user_hero.ycor() - UserHero._STEP
        Game.user_hero.sety(y)


class Game:
    GAME_OVER = 'Game over!'
    NEXT_LEVEL = 'Next level'
    user_hero = UserHero()

    def __init__(self):
        self.window = Window()

    def run_game(self):
        while True:
            Game.check_user(self.user_hero)
            self.window.canvas.update()

    @staticmethod
    def check_user(user):
        y = user.ycor()

        if y < -Window.SCREEN_HEIGHT_HALF:
            user.goto(0, -Window.SCREEN_HEIGHT_HALF)

        if y > Window.SCREEN_HEIGHT_HALF:
            Game.message(user, Game.NEXT_LEVEL, 'green')

    @staticmethod
    def message(user, text, color_text):
        user.hideturtle()
        user.goto(0, 0)
        user.color(color_text)
        user.write(text, font=("Arial", 12, "bold"))


if __name__ == '__main__':
    game = Game()
    game.run_game()
"""Turtle first game"""
from turtle import *
from random import randrange, random
from time import sleep


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
    SCREEN_WIDTH_QUARTER = SCREEN_WIDTH // 4

    def __init__(self, screen_title: str = 'Ball chaos'):
        self.canvas = Screen()
        self.canvas.title(screen_title)
        self.canvas.setup(self.SCREEN_WIDTH, Window.SCREEN_HEIGHT)
        self.canvas.onkey(self.canvas.bye, 'Escape')
        self.canvas.onkeypress(lambda: UserHero.move_user_hero_up(), "Up")
        self.canvas.onkeypress(lambda: UserHero.move_user_hero_down(), "Down")
        self.canvas.listen()
        self.canvas.tracer(0)


class Obstacles(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.shape('square')
        self.turtlesize(1, 2, 1)
        self.speed(0.1)
        self.color(self.get_random_color())
        self.goto(self.get_random_position())
        self.seth(180)
        self.showturtle()

    def move_obstacles(self):
        self.fd(0.5)

    @staticmethod
    def get_random_color():
        return random(), random(), random()

    @staticmethod
    def get_random_position():
        return randrange(Window.SCREEN_WIDTH_QUARTER, Window.SCREEN_WIDTH * complexity, 55),\
               randrange(-Window.SCREEN_HEIGHT_HALF, Window.SCREEN_HEIGHT, 25)


class UserHero(Sprite):
    """Make hero"""
    STEP = 5
    size = 25

    def __init__(self):
        Sprite.__init__(self)
        self.shape('turtle')
        self.goto(0, -Window.SCREEN_HEIGHT_HALF)
        self.seth(90)
        self.showturtle()

    @staticmethod
    def move_user_hero_up():
        y = Game.user_hero.ycor() + UserHero.STEP
        Game.user_hero.sety(y)

    @staticmethod
    def move_user_hero_down():
        y = Game.user_hero.ycor() - UserHero.STEP
        Game.user_hero.sety(y)


class Game:
    """Main controller game"""
    GAME_OVER = 'Game over!'
    NEXT_LEVEL = 'Next level'
    user_hero = UserHero()

    def __init__(self, level_hard):
        self.window = Window()
        self.complexity = level_hard

    def run_game(self):
        obstacles = [Obstacles() for _ in range(0, Window.SCREEN_HEIGHT//self.complexity)]
        counter_obstacles = len(obstacles)
        print(counter_obstacles)
        while True:
            check_next_level = Game.check_user(self.user_hero)
            if check_next_level:
                Game.message(self.user_hero, Game.NEXT_LEVEL, 'green')
                self.window.canvas.clearscreen()
                self.complexity -= 1
                next_game = Game(self.complexity)
                next_game.run_game()

            for obstacle in obstacles:
                obstacle.move_obstacles()
            self.window.canvas.update()
            if counter_obstacles > 500:
                sleep(0.00001 * counter_obstacles)

            check_game_over = self.check_collision(self.user_hero, obstacles)
            if check_game_over:
                self.window.canvas.clearscreen()
                Game.message(self.user_hero, Game.GAME_OVER, 'red')

    @staticmethod
    def check_user(user):
        y = user.ycor()
        if y < -Window.SCREEN_HEIGHT_HALF:
            user.goto(0, -Window.SCREEN_HEIGHT_HALF)

        if y > Window.SCREEN_HEIGHT_HALF:
            return True

    @staticmethod
    def check_collision(user_hero, obstacles: list):
        for i in range(len(obstacles)):
            if obstacles[i].distance(user_hero) < user_hero.size:
                return True

    @staticmethod
    def message(user, text, color_text):
        user.goto(0, 0)
        user.color(color_text)
        user.write(text, font=("Arial", 12, "bold"))


if __name__ == '__main__':
    complexity = 4
    game = Game(complexity)
    game.run_game()

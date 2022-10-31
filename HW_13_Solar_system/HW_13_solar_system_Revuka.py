from turtle import *
from math import *
import time


class Planet(Turtle):
    def __init__(self, planet_size, planet_color, radius, star, increase_angle, angle, name='star'):
        Turtle.__init__(self, shape='circle')
        self.name = name
        self.speed(0)
        self.shapesize(*planet_size)
        self.x = 0
        self.y = 0
        self.color(planet_color)
        self.up()
        self.star = star
        self.radius = radius
        self.increase_angle = increase_angle
        self.angle = 0

    def move(self):
        self.goto(self.x, self.y)
        self.x = self.radius * cos(self.angle)
        self.y = self.radius * sin(self.angle)
        self.goto(self.star.xcor() + self.x, self.star.ycor() + self.y)
        self.angle += self.increase_angle


SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 950


window = Screen()
window.bgcolor('black')
window.title('Solar system')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')
window.tracer(0)

sun = Turtle(shape='circle')
sun.color('yellow')
sun.shapesize(5, 5)


mercury = Planet((0.5, 0.5), 'grey', 90, sun, 0.0318, 0.3)
venus = Planet((0.8, 0.8), 'yellow', 120, sun, 0.0235, 0.5)

earth = Planet((1, 1), 'blue', 150, sun, 0.02, 0)
moon = Planet((0.1, 0.1), 'grey', 15, earth, 0.000685, 0)

mars = Planet((0.7, 0.7), 'red', 180, sun, 0.0162, 0.5)
phobos = Planet((0.05, 0.05), 'grey', 15, mars, 0.02, 0)
deimos = Planet((0.05, 0.05), 'grey', 10, mars, 0.04, 0)

jupiter = Planet((2, 2), 'brown', 230, sun, 0.00877, 0.65)
ganymede = Planet((0.05, 0.05), 'grey', 40, jupiter, 0.14, 0)
europa = Planet((0.05, 0.05), 'grey', 35, jupiter, 0.33, 0)
io = Planet((0.05, 0.05), 'grey', 30, jupiter, 0.6, 0)

saturn = Planet((1.8, 1.8), 'orange', 310, sun, 0.0065, 0.7)

uranus = Planet((1.4, 1.4), 'green', 360, sun, 0.00457, 0.9)
neptune = Planet((1.4, 1.4), 'purple', 400, sun, 0.00364, 1)
star = Planet((0.01, 0.01), 'white', 500, sun, 0.1, 1)

window.listen()

while True:
    window.update()
    time.sleep(0.05)
    mercury.move()
    venus.move()
    earth.move()
    moon.move()
    mars.move()
    phobos.move()
    deimos.move()
    jupiter.move()
    ganymede.move()
    europa.move()
    io.move()
    saturn.move()
    uranus.move()
    neptune.move()

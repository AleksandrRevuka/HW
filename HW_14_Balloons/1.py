"""Main module of Solar system app"""
from random import randint
from turtle import *
from screeninfo import get_monitors
import time

from solar_system.classes.planet import Planet
from solar_system.classes.asteroid import Asteroid
from solar_system.classes.planet_data import PlanetData

MONITOR = get_monitors().pop()
SCREEN_WIDTH = MONITOR.width
SCREEN_HEIGHT = MONITOR.height


def make_window():
    """Make window and settings"""
    screen = Screen()
    screen.bgcolor('black')
    screen.title('Solar system')
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.cv._rootwindow.resizable(False, False)
    screen.onkey(screen.bye, 'Escape')
    screen.listen()
    screen.tracer(0)
    return screen


def make_base_planet():
    """Make base planet"""
    base_planet = Turtle(shape='circle')
    base_planet.color('yellow')
    base_planet.shapesize(5, 5)
    return base_planet


def make_planets_data():
    """Planet data"""
    mercury = PlanetData((0.5, 0.5), 'grey', 90, 0.0318)
    venus = PlanetData((0.8, 0.8), 'yellow', 120, 0.0235)

    earth = PlanetData((1, 1), 'blue', 150, 0.02)
    moon = PlanetData((0.1, 0.1), 'grey', 15, 0.000685)

    mars = PlanetData((0.7, 0.7), 'red', 180, 0.0162)
    phobos = PlanetData((0.05, 0.05), 'grey', 15, 0.02)
    deimos = PlanetData((0.05, 0.05), 'grey', 10, 0.04)

    jupiter = PlanetData((2, 2), 'brown', 230, 0.00877)
    ganymede = PlanetData((0.05, 0.05), 'grey', 40, 0.14)
    europa = PlanetData((0.05, 0.05), 'grey', 35, 0.33)
    io = PlanetData((0.05, 0.05), 'grey', 30, 0.6)

    saturn = PlanetData((1.8, 1.8), 'orange', 310, 0.0065, 'saturn')

    uranus = PlanetData((1.4, 1.4), 'green', 360, 0.00457)
    neptune = PlanetData((1.4, 1.4), 'purple', 400, 0.00364)

    stars_data = {
        'mercury': mercury,
        'venus': venus,
        'earth': earth,
        'moon': moon,
        'mars': mars,
        'phobos': phobos,
        'deimos': deimos,
        'jupiter': jupiter,
        'ganymede': ganymede,
        'europa': europa,
        'io': io,
        'saturn': saturn,
        'uranus': uranus,
        'neptune': neptune,
    }
    return stars_data


def make_planets():
    """Make planets of solar system"""
    planets_data = make_planets_data()
    mercury = Planet(planets_data['mercury'], sun)
    venus = Planet(planets_data['venus'], sun)

    earth = Planet(planets_data['earth'], sun)
    moon = Planet(planets_data['moon'], earth)

    mars = Planet(planets_data['mars'], sun)
    phobos = Planet(planets_data['phobos'], mars)
    deimos = Planet(planets_data['deimos'], mars)

    jupiter = Planet(planets_data['jupiter'], sun)
    ganymede = Planet(planets_data['ganymede'], jupiter)
    europa = Planet(planets_data['europa'], jupiter)
    io = Planet(planets_data['io'], jupiter)

    saturn = Planet(planets_data['saturn'], sun)
    uranus = Planet(planets_data['uranus'], sun)
    neptune = Planet(planets_data['neptune'], sun)
    planets = [mercury, venus, earth, moon, mars, phobos, deimos, jupiter, ganymede,
               europa, io, saturn, uranus, neptune]
    return planets


def make_belt_around_planet():
    """Make belt around planet"""
    belt = Turtle()
    belt.hideturtle()
    belt.up()
    belt.width(5)
    belt.speed(0)
    belt.color('grey')
    return belt


def make_asteroids():
    """Make asteroids belt around solar system"""
    return [Asteroid(sun, randint(500, 800)) for _ in range(1000)]


def move_objects(objects):
    """Move planets and asteroids"""
    for obj in objects:
        if obj.name == 'saturn':
            saturn_circle.goto(obj.xcor(), obj.ycor() - 26)
            saturn_circle.circle(26)
            saturn_circle.down()
        obj.move()


def mainloop():
    """Mainloop of Solar system app"""
    while True:
        saturn_circle.clear()
        move_objects(stars)
        window.update()
        time.sleep(0.01)


if __name__ == '__main__':
    window = make_window()
    sun = make_base_planet()
    stars = make_planets() + make_asteroids()
    saturn_circle = make_belt_around_planet()
    mainloop()

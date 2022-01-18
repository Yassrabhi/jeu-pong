import random
from copy import t

import pygame
from pygame import color, rect
from pygame.math import Vector2
import core



def setup():

    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [800, 800]
    core.memory("centredecercle", Vector2(100, 200))
    core.memory("rayonducercle", 6)
    core.memory("couleurducercle", (255, 0, 0))
    core.memory("direction", Vector2(0, 0))

    core.memory("Fx", 0)
    core.memory("Ux", Vector2(0, 0))

    core.memory("l", 0)
    core.memory("l0", 5)
    core.memory("L", 0)






    print("Setup END-----------")

def run():

    core.cleanScreen()

    if core.getKeyPressList(pygame.K_SPACE):
        core.memory("direction", Vector2(0, 0))

    if core.getKeyPressList(pygame.K_z):
        core.memory("direction", Vector2(core.memory("direction").x, -1))

    if core.getKeyPressList(pygame.K_s):
        core.memory("direction", Vector2(core.memory("direction").x, 1))

    if core.getKeyPressList(pygame.K_q):
        core.memory("direction", Vector2(-1, core.memory("direction").y))

    if core.getKeyPressList(pygame.K_d):
        core.memory("direction", Vector2(1, core.memory("direction").y))

    if core.memory("centredecercle").y < 0 or core.memory("centredecercle").y > core.WINDOW_SIZE[1]:
        core.memory("direction", Vector2(core.memory("direction").x, core.memory("direction").y*-1))
        core.memory("couleurducercle", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    if core.memory("centredecercle").x < 0 or core.memory("centredecercle").x > core.WINDOW_SIZE[0]:
        core.memory("direction", Vector2(core.memory("direction").x*-1, core.memory("direction").y))
        core.memory("couleurducercle", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    core.memory("centredecercle", core.memory("direction")+core.memory("centredecercle"))

    if core.getMouseLeftClick() is not None:
        core.memory("Ux", core.getMouseLeftClick() - core.memory("centredecercle"))
        core.memory("l", core.memory("Ux").length())
        core.memory("Ux", core.memory("Ux").normalize())
        core.memory("L", abs(core.memory("l") - core.memory("l0")))



    core.memory("Fx", 0.00015 * (core.memory("L") * core.memory("Ux")))
    core.memory("direction", core.memory("direction") + core.memory("Fx"))
    pygame.draw.circle(core.screen, core.memory("couleurducercle"), core.memory("centredecercle"), core.memory("rayonducercle"))



core.main(setup, run)
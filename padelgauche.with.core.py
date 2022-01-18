import random

import pygame
from pygame import Vector2


class Padelgauche:
    def __init__(self):
        self.position = Vector2(random.randint(0,800),random.randint(0,800))
        self.shape_surf = (4,6)
        self.couleur = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.masse = 10

    def show(self,screen):
        pygame.draw.rectangle(screen,self.couleur,self.position,self.shape_surf)
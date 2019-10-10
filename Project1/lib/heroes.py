import pygame.image
from grid import *

class Hero:
        def __init__(self):
                self.spritePosition = pygame.image.load("./sprites/Hero/heroForward8.png")
                self.playerPosition = [0, 0]
                self.playerInventory = []
                self.weapon = False
                self.health = 100
                self.mana = 200
                self.direction = False
                self.transform = False

        def transforming(self):
                self.transform = not self.transform

class Orb:
        def __init__(self, X, Y, direction):
                self.image = pygame.transform.scale(pygame.image.load('./sprites/orb.png'), (25, 25))
                self.position = [X, Y]
                self.direction = direction
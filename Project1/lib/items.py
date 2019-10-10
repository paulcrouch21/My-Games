import pygame.image
from grid import mapHeight, mapWidth
import random

rand = random.randint

class Sword():
        def __init__(self):
                self.name = "Sword"
                self.image = pygame.image.load("./sprites/sword.png")
                self.imageArmed = pygame.transform.scale(self.image, (35, 35))
                self.position = [rand(0, mapWidth - 1), rand(0, mapHeight - 1)]
                self.placed = True

class Wand:
        def __init__(self):
                self.name = "Wand"
                self.image = pygame.image.load("./sprites/wand.png")
                self.imageArmed = pygame.transform.scale(self.image, (35, 35))
                self.position = [rand(0, mapWidth - 1), rand(0, mapHeight - 1)]
                self.placed = True

class Gold:
        name = "Bitcoin"
        image = pygame.image.load("./sprites/goldCoin.png")
        position = [rand(0, mapWidth - 1), rand(0, mapHeight - 1)]
        placed = True

class Shield:
        def __init__(self):
                self.name = "Shield"
                self.image = pygame.image.load("./sprites/shield.png")
                self.position = [rand(0, mapWidth - 1), rand(0, mapHeight - 1)]
                self.placed = True

class Bow:
        def __init__(self):
                self.name = "Bow"
                self.image = pygame.transform.scale(pygame.image.load("./sprites/bow.png"), (50, 75))
                self.imageArmed = pygame.transform.scale(self.image, (35, 20))
                self.position = [rand(0, mapWidth - 1), rand(0, mapHeight - 1)]
                self.placed = True


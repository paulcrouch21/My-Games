import pygame.image, sys
from grid import mapHeight, mapWidth
import random

rand = random.randint

class Enemy:
        def __init__(self):
                self.enemy = pygame.image.load('./sprites/enemy.png')
                self.enemyPosition = [rand(0, mapWidth - 1), rand(0, mapHeight - 1)]
                self.health = 250
                self.vulnerable = True

class Beast:
        def __init__(self):
                self.beast = pygame.image.load('./sprites/beast.png')
                self.portal = False
                self.portalAppear = True
                self.appear = False 
                self.position = []
                self.summoned = False
                self.health = 100

class Portal:
        def __init__(self):
                self.portal = pygame.image.load('./textures/portal/portal0.png')
                pygame.transform.scale(self.portal, (999, 999))
                self.position = [rand(0, mapWidth - 1), rand(0, mapHeight - 1)]
                self.frame = 0
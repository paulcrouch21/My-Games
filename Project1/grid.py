import pygame
import random

#tiles
dirt = 0
grass = 1
water = 2
wall = 3
tree0 = 4
tree1 = 5
tree2 = 6

#tree object template
class Tree:
        def __init__(self):
                #loads in sprite for game
                self.sprite = pygame.transform.scale(pygame.image.load('./textures/tree.png'), (125, 125))
                self.xPosition = random.randint(50, 300)
                self.yPosition = random.randint(50, 450)

#temple object template
class Temple:
        def __init__(self):
                #loads in sprite for game
                self.sprite = pygame.transform.scale(pygame.image.load('./sprites/temple.png'), (125, 125))
                self.xPosition = 6
                self.yPosition = 1

#determines how many trees will be in the game
numTrees = 0;
trees = [Tree() for x in range (numTrees)]

#loads in textures
textures = {
        dirt: pygame.image.load("./textures/dirt.png"),
        grass: pygame.image.load("./textures/grass.png"),
        water: pygame.image.load("./textures/water.png"),
        wall: pygame.image.load("./textures/wall.png"),
        tree0: pygame.image.load("./textures/tree.png")
}

#tiles to be displayed
grid = [
        [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, water, water, water, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
        [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, water, water, water, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
        [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, water, water, water, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
        [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, water, water, water, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
        [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, water, water, water, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
        [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, water, water, water, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
        [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, water, water, water, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
        [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, water, water, water, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
        [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, water, water, water, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
        [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, water, water, water, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
        [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, water, water, water, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
        [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, water, water, water, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
        [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, water, water, water, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
        [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, water, water, water, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
        [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, water, water, water, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass]
]

#game dimensions
tileSize = 50
mapWidth = 30
mapHeight = 15
pygame.init()
pygame.display.set_caption("Hero's Adventure")
displaySurface = pygame.display.set_mode((mapWidth * tileSize, mapHeight * tileSize))

#colors
white = (200, 200, 200)
black = (0, 0, 0)
blue = (30, 144, 255)
green = (60, 179, 113)
red = (178, 0, 0)
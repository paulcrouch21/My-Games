import pygame, sys

"""
library for all key events
"""

#images for hero animated walking
imagePath = "./sprites/Hero/hero"
forwardPath = imagePath + "Forward"
backPath = imagePath + "Back"
rightPath = imagePath + "Right"
leftPath =  imagePath + "Left"

forwardImages = [forwardPath + str(Forward) + ".png" for Forward in range(8)]
backImages = [backPath + str(Back) + ".png" for Back in range(8)]
rightImages = [rightPath + str(Right) + ".png" for Right in range(8)]
leftImages = [leftPath + str(Left) + ".png" for Left in range(8)]


class KeyEvents:
    def __init__(self, player):
        self.player = player
        self.counter = 0
        self.movement = 1
        self.orbs = []

    def globalEvents(self):
        if self.player.transform:
            self.movement =  1
        else:
            self.movement = 0.5

    def quit(self):
        pygame.quit()
        sys.exit()

    def keyDown(self):
        self.player.playerPosition[1] += self.movement
        self.player.direction = 'd'

        self.player.spritePosition = pygame.image.load(forwardImages[self.counter])
        self.counter = (self.counter + 1) % len(forwardImages)

    def keyUp(self):
        self.player.playerPosition[1] -= self.movement 
        self.player.direction = 'u'

        self.player.spritePosition = pygame.image.load(backImages[self.counter])
        self.counter = (self.counter + 1) % len(backImages)

    def keyLeft(self):
        self.player.playerPosition[0] -= self.movement 
        self.player.direction = 'l'

        self.player.spritePosition = pygame.image.load(leftImages[self.counter])
        self.counter = (self.counter + 1) % len(leftImages)

    def keyRight(self):
        self.player.playerPosition[0] += self.movement
        self.player.direction = 'r'

        self.player.spritePosition = pygame.image.load(rightImages[self.counter])
        self.counter = (self.counter + 1) % len(rightImages)

    def keySpace(self):
        if self.player.weapon:
            self.player.playerInventory.remove(self.player.weapon)
            self.player.weapon.placed = True

            #drop weapon
            if self.player.direction == "d":
                    self.player.weapon.position[0] = self.player.playerPosition[0]
                    self.player.weapon.position[1] = self.player.playerPosition[1] - 1
            elif self.player.direction == "u":
                    self.player.weapon.position[0] = self.player.playerPosition[0]
                    self.player.weapon.position[1] = self.player.playerPosition[1] + 1
            elif self.player.direction == "r":
                    self.player.weapon.position[0] = self.player.playerPosition[0] - 1
                    self.player.weapon.position[1] = self.player.playerPosition[1]
            elif self.player.direction == "l":
                    self.player.weapon.position[0] = self.player.playerPosition[0] + 1
                    self.player.weapon.position[1] = self.player.playerPosition[1]

        self.player.weapon = False
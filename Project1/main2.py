import pygame #imports pygame
import sys
from pygame.locals import * #imports the local files from pygame (saves on typing)
from lib import enemies, heroes, items
from grid import *
import random
from keyEvents import KeyEvents
import math
pygame.init()

# #instances of game objects
# player = heroes.Hero()
# keyEvents = keyEvents(player)
# wand = items.Wand()
# gold = items.Gold()
# sword = items.Sword()
# shield = items.Shield()
# bow = items.Bow()
# enemy = enemies.Enemy()
# portal = enemies.Portal()
# temple = Temple()

# #groupings of related game objects
# gameItems = [wand, sword, shield]
# gameWeapons = [wand, bow]
# beastList = []
# orbsList = []

#other config
inventoryFont = pygame.font.SysFont("FreeSansBold.ttf", 20)
healthFont = pygame.font.SysFont("FreeSansBold.ttf", 40)
portalPath = "./textures/portal/portal_"
portalImages = [portalPath + str(p) + ".png" for p in range(1, 7)]

"""
timed events
"""
#enemy movement
pygame.time.set_timer(USEREVENT, 400)
#spawn beast
pygame.time.set_timer(USEREVENT + 1, 7500)
#increment beast portal frames
pygame.time.set_timer(USEREVENT + 2, 400)
#move beasts
pygame.time.set_timer(USEREVENT + 3, 1000)
#orb travel on path
pygame.time.set_timer(USEREVENT + 4, 100)

gameOver = False
#game loop
# while not gameOver:

#     enemyVulnerableIf = [beast for beast in beastList if beast.appear == True]

#     if len(enemyVulnerableIf) < 1:
#         enemy.vulnerable = True
#     else:
#         enemy.vulnearble = False

#     for event in pygame.event.get():

#         keys = pygame.key.get_pressed()
#         keyEvents.global_events()
    
#         if event.type == QUIT:
#             keyEvents.quit()
    
#         if keys[K_w] and keys[K_t]:
#             keyEvents.key_w()

#         #move right
#         if (keys[K_RIGHT]) and player.playerPosition[0] < mapWidth - 1:
#            keyEvents.keyRight() 
    
#         #move left
#         if (keys[K_LEFT]) and player.playerPosition[0] > 0:
#            keyEvents.keyLeft() 
    
#         #move up
#         if (keys[K_UP]) and player.playerPosition[1] > 0:
#             keyEvents.keyUp()
    
#         #move down
#         if (keys[K_DOWN]) and player.playerPosition[1] < mapHeight - 1:
#             keyEvents.keyDown()
    
#         #placing down items
#         if (keys[K_SPACE]):
#             keyEvents.keySpace()
    
#         #fire orb from wand
#         if (keys[K_f]):
#             if player.weapon == wand:
#                 orbsList.append(heroes.Orb(math.ceil(player.playerPosition[0]), math.ceil(player.playerPosition[1]), player.direction))

#         """
#         TIMED EVENTS
#         """

#         #enemy with portal movement
#         if (event.type == USEREVENT):
#             if portal.frame < 5:
#                 portal.frame += 1
#             else:
#                 x = random.randint(1, 9)
#                 y = random.randint(1, 9)
#                 portal.position = [x, y]
#                 enemy.enemyPosition = [x, y]
#                 portal.frame = 1
        
#         #beast object generator 
#         elif (event.type == USEREVENT + 1):
#             newBeast = enemies.beast()
#             newBbeast.portal = enemies.PORTAL()
#             beastList.append(newBeast)

#        # beast with portal generator
#         elif (event.type == USEREVENT + 2):
#             for beast in beastList:
#                 if beast.portalAppear and beast.portal.frame < 5:
#                     beast.portal.frame += 1
#                 elif not beast.summoned:
#                     beast.portalAppear = False
#                     beast.appear = True
#                     beast.summoned = True
#                     beast.position = [beast.portal.position[0], beast.portal.position[1]]
        
#         #beasts movement hunts player
#         elif (event.type == USEREVENT + 3):
#             for beast in beastList:
#                 if beast.appear:
#                     if player.playerPosition == beast.position:
#                         player.health -= 10
#                     for coordinate in range(len(beast.position)):
#                         if player.playerPosition[coordinate] > beast.position[coordinate]:
#                             beast.position[coordinate] += 1 
#                         else:
#                             beast.position[coordinate] -= 1
        
#         #orb path movement animation
#         elif (event.type == USEREVENT + 4):
#             for orb in orbsList:
#                 if orb.direction == 'd':
#                     orb.position[1] += 1
#                 elif orb.direction == 'u':
#                     orb.position[1] -= 1
#                 elif orb.direction == 'l':
#                     orb.position[0] -= 1 
#                 elif orb.direction == 'r':
#                     orb.position[0] += 1

#         #pickup item conditions
#         for item in gameItems:
#             if player.playerPosition == item.position and item.placed:
#                 player.playerInventory.append(item)
#                 item.placed = False
#                 if item in gameWeapons:
#                     player.weapon = item

#     """
#     Rendering grid, sprites, and view
#     """

#     #render game grid
#     for row in range(mapHeight):
#         for column in range(mapWidth):
#             display.blit(textures[grid[row][column]], (column * tileSize, row * tileSize))

#     #render hero
#     if player.transform:
#         displaySurface.blit(player.wolf, (player.playerPosition[0] * tileSize, player.playerPosition[1] * tileSize))
#     else:
#         displaySurface.blit(player.spritePosition, (player.playerPosition[0] * tileSize, player.playerPosition[1] * tileSize))

#     #render temple
#     displaySurface.blit(temple.sprite, (temple.xPosition * tileSize, temple.yPosition * tileSize))

#     #rendering armed items with player sprite
#     if player.weapon:
#         displaySurface.blit(player.weapon.imageArmed, (player.playerPosition[0] * tileSize, player.playerPosition[1] * tileSize))

#     #render beasts and portal
#     for beast in beastList:
#         if beast.portalAppear:
#             displaySurface.blit(pygame.image.load(portalImages[beast.portal.frame]), (beast.portal.position[0] * tileSize, beast.portal.position[1] * tileSize))
#         if beast.appear:
#             displaySurface.blit(beast.beast, (beast.POS[0] * tileSize, beast.position[1] * tileSize))

#     #render items
#     for item in gameItems:
#             if item.placed == True:
#                 displaySurface.blit(item.image, (item.position[0] * tileSize, item.position[1] * tileSize))

#     #render orbs
#     for orb in orbsList:
#         if orb.position == enemy.enemyPosition and enemy.vulnerable:
#             print('Enemy Health', enemy.health)
#             enemy.health -= 10
#         for beast in beastList:
#                 if orb.position == beast.position:
#                     beast.appear = False
#                     beastList.remove(beast)
#                     orbsList.remove(orb)
#         if orb.position[0] > mapWidth or orb.position[0] < 0 or orb.position[1] > mapHeight or orb.position[1] < 0: 
#             orbsList.remove(orb)

#         displaySurface.blit(orb.IMAGE, (orb.POS[0] * tileSize, orb.POS[1] * tileSize))

#     #render player inventory
#     inventoryPosition = 250
#     for item in player.playerInventory:
#         displaySurface.blit(item.IMAGE, (inventoryPosition, mapHeight * tileSize + 35))
#         inventoryPosition += 10 
#         inventoryText = inventoryFont.render(item.name, True, white, black)
#         displaySurface.blit(inventoryText, (inventoryPosition, mapHeight * tileSize + 15))
#         inventoryPosition += 100

#     #render player health bar
#     playerHealthBarText = healthFont.render('Hero Health:', True, green, black)
#     displaySurface.blit(playerHealthBarText, (15, mapHeight * tileSize - 500))
#     displaySurface.blit(healthFont.render(str(player.health), True, green, black), (225, mapHeight * tileSize - 500))

#     #render enemy health bar
#     playerManaTextBar = healthFont.render('Enemy Health:', True, red, black)
#     displaySurface.blit(playerManaTextBar, (650, mapHeight * tileSize - 500))
#     displaySurface.blit(healthFont.render(str(enemy.health), True, red, black), (900, mapHeight * tileSize - 500))

#     #render trees
#     for tree in sorted(trees, key = lambda t: t.yPosition):
#         displaySurface.blit(tree.sprite, (tree.xPosition, tree.yPosition))

#     #render enemy and portal
#     displaySurface.blit(pygame.image.load(portalImages[portal.frame]), (enemy.enemyPosition[0] * tileSize, enemy.enemyPosition[1] * tileSize))
#     displaSurface.blit(enemy.enemy, (enemy.enemyPosition[0] * tileSize, enemy.enemyPosition[1] * tileSize))

    
#     pygame.display.update()

#     if enemy.health <= 0:
#         gameOver = True
#         print("You Win!")
    
#     if player.health <= 0:
#         gameOver = True
#         print("Game Over. You Lose!")

#end of game loop
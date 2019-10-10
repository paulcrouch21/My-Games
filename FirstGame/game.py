import pygame
import sys
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BACKGROUD_COLOR = (0, 0, 0)

PLAYER_SIZE = 50
playerPos = [WIDTH / 2, HEIGHT - 2 * PLAYER_SIZE]

enemySize = 50
enemyPos = [random.randint(0, WIDTH - enemySize), 0]
enemyList = [enemyPos]

speed = 5

#makes the screen to play the game
screen = pygame.display.set_mode((WIDTH, HEIGHT))

gameOver = False

score = 0

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)

#sets the speed
def setLevel(score, speed):
    return (speed + 100) / 3

#makes the enemies drop down
def dropEnemies(enemyList):
    delay = random.random()
    if len(enemyList) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - enemySize)
        y_pos = 0
        enemyList.append([x_pos, y_pos])

#creates the enemies
def drawEnemies(enemyList):
    for enemyPos in enemyList:
        pygame.draw.rect(screen, BLUE, (enemyPos[0], enemyPos[1], enemySize, enemySize))

def updateEnemyPositions(enemyList, score):
    for idx, enemyPos in enumerate(enemyList):
        if enemyPos[1] >= 0 and enemyPos[1] < HEIGHT:
            enemyPos[1] += speed 
        else:
            enemyList.pop(idx)
            score += 1
    return score

#checks to see if there is a game over
def collisionCheck(enemyList, playerPos):
    for enemyPos in enemyList:
        if detectCollision(enemyPos, playerPos):
            return True
    return False

#function to determine when the blocks touch to end the game
def detectCollision (playerPos, enemyPos):
    p_x = playerPos[0]
    p_y = playerPos[1]

    e_x = enemyPos[0]
    e_y = enemyPos[1]

    if (e_x >= p_x and e_x < (p_x + PLAYER_SIZE)) or (p_x >= e_x and p_x < (e_x + enemySize)):
        if (e_y >= p_y and e_y < (p_y + PLAYER_SIZE)) or (p_y >= e_y and p_y < (e_y + enemySize)):
            return True
    return False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = playerPos[0]
            y = playerPos[1]
            if event.key == pygame.K_LEFT:
                x -= PLAYER_SIZE
            elif event.key == pygame.K_RIGHT:
                x += PLAYER_SIZE

            playerPos = [x, y]

    screen.fill(BACKGROUD_COLOR)

    dropEnemies(enemyList)
    score = updateEnemyPositions(enemyList, score)
    speed = setLevel(score, speed)
    
    text = "Score:" + str(score)
    label = myFont.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH - 200, HEIGHT - 40))

    if collisionCheck(enemyList, playerPos):
        gameOver = True

    drawEnemies(enemyList)

    pygame.draw.rect(screen, RED, (playerPos[0], playerPos[1], PLAYER_SIZE, PLAYER_SIZE))

    clock.tick(144)

    pygame.display.update()

print("Game Over!\nYour score: " + str(score))
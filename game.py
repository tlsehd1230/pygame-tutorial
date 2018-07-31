import pygame
from color import *
import random

TOTAL_SCORE = 0
BOARD_SIZE = 4

pygame.init()

surface = pygame.display.set_mode((400, 500))

pygame.display.set_caption("2048")

font = pygame.font.SysFont("monospace", 20)
score_font = pygame.font.SysFont("monospace", 50)

tile_matrix = [[0, 0, 0, 0],
               [0, 0, 0 ,0],
               [0, 0, 0, 0],
               [0, 0, 0 ,0]]

undo_matrix = []

def main() :
    gameExit = False
    placeRandomTile()
    placeRandomTile()
    printMatrix()

    while not gameExit :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                gameExit = True

            if checkIfcando():
                if event.type == pygame.KEYDOWN and isArrow(event.key):
                    addToUndo()
                    rotation_num = getRotationNum(event.key)

            # rotation_num만큼 반시계방향으로 회전시킴
                for number in range(0, rotation_num):
                    rotateCCW()

                if canMove():
                    moveTiles()
                    mergeTiles()
                    placeRandomTile()

                for count in range(0, (4 - rotation_num) % 4):
                    rotateCCW()

                printMatrix()

            else:
                printGameOver()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                unDo()

        pygame.display.update()

def rotateCCW() :
    temp = tile_matrix[:]
    for n in range(0,4) :
        tile_matrix[n] = temp[3-n]
    temp = tile_matrix[:]

    for x in range(0,4) :
        for y in range(0,4) :
            tile_matrix[x][y] = temp[3-y][3-x]

def isArrow(K) :
    if K in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN) :
        return True

    else :
        return False

def getRotationNum(K) :
    if K == pygame.K_UP :
        return 0
    elif K == pygame.K_DOWN :
        return 2
    elif K == pygame.K_LEFT :
        return 3
    elif K == pygame.K_RIGHT :
        return 1

def checkIfcando() :
    if 0 in tile_matrix :
        return True
    for x in range(0, 4) :
        for y in range(0, 3) :
            if tile_matrix[x][y] == tile_matrix[x][y+1] :
                return True
    for x in range(0, 3) :
        for y in range(0, 4) :
            if tile_matrix[x][y] == tile_matrix[x+1][y] :
                return True
    return False

def printMatrix() :
    surface.fill(white)


main()
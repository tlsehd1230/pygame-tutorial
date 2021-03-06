import pygame
from color import *
import random

TOTAL_SCORE = 0
BOARD_SIZE = 4

pygame.init()

surface = pygame.display.set_mode((400, 500))

pygame.display.set_caption("2048")

font_40 = pygame.font.SysFont("D2Coding", 40)
font_50 = pygame.font.SysFont("D2Coding", 50)
font_70 = pygame.font.SysFont("D2Coding", 70)

tile_matrix = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

undo_matrix = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
undo_score = 0

def main() :

    gameExit = False
    gameSuccess = False
    successCount = 0
    placeRandomTile()
    placeRandomTile()
    printMatrix()

    while not gameExit :
        if gameSuccess and successCount == 1:
            printSuccess()

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                gameExit = True

            if checkIfcando():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    gameSuccess = False
                    printMatrix()

                if event.type == pygame.KEYDOWN and isArrow(event.key):
                    global undo_matrix
                    for i in range(0, 4):
                        for j in range(0, 4):
                            undo_matrix[i][j] = tile_matrix[i][j]

                    global undo_score
                    undo_score = TOTAL_SCORE

                    rotation_num = getRotationNum(event.key)

                    for number in range(0, rotation_num):
                        rotateCCW()

                    if canMove():
                        moveTiles()
                        mergeTiles()
                        placeRandomTile()

                    for count in range(0, (4 - rotation_num) % 4):
                        rotateCCW()

                    printMatrix()

                    for row in tile_matrix:
                        if 2048 in row:
                            successCount += 1
                            gameSuccess = True

            else:
                printGameOver()


            if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                unDo()

        pygame.display.update()

def rotateCCW() :
    temp = [[0, 0, 0, 0],
            [0, 0, 0, 0] ,
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

    for x in range(0, 4) :
        for y in range(0, 4) :
            temp[x][y] = tile_matrix[x][y]
            tile_matrix[x][y] = 0

    for x in range(0, 4) :
        for y in range(0, 4) :
            tile_matrix[x][y] = temp[y][3-x]

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
    for x in range(0,4) :
        for y in range(0,4) :
            if tile_matrix[x][y] == 0:
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
    pygame.draw.rect(surface, gray, (25, 125, 350, 350))
    for l in range(0,4) :
        for p in range(0,4) :
            pygame.draw.rect(surface, dictionary[tile_matrix[p][l]], (25+87.5*l, 125+87.5*p, 87.5, 87.5))
            if tile_matrix[p][l] != 0 :
                if tile_matrix[p][l] > 999 :
                    selected_font = font_40
                else :
                    selected_font = font_50

                label = selected_font.render(str(tile_matrix[p][l]), True, black)
                width = label.get_width()
                height = label.get_height()
                surface.blit(label, (25+87.5*l+(87.5-width)/2, 125+87.5*p+(87.5-height)/2))
    pygame.draw.rect(surface, gray, (135, 30, 130, 40))
    score_label = font_40.render(str(TOTAL_SCORE), True, black)
    score_width = score_label.get_width()
    score_height = score_label.get_height()
    surface.blit(score_label, (135+(130-score_width)/2, 30+(40-score_height)/2))

def printGameOver() :
    surface.fill(black)
    gameover_label = font_70.render("GAMEOVER", True, white)
    gameover_width = gameover_label.get_width()
    gameover_height = gameover_label.get_height()
    surface.blit(gameover_label, ((400-gameover_width)/2,(500-gameover_height)/2))

def printSuccess() :
    surface.fill(white)
    success_label = font_70.render("YOU WIN", True, color16)
    success_width = success_label.get_width()
    success_height = success_label.get_height()
    surface.blit(success_label, ((400-success_width)/2,(500-success_height)/2))

def placeRandomTile() :
    rand_x = random.randrange(0,4)
    rand_y = random.randrange(0,4)
    while tile_matrix[rand_x][rand_y] != 0 :
        rand_x = random.randrange(0, 4)
        rand_y = random.randrange(0, 4)
    list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
    tile_matrix[rand_x][rand_y] = random.choice(list)

def canMove() :
    for x in range(0,3) :
        for y in range(0,4) :
            if (tile_matrix[x][y] == tile_matrix[x+1][y] and tile_matrix[x][y] != 0) or (tile_matrix[x][y] == 0 and tile_matrix[x+1][y] != 0) :
                return True
    return False

def moveTiles() :
    for y in range(0,4) :
        list = []
        for x in range(0,4) :
            if tile_matrix[x][y] != 0 :
                list.append(tile_matrix[x][y])

        for x in range(0, len(list)) :
            tile_matrix[x][y] = list[x]

        for x in range(len(list), 4) :
            tile_matrix[x][y] = 0

def mergeTiles() :
    for y in range(0,4) :
        for x in range(0,3) :
            if  tile_matrix[x][y] == tile_matrix[x + 1][y] and tile_matrix[x][y] != 0 :
                tile_matrix[x][y] += tile_matrix[x + 1][y]

                global TOTAL_SCORE
                TOTAL_SCORE += tile_matrix[x][y]
                tile_matrix[x + 1][y] = 0
                moveTiles()

def unDo():
    global TOTAL_SCORE
    global tile_matrix
    TOTAL_SCORE = undo_score

    for i in range(0, 4):
        for j in range(0, 4):
            tile_matrix[i][j] = undo_matrix[i][j]

    printMatrix()

main()

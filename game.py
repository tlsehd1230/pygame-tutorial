import pygame

pygame.init()

white = (255, 255, 255)
yellow = (235, 243, 65)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("2048")

gameTerminate = False
X = 200
Y = 100
X_change = 0
Y_change = 0

clock = pygame.time.Clock()

while not gameTerminate :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameTerminate = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :

                pygame.draw.rect(gameDisplay, yellow, (X, Y, 400, 400))
                pygame.display.update()
            if event.key == pygame.K_RIGHT :
                X_change = 5
                Y_change = 0
            if event.key == pygame.K_UP :
                Y_change = -5
                X_change = 0
            if event.key == pygame.K_DOWN :
                Y_change = 5
                X_change = 0

            X += X_change
            Y += Y_change
    clock.tick(30)

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, yellow, (X, Y, 400, 400))
    pygame.display.update()

pygame.quit()

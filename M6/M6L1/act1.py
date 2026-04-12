import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

gray = (128, 128, 128)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(gray)

    pygame.display.flip()

pygame.quit()
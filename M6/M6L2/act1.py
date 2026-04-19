import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rectangle Control")

black = (0, 0, 0)
blue = (0, 125, 255)

x, y = 0 , 0
w, h = 100 , 100
speed = 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill(black)
    pygame.draw.rect(screen, blue, (x, y, w, h))
    pygame.display.flip()
    clock.tick(60)
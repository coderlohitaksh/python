import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Circle")

clock = pygame.time.Clock()

radius = 20
x, y = WIDTH // 2, HEIGHT // 2

dx, dy = 4, 4
speed_multiplier = 1.0

color = (0, 255, 255)

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dx -= 0.2
    if keys[pygame.K_RIGHT]:
        dx += 0.2
    if keys[pygame.K_UP]:
        dy -= 0.2
    if keys[pygame.K_DOWN]:
        dy += 0.2

    x += dx * speed_multiplier
    y += dy * speed_multiplier

    if x - radius <= 0 or x + radius >= WIDTH:
        dx = -dx
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    if y - radius <= 0 or y + radius >= HEIGHT:
        dy = -dy
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    speed_multiplier += 0.0005

    pygame.draw.circle(screen, color, (int(x), int(y)), radius)

    pygame.display.flip()
    clock.tick(60)
[
    
]
pygame\
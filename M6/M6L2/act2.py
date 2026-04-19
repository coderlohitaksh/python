import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Inertia Movement")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

solid_x, solid_y = 150, 200
hollow_x, hollow_y = 400, 200

solid_radius = 50
hollow_radius = 70

solid_vx, solid_vy = 0, 0
hollow_vx, hollow_vy = 0, 0

acceleration = 600
friction = 0.9
max_speed = 300

clock = pygame.time.Clock()

while True:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        solid_vx -= acceleration * dt
    if keys[pygame.K_RIGHT]:
        solid_vx += acceleration * dt
    if keys[pygame.K_UP]:
        solid_vy -= acceleration * dt
    if keys[pygame.K_DOWN]:
        solid_vy += acceleration * dt

    if keys[pygame.K_a]:
        hollow_vx -= acceleration * dt
    if keys[pygame.K_d]:
        hollow_vx += acceleration * dt
    if keys[pygame.K_w]:
        hollow_vy -= acceleration * dt
    if keys[pygame.K_s]:
        hollow_vy += acceleration * dt

    # --- APPLY FRICTION ---
    solid_vx *= friction
    solid_vy *= friction
    hollow_vx *= friction
    hollow_vy *= friction

    # --- LIMIT SPEED ---
    solid_vx = max(-max_speed, min(max_speed, solid_vx))
    solid_vy = max(-max_speed, min(max_speed, solid_vy))
    hollow_vx = max(-max_speed, min(max_speed, hollow_vx))
    hollow_vy = max(-max_speed, min(max_speed, hollow_vy))

    # --- UPDATE POSITIONS ---
    solid_x += solid_vx * dt
    solid_y += solid_vy * dt

    hollow_x += hollow_vx * dt
    hollow_y += hollow_vy * dt

    # --- BOUNDARIES + BOUNCE ---
    if solid_x - solid_radius < 0 or solid_x + solid_radius > WIDTH:
        solid_vx *= -0.7  # bounce + energy loss
    if solid_y - solid_radius < 0 or solid_y + solid_radius > HEIGHT:
        solid_vy *= -0.7

    if hollow_x - hollow_radius < 0 or hollow_x + hollow_radius > WIDTH:
        hollow_vx *= -0.7
    if hollow_y - hollow_radius < 0 or hollow_y + hollow_radius > HEIGHT:
        hollow_vy *= -0.7

    solid_x = max(solid_radius, min(WIDTH - solid_radius, solid_x))
    solid_y = max(solid_radius, min(HEIGHT - solid_radius, solid_y))

    hollow_x = max(hollow_radius, min(WIDTH - hollow_radius, hollow_x))
    hollow_y = max(hollow_radius, min(HEIGHT - hollow_radius, hollow_y))

    screen.fill(WHITE)

    pygame.draw.circle(screen, GREEN, (int(solid_x), int(solid_y)), solid_radius)
    pygame.draw.circle(screen, GREEN, (int(hollow_x), int(hollow_y)), hollow_radius, 3)

    pygame.display.flip()
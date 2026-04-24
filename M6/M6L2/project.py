import pygame
import sys
import random
import math
import os

pygame.init()
pygame.mixer.init()

w, h = 640, 480
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snake Glow Grass")

white = (255, 255, 255)
black = (0, 0, 0)

# 🌿 grass colors
sap_green = (60, 100, 30)
leaf_green = (100, 150, 60)

cell = 20
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# load apple
base_path = os.path.dirname(__file__)
apple_path = os.path.join(base_path, "apple.png")
apple_img = pygame.image.load(apple_path)
apple_img = pygame.transform.scale(apple_img, (cell, cell))

# load highscore
highscore = 0
if os.path.exists("highscore.txt"):
    with open("highscore.txt", "r") as f:
        try:
            highscore = int(f.read())
        except:
            highscore = 0

snake = [(300, 240)]
direction = (cell, 0)
food = (random.randrange(0, w, cell), random.randrange(0, h, cell))

score = 0
speed = 10

# 🌿 static grass background
bg_surface = pygame.Surface((w, h))
for y in range(0, h, cell):
    for x in range(0, w, cell):
        if (x // cell + y // cell) % 2 == 0:
            color = sap_green
        else:
            color = leaf_green
        pygame.draw.rect(bg_surface, color, (x, y, cell, cell))

# ✨ glowing trail particles
trail_particles = []

# draw glowing snake + eyes
def draw_snake():
    for i, segment in enumerate(snake):
        x, y = segment

        for glow_size, alpha in [(34, 30), (26, 50), (18, 80)]:
            glow = pygame.Surface((glow_size, glow_size), pygame.SRCALPHA)
            pygame.draw.rect(glow, (0, 255, 120, alpha), (0, 0, glow_size, glow_size), border_radius=10)
            screen.blit(glow, (x - (glow_size - cell)//2, y - (glow_size - cell)//2))

        pygame.draw.rect(screen, (0, 255, 140), (x, y, cell, cell), border_radius=6)

        if i == 0:
            hx, hy = segment
            fx, fy = food

            eye1 = (hx + 6, hy + 6)
            eye2 = (hx + 14, hy + 6)

            pygame.draw.circle(screen, white, eye1, 4)
            pygame.draw.circle(screen, white, eye2, 4)

            dx = fx - hx
            dy = fy - hy
            dist = math.hypot(dx, dy)
            if dist != 0:
                dx /= dist
                dy /= dist

            pupil1 = (int(eye1[0] + dx * 2), int(eye1[1] + dy * 2))
            pupil2 = (int(eye2[0] + dx * 2), int(eye2[1] + dy * 2))

            pygame.draw.circle(screen, black, pupil1, 2)
            pygame.draw.circle(screen, black, pupil2, 2)

def save_highscore():
    with open("highscore.txt", "w") as f:
        f.write(str(highscore))

def game_over():
    global highscore
    if score > highscore:
        highscore = score
        save_highscore()

    text = font.render("GAME OVER - Press R", True, (255, 50, 50))
    screen.blit(text, (140, 220))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, cell):
                direction = (0, -cell)
            if event.key == pygame.K_DOWN and direction != (0, -cell):
                direction = (0, cell)
            if event.key == pygame.K_LEFT and direction != (cell, 0):
                direction = (-cell, 0)
            if event.key == pygame.K_RIGHT and direction != (-cell, 0):
                direction = (cell, 0)

    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    if (
        new_head[0] < 0 or new_head[0] >= w or
        new_head[1] < 0 or new_head[1] >= h or
        new_head in snake
    ):
        game_over()
        snake = [(300, 240)]
        direction = (cell, 0)
        food = (random.randrange(0, w, cell), random.randrange(0, h, cell))
        score = 0
        speed = 10
        trail_particles.clear()
        continue

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        speed += 0.3
        food = (random.randrange(0, w, cell), random.randrange(0, h, cell))
    else:
        snake.pop()

    # ✨ add trail particles
    trail_particles.append([new_head[0], new_head[1], 255])

    # 🌿 draw background
    screen.blit(bg_surface, (0, 0))

    # ✨ draw fading glow trail (does NOT affect background)
    for p in trail_particles[:]:
        x, y, alpha = p

        for size, a in [(30, alpha//6), (20, alpha//4), (12, alpha//2)]:
            glow = pygame.Surface((size, size), pygame.SRCALPHA)
            pygame.draw.rect(glow, (0, 255, 120, a), (0, 0, size, size), border_radius=8)
            screen.blit(glow, (x - (size - cell)//2, y - (size - cell)//2))

        p[2] -= 10
        if p[2] <= 0:
            trail_particles.remove(p)

    draw_snake()
    screen.blit(apple_img, food)

    score_text = font.render(f"Score: {score}", True, white)
    high_text = font.render(f"High: {highscore}", True, white)

    screen.blit(score_text, (10, 10))
    screen.blit(high_text, (10, 40))

    pygame.display.flip()
    clock.tick(speed)
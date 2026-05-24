import pygame
import random
import math

pygame.init()

WIDTH = 1280
HEIGHT = 720
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ULTIMATE PLATFORMER")

clock = pygame.time.Clock()

GRAVITY = 0.9
FRICTION = 0.8

WHITE = (255, 255, 255)
BLACK = (15, 15, 15)
RED = (255, 70, 70)
GREEN = (60, 220, 100)
BLUE = (70, 150, 255)
YELLOW = (255, 220, 70)
PURPLE = (170, 90, 255)
CYAN = (70, 255, 255)
ORANGE = (255, 140, 50)

font = pygame.font.SysFont("Arial", 30)
big_font = pygame.font.SysFont("Arial", 80)

camera_x = 0

particles = []


class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = random.randint(3, 7)

        self.vel_x = random.uniform(-5, 5)
        self.vel_y = random.uniform(-8, -2)

        self.life = 40

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y

        self.vel_y += 0.25

        self.life -= 1

    def draw(self):
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x - camera_x), int(self.y)),
            self.radius
        )


class Player:
    def __init__(self):

        self.width = 50
        self.height = 70

        self.rect = pygame.Rect(100, 400, self.width, self.height)

        self.vel_x = 0
        self.vel_y = 0

        self.speed = 1
        self.max_speed = 10

        self.jump_strength = 18

        self.on_ground = False

        self.health = 5

        self.double_jump = True

        self.dash_cooldown = 0

        self.facing = 1

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.vel_x -= self.speed
            self.facing = -1

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.vel_x += self.speed
            self.facing = 1

        self.vel_x *= FRICTION

        if self.vel_x > self.max_speed:
            self.vel_x = self.max_speed

        if self.vel_x < -self.max_speed:
            self.vel_x = -self.max_speed

        self.rect.x += self.vel_x

        for platform in platforms:

            if self.rect.colliderect(platform):

                if self.vel_x > 0:
                    self.rect.right = platform.left

                if self.vel_x < 0:
                    self.rect.left = platform.right

        self.vel_y += GRAVITY

        if self.vel_y > 20:
            self.vel_y = 20

        self.rect.y += self.vel_y

        self.on_ground = False

        for platform in platforms:

            if self.rect.colliderect(platform):

                if self.vel_y > 0:
                    self.rect.bottom = platform.top
                    self.vel_y = 0
                    self.on_ground = True
                    self.double_jump = True

                elif self.vel_y < 0:
                    self.rect.top = platform.bottom
                    self.vel_y = 0

        if self.rect.y > HEIGHT + 300:
            self.damage()

        if self.dash_cooldown > 0:
            self.dash_cooldown -= 1

    def jump(self):

        if self.on_ground:
            self.vel_y = -self.jump_strength

        elif self.double_jump:
            self.vel_y = -self.jump_strength
            self.double_jump = False

            for i in range(20):
                particles.append(
                    Particle(
                        self.rect.centerx,
                        self.rect.centery,
                        PURPLE
                    )
                )

    def dash(self):

        if self.dash_cooldown == 0:

            self.vel_x = 30 * self.facing

            self.dash_cooldown = 50

            for i in range(25):
                particles.append(
                    Particle(
                        self.rect.centerx,
                        self.rect.centery,
                        CYAN
                    )
                )

    def damage(self):

        self.health -= 1

        self.rect.x = 100
        self.rect.y = 400

        self.vel_x = 0
        self.vel_y = 0

        for i in range(35):
            particles.append(
                Particle(
                    self.rect.centerx,
                    self.rect.centery,
                    RED
                )
            )

    def draw(self):

        pygame.draw.rect(
            screen,
            CYAN,
            (
                self.rect.x - camera_x,
                self.rect.y,
                self.width,
                self.height
            ),
            border_radius=10
        )

        eye_x = self.rect.x - camera_x + 35

        if self.facing == -1:
            eye_x = self.rect.x - camera_x + 10

        pygame.draw.circle(
            screen,
            WHITE,
            (eye_x, self.rect.y + 20),
            6
        )


class Enemy:
    def __init__(self, x, y, distance):

        self.rect = pygame.Rect(x, y, 50, 50)

        self.start_x = x
        self.distance = distance

        self.speed = 3

    def update(self):

        self.rect.x += self.speed

        if self.rect.x > self.start_x + self.distance:
            self.speed *= -1

        if self.rect.x < self.start_x:
            self.speed *= -1

    def draw(self):

        pygame.draw.rect(
            screen,
            RED,
            (
                self.rect.x - camera_x,
                self.rect.y,
                50,
                50
            ),
            border_radius=10
        )

        pygame.draw.circle(
            screen,
            WHITE,
            (self.rect.x - camera_x + 15, self.rect.y + 15),
            5
        )

        pygame.draw.circle(
            screen,
            WHITE,
            (self.rect.x - camera_x + 35, self.rect.y + 15),
            5
        )


class Coin:
    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.rect = pygame.Rect(x, y, 25, 25)

        self.time = random.randint(0, 100)

    def update(self):
        self.time += 0.1

    def draw(self):

        offset = math.sin(self.time) * 8

        pygame.draw.circle(
            screen,
            YELLOW,
            (
                int(self.x - camera_x + 12),
                int(self.y + offset + 12)
            ),
            12
        )


player = Player()

platforms = [
    pygame.Rect(0, 650, 7000, 100),

    pygame.Rect(300, 500, 220, 25),
    pygame.Rect(650, 400, 220, 25),
    pygame.Rect(1000, 320, 220, 25),
    pygame.Rect(1450, 450, 220, 25),
    pygame.Rect(1850, 350, 220, 25),
    pygame.Rect(2250, 250, 220, 25),
    pygame.Rect(2700, 450, 220, 25),
    pygame.Rect(3150, 350, 220, 25),
    pygame.Rect(3650, 250, 220, 25),
    pygame.Rect(4200, 400, 220, 25),
    pygame.Rect(4700, 300, 220, 25),
]

lava = [
    pygame.Rect(2400, 680, 300, 40),
    pygame.Rect(3900, 680, 400, 40),
]

enemies = [
    Enemy(700, 600, 250),
    Enemy(1600, 400, 250),
    Enemy(3300, 300, 300),
    Enemy(4700, 250, 200),
]

coins = []

for i in range(35):

    x = random.randint(300, 5000)
    y = random.randint(120, 550)

    coins.append(Coin(x, y))

score = 0

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                player.jump()

            if event.key == pygame.K_LSHIFT:
                player.dash()

            if event.key == pygame.K_r:

                player.health = 5
                score = 0

                player.rect.x = 100
                player.rect.y = 400

    player.move()

    camera_x = player.rect.centerx - WIDTH // 2

    if camera_x < 0:
        camera_x = 0

    for enemy in enemies:

        enemy.update()

        if player.rect.colliderect(enemy.rect):
            player.damage()

    for lava_block in lava:

        if player.rect.colliderect(lava_block):
            player.damage()

    for coin in coins[:]:

        coin.update()

        if player.rect.colliderect(coin.rect):

            score += 1

            coins.remove(coin)

            for i in range(25):
                particles.append(
                    Particle(
                        coin.x,
                        coin.y,
                        YELLOW
                    )
                )

    screen.fill((20, 20, 35))

    for i in range(200):

        star_x = (i * 350) % 7000
        star_y = (i * 73) % HEIGHT

        pygame.draw.circle(
            screen,
            WHITE,
            (
                int(star_x - camera_x * 0.2),
                star_y
            ),
            2
        )

    for lava_block in lava:

        pygame.draw.rect(
            screen,
            ORANGE,
            (
                lava_block.x - camera_x,
                lava_block.y,
                lava_block.width,
                lava_block.height
            )
        )

    for platform in platforms:

        pygame.draw.rect(
            screen,
            GREEN,
            (
                platform.x - camera_x,
                platform.y,
                platform.width,
                platform.height
            ),
            border_radius=8
        )

    for enemy in enemies:
        enemy.draw()

    for coin in coins:
        coin.draw()

    player.draw()

    for particle in particles[:]:

        particle.update()
        particle.draw()

        if particle.life <= 0:
            particles.remove(particle)

    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, 90))

    score_text = font.render(f"COINS: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

    health_text = font.render(f"HP: {player.health}", True, WHITE)
    screen.blit(health_text, (20, 50))

    controls = font.render(
        "A/D MOVE   SPACE JUMP   SHIFT DASH   DOUBLE JUMP",
        True,
        WHITE
    )

    screen.blit(controls, (320, 25))

    if player.health <= 0:

        text = big_font.render("GAME OVER", True, RED)
        screen.blit(text, (380, 250))

        retry = font.render("PRESS R TO RESTART", True, WHITE)
        screen.blit(retry, (500, 360))

    if score >= 35:

        text = big_font.render("YOU WIN!", True, YELLOW)
        screen.blit(text, (430, 250))

    pygame.display.update()

pygame.quit()
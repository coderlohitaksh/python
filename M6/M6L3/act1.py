import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 1280, 720
FPS = 165

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("COSMIC NEON CORE")

clock = pygame.time.Clock()

particles = []
stars = []

time_passed = 0


def neon(hue, sat=100, val=100):
    color = pygame.Color(0)
    color.hsva = (hue % 360, sat, val, 100)
    return color


class Star:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed = random.uniform(0.5, 4)
        self.size = random.randint(1, 3)

    def update(self):
        self.y += self.speed

        if self.y > HEIGHT:
            self.reset()
            self.y = 0

    def draw(self):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.x), int(self.y)),
            self.size
        )


class Particle:
    def __init__(self, x, y, hue):
        self.x = x
        self.y = y

        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(1, 7)

        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed

        self.life = random.randint(30, 70)
        self.size = random.randint(2, 6)
        self.hue = hue

    def update(self):
        self.x += self.dx
        self.y += self.dy

        self.dx *= 0.98
        self.dy *= 0.98

        self.life -= 1

    def draw(self):
        if self.life <= 0:
            return

        alpha = max(0, self.life * 3)

        surf = pygame.Surface((80, 80), pygame.SRCALPHA)

        pygame.draw.circle(
            surf,
            (*neon(self.hue)[:3], alpha),
            (40, 40),
            self.size * 2
        )

        screen.blit(surf, (self.x - 40, self.y - 40))


class CosmicOrb:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2

        self.radius = 80

        self.vel_x = 6
        self.vel_y = 5

        self.hue = 0
        self.rotation = 0

        self.pulse = 0

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y

        self.rotation += 2
        self.hue += 1.5
        self.pulse += 0.1

        dynamic_radius = self.radius + math.sin(self.pulse) * 10

        if self.x - dynamic_radius <= 0 or self.x + dynamic_radius >= WIDTH:
            self.vel_x *= -1

            for _ in range(60):
                particles.append(
                    Particle(self.x, self.y, self.hue)
                )

        if self.y - dynamic_radius <= 0 or self.y + dynamic_radius >= HEIGHT:
            self.vel_y *= -1

            for _ in range(60):
                particles.append(
                    Particle(self.x, self.y, self.hue)
                )

    def draw(self):
        dynamic_radius = self.radius + math.sin(self.pulse) * 10

        for layer in range(8, 0, -1):
            glow_radius = int(dynamic_radius + layer * 12)

            alpha = 15

            glow_surface = pygame.Surface(
                (glow_radius * 2, glow_radius * 2),
                pygame.SRCALPHA
            )

            pygame.draw.circle(
                glow_surface,
                (*neon(self.hue)[:3], alpha),
                (glow_radius, glow_radius),
                glow_radius
            )

            screen.blit(
                glow_surface,
                (
                    self.x - glow_radius,
                    self.y - glow_radius
                )
            )

        pygame.draw.circle(
            screen,
            neon(self.hue),
            (int(self.x), int(self.y)),
            int(dynamic_radius)
        )

        skull_font = pygame.font.SysFont(
            "segoe ui emoji",
            int(dynamic_radius)
        )

        skull = skull_font.render(
            "☠️",
            True,
            (255, 255, 255)
        )

        skull_rect = skull.get_rect(
            center=(int(self.x), int(self.y))
        )

        screen.blit(skull, skull_rect)

        for i in range(12):
            angle = math.radians((360 / 12) * i + self.rotation)

            ring_x = self.x + math.cos(angle) * (dynamic_radius + 35)
            ring_y = self.y + math.sin(angle) * (dynamic_radius + 35)

            pygame.draw.circle(
                screen,
                neon(self.hue + i * 20),
                (int(ring_x), int(ring_y)),
                10
            )


for _ in range(250):
    stars.append(Star())

orb = CosmicOrb()

font_big = pygame.font.SysFont("consolas", 50, bold=True)
font_small = pygame.font.SysFont("consolas", 22)

running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time_passed += 0.01

    bg = (
        int(10 + math.sin(time_passed) * 10),
        int(10 + math.cos(time_passed) * 10),
        int(20 + math.sin(time_passed * 2) * 20)
    )

    screen.fill(bg)

    for star in stars:
        star.update()
        star.draw()

    orb.update()
    orb.draw()

    for particle in particles[:]:
        particle.update()
        particle.draw()

        if particle.life <= 0:
            particles.remove(particle)

    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

    for y in range(0, HEIGHT, 4):
        alpha = random.randint(0, 10)

        pygame.draw.line(
            overlay,
            (255, 255, 255, alpha),
            (0, y),
            (WIDTH, y)
        )

    screen.blit(overlay, (0, 0))

    title = font_big.render(
        "COSMIC NEON CORE",
        True,
        neon(orb.hue + 100)
    )

    subtitle = font_small.render(
        "ENERGY SYSTEM ACTIVE",
        True,
        (220, 220, 220)
    )

    screen.blit(title, (40, 35))
    screen.blit(subtitle, (45, 95))

    pygame.display.flip()

pygame.quit()
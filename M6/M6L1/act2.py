import pygame
import sys
import math
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
FPS = 60

BG_COLOR = (120, 120, 120)

PLAYER_SPEED = 300
FRICTION = 0.85

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Penguin game")
clock = pygame.time.Clock()

base_font_size = 42

def load_image(path, size=None, alpha=False):
    try:
        image = pygame.image.load(path)
        image = image.convert_alpha() if alpha else image.convert()
        if size:
            image = pygame.transform.scale(image, size)
        return image
    except pygame.error as e:
        print(f"Error loading {path}: {e}")
        sys.exit()

background = load_image("background.png", (SCREEN_WIDTH, SCREEN_HEIGHT))
background.set_alpha(180)

penguin_img = load_image("penguin.png", (150, 150), alpha=True)

class Penguin:
    def __init__(self):
        self.image = penguin_img
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.velocity = pygame.Vector2(0, 0)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        acc = pygame.Vector2(0, 0)

        if keys[pygame.K_LEFT]:
            acc.x = -1
        if keys[pygame.K_RIGHT]:
            acc.x = 1
        if keys[pygame.K_UP]:
            acc.y = -1
        if keys[pygame.K_DOWN]:
            acc.y = 1

        if acc.length() > 0:
            acc = acc.normalize()

        self.velocity += acc * PLAYER_SPEED / 60

    def apply_friction(self):
        self.velocity *= FRICTION

    def update(self, dt):
        self.rect.x += self.velocity.x * dt * 60
        self.rect.y += self.velocity.y * dt * 60
        self.rect.clamp_ip(screen.get_rect())

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Game:
    def __init__(self):
        self.running = True
        self.penguin = Penguin()
        self.time = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt):
        self.time += dt
        self.penguin.handle_input()
        self.penguin.apply_friction()
        self.penguin.update(dt)

    def draw(self):
        screen.fill(BG_COLOR)
        screen.blit(background, (0, 0))
        self.penguin.draw(screen)

        r = int((math.sin(self.time * 2) + 1) * 127)
        g = int((math.sin(self.time * 2 + 2) + 1) * 127)
        b = int((math.sin(self.time * 2 + 4) + 1) * 127)
        color = (r, g, b)

        flicker = 1 + random.uniform(-0.08, 0.08)
        scale = (1 + 0.25 * math.sin(self.time * 3)) * flicker

        dynamic_size = int(base_font_size * scale)
        font_main = pygame.font.SysFont("arial", dynamic_size, bold=True)

        text_str = "penguin hello !"

        for glow_size, alpha in [(14, 25), (10, 40), (6, 70), (3, 120)]:
            glow_font = pygame.font.SysFont("arial", dynamic_size + glow_size, bold=True)
            glow = glow_font.render(text_str, True, color)
            glow.set_alpha(alpha)
            rect = glow.get_rect(center=(SCREEN_WIDTH // 2, 80))
            screen.blit(glow, rect)

        core_outer = font_main.render(text_str, True, color)
        core_outer.set_alpha(180)
        rect_outer = core_outer.get_rect(center=(SCREEN_WIDTH // 2, 80))
        screen.blit(core_outer, rect_outer)

        core_inner = font_main.render(text_str, True, (255, 255, 255))
        rect_inner = core_inner.get_rect(center=(SCREEN_WIDTH // 2, 80))
        screen.blit(core_inner, rect_inner)

        pygame.display.flip()

    def run(self):
        while self.running:
            dt = clock.tick(FPS) / 1000
            self.events()
            self.update(dt)
            self.draw()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Game().run()

import pygame
import random

pygame.init()

WIDTH = 1000
HEIGHT = 650
GROUND_Y = 560

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Fighter")

clock = pygame.time.Clock()

WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
RED = (220, 70, 70)
BLUE = (70, 120, 255)
GREEN = (50, 220, 50)
YELLOW = (255, 220, 50)
DARK_RED = (120, 0, 0)

font = pygame.font.SysFont("arial", 28)
big_font = pygame.font.SysFont("arial", 64)


class Particle:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.vx = random.uniform(-4, 4)
        self.vy = random.uniform(-5, -1)

        self.life = random.randint(15, 30)
        self.radius = random.randint(2, 5)

    def update(self):

        self.x += self.vx
        self.y += self.vy

        self.vy += 0.2

        self.life -= 1

    def draw(self, surf):

        if self.life > 0:

            pygame.draw.circle(
                surf,
                YELLOW,
                (int(self.x), int(self.y)),
                self.radius
            )


class Fighter:

    def __init__(self, x, color):

        self.x = x
        self.color = color

        self.width = 70
        self.height = 110

        self.rect = pygame.Rect(
            x,
            GROUND_Y - self.height,
            self.width,
            self.height
        )

        self.health = 150

        self.speed = 8

        self.vel_y = 0

        self.gravity = 0.7
        self.jump_power = -13

        self.on_ground = True
        self.jumps_left = 1

        self.attack_timer = 0
        self.hit_timer = 0

        self.facing = 1

        self.combo = 0
        self.combo_timer = 0

        self.rounds = 0

    def move(self, direction):

        self.rect.x += direction * self.speed

        if direction > 0:
            self.facing = 1

        if direction < 0:
            self.facing = -1

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def jump(self):

        if self.jumps_left > 0:

            self.vel_y = self.jump_power
            self.jumps_left -= 1
            self.on_ground = False

    def apply_gravity(self):

        self.vel_y += self.gravity

        self.rect.y += self.vel_y

        if self.rect.bottom >= GROUND_Y:

            self.rect.bottom = GROUND_Y

            self.vel_y = 0

            self.on_ground = True
            self.jumps_left = 1

    def attack(self, enemy):

        if self.attack_timer > 0:
            return []

        self.attack_timer = 18

        if self.facing == 1:

            hitbox = pygame.Rect(
                self.rect.right,
                self.rect.y + 20,
                90,
                70
            )

        else:

            hitbox = pygame.Rect(
                self.rect.left - 90,
                self.rect.y + 20,
                90,
                70
            )

        particles = []

        if hitbox.colliderect(enemy.rect):

            damage = random.randint(8, 14)

            enemy.health -= damage

            enemy.hit_timer = 8

            enemy.rect.x += self.facing * 25

            if self.combo_timer > 0:
                self.combo += 1
            else:
                self.combo = 1

            self.combo_timer = 90

            for _ in range(12):

                particles.append(
                    Particle(
                        enemy.rect.centerx,
                        enemy.rect.centery
                    )
                )

        return particles

    def update(self):

        self.apply_gravity()

        if self.attack_timer > 0:
            self.attack_timer -= 1

        if self.hit_timer > 0:
            self.hit_timer -= 1

        if self.combo_timer > 0:
            self.combo_timer -= 1
        else:
            self.combo = 0

    def draw(self, surf):

        body_color = self.color

        if self.hit_timer > 0:
            body_color = WHITE

        pygame.draw.circle(
            surf,
            (255, 220, 180),
            (self.rect.centerx, self.rect.y + 20),
            16
        )

        pygame.draw.rect(
            surf,
            body_color,
            (
                self.rect.x + 15,
                self.rect.y + 38,
                40,
                45
            ),
            border_radius=8
        )

        pygame.draw.line(
            surf,
            BLACK,
            (
                self.rect.centerx,
                self.rect.y + 83
            ),
            (
                self.rect.centerx - 12,
                self.rect.bottom
            ),
            4
        )

        pygame.draw.line(
            surf,
            BLACK,
            (
                self.rect.centerx,
                self.rect.y + 83
            ),
            (
                self.rect.centerx + 12,
                self.rect.bottom
            ),
            4
        )

        pygame.draw.line(
            surf,
            BLACK,
            (
                self.rect.centerx,
                self.rect.y + 55
            ),
            (
                self.rect.centerx - 18,
                self.rect.y + 68
            ),
            4
        )

        pygame.draw.line(
            surf,
            BLACK,
            (
                self.rect.centerx,
                self.rect.y + 55
            ),
            (
                self.rect.centerx + 18,
                self.rect.y + 68
            ),
            4
        )

        eye_x = self.rect.centerx + self.facing * 4

        pygame.draw.circle(
            surf,
            BLACK,
            (
                eye_x,
                self.rect.y + 18
            ),
            2
        )

        pygame.draw.arc(
            surf,
            BLACK,
            (
                self.rect.centerx - 5,
                self.rect.y + 24,
                10,
                6
            ),
            0,
            3.14,
            1
        )


def draw_health(x, y, hp):

    pygame.draw.rect(
        screen,
        DARK_RED,
        (x, y, 300, 25)
    )

    pygame.draw.rect(
        screen,
        GREEN,
        (
            x,
            y,
            max(0, hp * 2),
            25
        )
    )

    pygame.draw.rect(
        screen,
        BLACK,
        (x, y, 300, 25),
        2
    )


player1 = Fighter(200, RED)
player2 = Fighter(700, BLUE)

particles = []

winner = ""
game_over = False

round_time = 99 * 60
def reset_round():

    player1.rect.x = 200
    player1.rect.bottom = GROUND_Y

    player2.rect.x = 700
    player2.rect.bottom = GROUND_Y

    player1.health = 150
    player2.health = 150

    player1.vel_y = 0
    player2.vel_y = 0

    player1.jumps_left = 1
    player2.jumps_left = 1

    player1.combo = 0
    player2.combo = 0

    return 99 * 60


running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if not game_over:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    player1.jump()

                if event.key == pygame.K_w:
                    player2.jump()

    if not game_over:

        keys = pygame.key.get_pressed()

        moved1 = False
        moved2 = False

        if keys[pygame.K_LEFT]:
            player1.move(-1)
            moved1 = True

        if keys[pygame.K_RIGHT]:
            player1.move(1)
            moved1 = True

        if keys[pygame.K_a]:
            player2.move(-1)
            moved2 = True

        if keys[pygame.K_d]:
            player2.move(1)
            moved2 = True

        if keys[pygame.K_RSHIFT]:
            particles.extend(
                player1.attack(player2)
            )

        if keys[pygame.K_SPACE]:
            particles.extend(
                player2.attack(player1)
            )

        player1.update()
        player2.update()

        round_time -= 1

        if player1.health <= 0:

            player2.rounds += 1
            round_time = reset_round()

        if player2.health <= 0:

            player1.rounds += 1
            round_time = reset_round()

        if round_time <= 0:

            if player1.health > player2.health:
                player1.rounds += 1

            elif player2.health > player1.health:
                player2.rounds += 1

            round_time = reset_round()

        if player1.rounds >= 2:
            winner = "RED PLAYER WINS!"
            game_over = True

        if player2.rounds >= 2:
            winner = "BLUE PLAYER WINS!"
            game_over = True

    for particle in particles[:]:

        particle.update()

        if particle.life <= 0:
            particles.remove(particle)

    screen.fill((230, 235, 255))

    pygame.draw.rect(
        screen,
        (120, 190, 120),
        (
            0,
            GROUND_Y,
            WIDTH,
            HEIGHT - GROUND_Y
        )
    )

    pygame.draw.rect(
        screen,
        (170, 170, 170),
        (
            0,
            GROUND_Y - 10,
            WIDTH,
            10
        )
    )

    pygame.draw.circle(
        screen,
        (255, 255, 180),
        (850, 90),
        45
    )

    draw_health(
        30,
        25,
        player1.health
    )

    draw_health(
        WIDTH - 330,
        25,
        player2.health
    )

    timer_text = font.render(
        str(max(0, round_time // 60)),
        True,
        BLACK
    )

    screen.blit(
        timer_text,
        (
            WIDTH // 2 - timer_text.get_width() // 2,
            20
        )
    )

    score_text = font.render(
        f"{player1.rounds} - {player2.rounds}",
        True,
        BLACK
    )

    screen.blit(
        score_text,
        (
            WIDTH // 2 - score_text.get_width() // 2,
            55
        )
    )

    combo1 = font.render(
        f"Combo {player1.combo}",
        True,
        BLACK
    )

    combo2 = font.render(
        f"Combo {player2.combo}",
        True,
        BLACK
    )

    screen.blit(combo1, (30, 60))

    screen.blit(
        combo2,
        (
            WIDTH - combo2.get_width() - 30,
            60
        )
    )

    player1.draw(screen)
    player2.draw(screen)

    for particle in particles:
        particle.draw(screen)

    controls = pygame.font.SysFont(
        "arial",
        20
    ).render(
        "RED: Arrows + Right Shift    BLUE: WASD + Space",
        True,
        BLACK
    )

    screen.blit(
        controls,
        (
            WIDTH // 2 - controls.get_width() // 2,
            HEIGHT - 35
        )
    )

    if game_over:

        overlay = pygame.Surface(
            (WIDTH, HEIGHT)
        )

        overlay.set_alpha(180)
        overlay.fill(BLACK)

        screen.blit(
            overlay,
            (0, 0)
        )

        win_text = big_font.render(
            winner,
            True,
            YELLOW
        )

        screen.blit(
            win_text,
            (
                WIDTH // 2 -
                win_text.get_width() // 2,
                HEIGHT // 2 - 50
            )
        )

        restart_text = font.render(
            "Close Window To Exit",
            True,
            WHITE
        )

        screen.blit(
            restart_text,
            (
                WIDTH // 2 -
                restart_text.get_width() // 2,
                HEIGHT // 2 + 30
            )
        )

    pygame.display.flip()

pygame.quit()
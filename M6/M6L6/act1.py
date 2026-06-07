import pygame
import math
import random
from pygame import mixer

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")
bg = pygame.image.load("space_bg.jpg")
bg = pygame.transform.scale(bg, (800, 600))
mixer.music.load("bg_music.mp3")
mixer.music.play(-1)
icon = pygame.image.load("ufo.png") 
pygame.display.set_icon(icon)

playerImg = pygame.image.load("001-rocket.png")
playerX = 370
playerY = 480
playerX_change = 0

alienImg = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
alien_alpha = []
alien_respawn_timer = []
num_of_enemy = 6

for i in range(num_of_enemy):
    alienImg.append(pygame.image.load("ufo.png").convert_alpha())
    alienX.append(random.randint(0, 736))
    alienY.append(random.randint(50, 150))
    alienX_change.append(random.choice([-200, 200]))
    alienY_change.append(40)
    alien_alpha.append(255)
    alien_respawn_timer.append(0)

bulletImg = pygame.image.load("bullet.png")
bullet_speed = 600
bullets = []
fire_hold = False
fire_rate = 0.2
fire_timer = 0
bullet_sound = mixer.Sound("fire.mp3")
boom_sound = mixer.Sound("boom.mp3")

shield = False
shieldImg = pygame.Surface((80, 80), pygame.SRCALPHA)
pygame.draw.circle(shieldImg, (0, 150, 255, 100), (40, 40), 40)
shield_timer = 0

boosterImg = pygame.image.load("shield.png")
boosterX = random.randint(50, 750)
boosterY = -100
booster_speed = 100
booster_active = False
booster_timer = 0

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
over_font = pygame.font.Font("freesansbold.ttf", 64)
menu_font = pygame.font.Font("freesansbold.ttf", 48)
textX = 10
textY = 10

shake_duration = 0
shake_magnitude = 5

game_over = False
game_started = False

bossImg = pygame.image.load("boss.png").convert_alpha()
bossImg = pygame.transform.scale(bossImg, (200, 150))
boss_active = False
boss_spawn_timer = 30
bossX = 300
bossY = -200
boss_speedY = 100
boss_speedX = 200
boss_dir = 1
boss_health = 30
boss_bullets = []
boss_bullet_speed = 250
boss_fire_rate = 1.5
boss_fire_timer = 0

def show_score(x, y):
    score = font.render(f"Score : {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))
    if shield:
        screen.blit(shieldImg, (x - 20, y - 20))


def enemy(x, y, i, alpha):
    temp = alienImg[i].copy()
    temp.set_alpha(alpha)
    screen.blit(temp, (x, y))


def fire_bullet(x, y):
    screen.blit(bulletImg, (x + 16, y + 10))


def is_collision(aX, aY, bX, bY):
    return math.sqrt((aX - bX) ** 2 + (aY - bY) ** 2) < 27


def is_player_collision(aX, aY, pX, pY):
    return math.sqrt((aX - pX) ** 2 + (aY - pY) ** 2) < 50


def game_over_text():
    over = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over, (200, 230))
    final = font.render(f"Final Score : {score_value}", True, (255, 255, 255))
    screen.blit(final, (300, 320))
    restart = font.render("Press R to Restart", True, (200, 200, 200))
    screen.blit(restart, (270, 370))


def start_menu():
    title = over_font.render("SPACE INVADER", True, (0, 200, 255))
    prompt = menu_font.render("Press SPACE to Start", True, (255, 255, 255))
    screen.blit(title, (170, 200))
    screen.blit(prompt, (210, 320))


def draw_boss_health():
    if boss_active and boss_health > 0:
        bar_width = 300
        max_hp = 30 + (wave_level - 1) * 10
        health_ratio = boss_health / max_hp
        health_ratio = max(0, min(1, health_ratio))
        pygame.draw.rect(screen, (100, 0, 0), (250, 10, bar_width, 20))
        pygame.draw.rect(screen, (0, 255, 0), (250, 10, int(bar_width * health_ratio), 20))


def draw_glow_circle(surface, x, y, core_radius, color, layers=6):
    for i in range(layers, 0, -1):
        radius = core_radius * (1 + i * 0.25)
        alpha = int(40 + (215 * (i / layers)))
        s = pygame.Surface((int(radius * 2), int(radius * 2)), pygame.SRCALPHA)
        pygame.draw.circle(s, (color[0], color[1], color[2], alpha),
                           (int(radius), int(radius)), int(radius))
        surface.blit(s, (x - radius, y - radius), special_flags=pygame.BLEND_PREMULTIPLIED)
    pygame.draw.circle(surface, color, (int(x), int(y)), core_radius)
alien_health = []
base_alien_health = 5
base_alien_speed = 200
wave_level = 1
wave_interval = 10
next_wave_score = wave_interval

for i in range(num_of_enemy):
    alien_health.append(base_alien_health)


def trigger_wave():
    global wave_level, next_wave_score, boss_health, boss_fire_rate, boss_bullet_speed
    wave_level += 1
    next_wave_score += wave_interval
    for i in range(num_of_enemy):
        alien_health[i] = base_alien_health + (wave_level - 1)
        alien_alpha[i] = 255
        alien_respawn_timer[i] = 0
        alienX[i] = random.randint(0, 736)
        alienY[i] = random.randint(50, 150)
        speed = base_alien_speed + (wave_level - 1) * 50
        alienX_change[i] = random.choice([-speed, speed])
    boss_health = 30 + (wave_level - 1) * 10
    boss_fire_rate = max(0.4, boss_fire_rate - 0.1)
    boss_bullet_speed += (wave_level - 1) * 20

running = True
while running:
    dt = clock.tick(60) / 1000
    screen.fill((0, 0, 0))
    offset_x = offset_y = 0
    if shake_duration > 0:
        offset_x = random.randint(-shake_magnitude, shake_magnitude)
        offset_y = random.randint(-shake_magnitude, shake_magnitude)
        shake_duration -= 1

    screen.blit(bg, (offset_x, offset_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_started and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_started = True
            start_time = pygame.time.get_ticks() / 1000
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            playerX = 370
            playerY = 480
            playerX_change = 0
            score_value = 0
            shield = False
            game_over = False
            bullets.clear()
            boss_active = False
            boss_health = 30
            bossY = -200
            boss_bullets.clear()
            fire_hold = False
            fire_timer = 0
            mixer.music.play(-1)
            wave_level = 1
            next_wave_score = wave_interval
            boss_fire_rate = 1.5
            boss_bullet_speed = 250
            for i in range(num_of_enemy):
                alienX[i] = random.randint(0, 736)
                alienY[i] = random.randint(50, 150)
                alien_alpha[i] = 255
                alien_respawn_timer[i] = 0
                alien_health[i] = base_alien_health
                alienX_change[i] = random.choice([-base_alien_speed, base_alien_speed])
        if not game_over and game_started:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -300
                if event.key == pygame.K_RIGHT:
                    playerX_change = 300
                if event.key == pygame.K_SPACE:
                    fire_hold = True
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    playerX_change = 0
                if event.key == pygame.K_SPACE:
                    fire_hold = False

    if not game_started:
        start_menu()
        pygame.display.update()
        continue

    if not game_over:
        playerX += playerX_change * dt
        playerX = max(0, min(playerX, 736))
        fire_timer -= dt
        if fire_hold and fire_timer <= 0:
            bullets.append([playerX, playerY, 0])
            try:
                bullet_sound.play()
            except:
                pass
            fire_timer = fire_rate

        for i in range(num_of_enemy):
            if alien_respawn_timer[i] > 0:
                alien_respawn_timer[i] -= dt
                if alien_respawn_timer[i] <= 0:
                    alienX[i] = random.randint(0, 736)
                    alienY[i] = random.randint(50, 150)
                    alien_alpha[i] = 0
            if alien_alpha[i] < 255:
                alien_alpha[i] += 400 * dt
                alien_alpha[i] = min(alien_alpha[i], 255)

            speed = base_alien_speed + (wave_level - 1) * 50
            sign = -1 if alienX_change[i] < 0 else 1
            alienX_change[i] = sign * speed
            alienX[i] += alienX_change[i] * dt
            if alienX[i] <= 0:
                alienX_change[i] = speed
                alienY[i] += alienY_change[i]
            elif alienX[i] >= 736:
                alienX_change[i] = -speed
                alienY[i] += alienY_change[i]

            for b in bullets[:]:
                if is_collision(alienX[i], alienY[i], b[0], b[1]) and alien_alpha[i] == 255:
                    bullets.remove(b)
                    alien_health[i] -= 1
                    shake_duration = 5
                    if alien_health[i] <= 0:
                        try:
                            boom_sound.play()
                        except:
                            pass
                        score_value += 1
                        shake_duration = 10
                        alien_alpha[i] = 0
                        alien_respawn_timer[i] = 0.5
                        alien_health[i] = base_alien_health + (wave_level - 1)

            if is_player_collision(alienX[i], alienY[i], playerX, playerY) and alien_alpha[i] == 255:
                if shield:
                    shield = False
                    shake_duration = 20
                    alien_alpha[i] = 0
                    alien_respawn_timer[i] = 1
                else:
                    game_over = True
                    shake_duration = 60
                    shake_magnitude = 20
                    mixer.music.stop()

            enemy(alienX[i] + offset_x, alienY[i] + offset_y, i, alien_alpha[i])

        for b in bullets[:]:
            b[1] -= bullet_speed * dt
            fire_bullet(b[0] + offset_x, b[1] + offset_y)
            if b[1] <= 0:
                bullets.remove(b)

        if score_value >= next_wave_score:
            trigger_wave()

        current_time = pygame.time.get_ticks() / 1000
        if current_time - start_time >= boss_spawn_timer and not boss_active:
            boss_active = True
            bossY = -200
            boss_health = 30 + (wave_level - 1) * 10
            boss_spawn_timer += 30
            boss_bullets.clear()
            boss_dir = random.choice([-1, 1])

        if boss_active:
            if bossY < 100:
                bossY += boss_speedY * dt
            else:
                bossX += boss_speedX * dt * boss_dir
                if bossX <= 0 or bossX >= 600:
                    boss_dir *= -1

            screen.blit(bossImg, (bossX + offset_x, bossY + offset_y))
            draw_boss_health()

            boss_fire_timer -= dt
            if boss_fire_timer <= 0:
                boss_bullets.append([bossX + 90, bossY + 120])
                boss_fire_timer = boss_fire_rate

            for bb in boss_bullets[:]:
                bb[1] += boss_bullet_speed * dt
                draw_glow_circle(screen, bb[0] + offset_x + 16, bb[1] + offset_y + 16, 8, (255, 60, 60))
                if is_player_collision(bb[0], bb[1], playerX, playerY):
                    if shield:
                        shield = False
                        shake_duration = 20
                        boss_bullets.remove(bb)
                    else:
                        game_over = True
                        shake_duration = 60
                        shake_magnitude = 20
                        mixer.music.stop()
                if bb[1] > 600:
                    boss_bullets.remove(bb)

            for b in bullets[:]:
                if is_collision(bossX + 100, bossY + 80, b[0], b[1]):
                    bullets.remove(b)
                    boss_health -= 1
                    boom_sound.play()
                    shake_duration = 10

            if boss_health <= 0:
                boss_active = False
                score_value += 10

        booster_timer += dt
        if booster_timer >= 30 and not booster_active:
            booster_active = True
            booster_timer = 0
            boosterY = -50
            boosterX = random.randint(50, 750)

        if booster_active:
            screen.blit(boosterImg, (boosterX + offset_x, boosterY + offset_y))
            boosterY += booster_speed * dt
            if boosterY > 600:
                booster_active = False
            if is_player_collision(boosterX, boosterY, playerX, playerY):
                booster_active = False
                shield = True
                shield_timer = 10

        if shield:
            shield_timer -= dt
            if shield_timer <= 0:
                shield = False

        player(playerX + offset_x, playerY + offset_y)
        show_score(textX, textY)
    else:
        game_over_text()

    fps = int(clock.get_fps())
    pygame.display.set_caption(f"Space Invader | FPS: {fps}")
    pygame.display.update


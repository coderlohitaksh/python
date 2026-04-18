import pygame, sys, random, math, os

pygame.init()
W, H = 1280, 720
s = pygame.display.set_mode((W, H))
pygame.display.set_caption("My first game screen")

clock = pygame.time.Clock()
font_big = pygame.font.SysFont("arial", 64)
font = pygame.font.SysFont("arial", 32)

BASE = os.path.dirname(__file__)
score_file = os.path.join(BASE, "highscore.txt")

def load_img(name, size=None, alpha=False):
    path = os.path.join(BASE, name)
    img = pygame.image.load(path)
    img = img.convert_alpha() if alpha else img.convert()
    if size:
        img = pygame.transform.scale(img, size)
    return img

def load_highscore():
    if not os.path.exists(score_file):
        return 0
    try:
        return int(open(score_file).read())
    except:
        return 0

def save_highscore(val):
    open(score_file, "w").write(str(val))

bg = load_img("space_bg.png", (W, H))
pimg = load_img("001-rocket.png", (110, 110), True)
limg = load_img("laser.png", (14, 40), True)

class Player:
    def __init__(self):
        self.x = W // 2
        self.y = H - 100
        self.speed = 320
        self.cooldown = 0
        self.power = "normal"
        self.power_time = 0

    def update(self, dt, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed * dt
        if keys[pygame.K_RIGHT]:
            self.x += self.speed * dt
        self.x = max(60, min(W - 60, self.x))
        self.cooldown -= dt
        if self.power_time > 0:
            self.power_time -= dt
        else:
            self.power = "normal"

    def draw(self, offset):
        r = pimg.get_rect(center=(self.x + offset[0], self.y + offset[1]))
        s.blit(pimg, r)
        return r

    def shoot(self):
        if self.cooldown > 0:
            return []
        self.cooldown = 0.3
        shots = []
        if self.power == "triple":
            shots.append(Laser(self.x - 25, self.y - 50, 0))
            shots.append(Laser(self.x, self.y - 50, 0))
            shots.append(Laser(self.x + 25, self.y - 50, 0))
        elif self.power == "spread":
            shots.append(Laser(self.x, self.y - 50, -0.5))
            shots.append(Laser(self.x, self.y - 50, 0))
            shots.append(Laser(self.x, self.y - 50, 0.5))
        else:
            shots.append(Laser(self.x, self.y - 50, 0))
        return shots

class Laser:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.speed = 450
        self.angle = angle

    def update(self, dt):
        self.y -= self.speed * dt
        self.x += self.angle * self.speed * dt

    def draw(self, offset):
        r = limg.get_rect(center=(self.x + offset[0], self.y + offset[1]))
        s.blit(limg, r)
        return r

    def offscreen(self):
        return self.y < -60 or self.x < -60 or self.x > W + 60

class PowerUp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choice(["triple", "spread"])
        self.vy = 150

    def update(self, dt):
        self.y += self.vy * dt

    def draw(self, offset):
        color = (0,255,255) if self.type == "triple" else (255,100,255)
        pygame.draw.circle(s, color, (int(self.x + offset[0]), int(self.y + offset[1])), 10)
        return pygame.Rect(self.x-10, self.y-10, 20, 20)

    def offscreen(self):
        return self.y > H + 50

class Asteroid:
    def __init__(self, difficulty):
        self.cx = random.randint(60, W - 60)
        self.cy = -60
        self.base_r = random.randint(20, 50)
        self.vy = random.randint(70, int(120 * difficulty))
        self.rot = random.random() * math.pi
        self.spin = random.uniform(-1.2, 1.2)
        self.points = self.make_shape()

    def make_shape(self):
        pts = []
        for i in range(10):
            ang = i * (2 * math.pi / 10)
            r = self.base_r + random.randint(-12, 12)
            pts.append([r * math.cos(ang), r * math.sin(ang)])
        return pts

    def update(self, dt):
        self.cy += self.vy * dt
        self.rot += self.spin * dt

    def get_points(self):
        pts = []
        for px, py in self.points:
            x = px * math.cos(self.rot) - py * math.sin(self.rot)
            y = px * math.sin(self.rot) + py * math.cos(self.rot)
            pts.append([self.cx + x, self.cy + y])
        return pts

    def draw(self, offset):
        pts = [[p[0] + offset[0], p[1] + offset[1]] for p in self.get_points()]
        pygame.draw.polygon(s, (140,140,140), pts)
        return self.get_rect()

    def get_rect(self):
        pts = self.get_points()
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        return pygame.Rect(min(xs), min(ys), max(xs)-min(xs), max(ys)-min(ys))

    def offscreen(self):
        return self.cy > H + 100

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-200,200)
        self.vy = random.uniform(-200,200)
        self.life = random.uniform(0.3,0.7)

    def update(self, dt):
        self.life -= dt
        self.x += self.vx * dt
        self.y += self.vy * dt

    def draw(self, offset):
        if self.life > 0:
            pygame.draw.circle(s, (255,200,80), (int(self.x+offset[0]), int(self.y+offset[1])), 2)

    def dead(self):
        return self.life <= 0

def reset_game():
    return Player(), [], [], [], [], 0, 0, 0

state = "menu"
difficulty = 1
highscore = load_highscore()

player, lasers, asteroids, particles, powerups, score, shake_time, shake_strength = reset_game()
spawn_timer = 0

while True:
    dt = min(clock.tick(60) / 1000, 0.05)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        if state == "menu" and e.type == pygame.KEYDOWN:
            if e.key == pygame.K_1: difficulty = 1; state = "game"; player, lasers, asteroids, particles, powerups, score, shake_time, shake_strength = reset_game()
            if e.key == pygame.K_2: difficulty = 2; state = "game"; player, lasers, asteroids, particles, powerups, score, shake_time, shake_strength = reset_game()
            if e.key == pygame.K_3: difficulty = 3; state = "game"; player, lasers, asteroids, particles, powerups, score, shake_time, shake_strength = reset_game()

        elif state == "game":
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()
                if e.key == pygame.K_SPACE:
                    lasers.extend(player.shoot())

        elif state == "gameover" and e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r:
                state = "menu"

    s.blit(bg, (0,0))

    if state == "menu":
        s.blit(font_big.render("SPACE SHOOTER", True, (255,255,255)), (W//2-250, H//2-80))
        s.blit(font.render("1 Easy  2 Medium  3 Hard", True, (200,200,200)), (W//2-180, H//2))

    elif state == "game":
        keys = pygame.key.get_pressed()
        player.update(dt, keys)

        for l in lasers: l.update(dt)
        lasers = [l for l in lasers if not l.offscreen()]

        spawn_timer += dt
        if spawn_timer > max(0.5, 1.2 - difficulty * 0.3):
            asteroids.append(Asteroid(difficulty))
            spawn_timer = 0

        for a in asteroids: a.update(dt)
        asteroids = [a for a in asteroids if not a.offscreen()]

        for p in particles: p.update(dt)
        particles = [p for p in particles if not p.dead()]

        for pu in powerups: pu.update(dt)
        powerups = [pu for pu in powerups if not pu.offscreen()]

        if shake_time > 0: shake_time -= dt
        offset = (random.randint(-8,8), random.randint(-8,8)) if shake_time > 0 else (0,0)

        s.blit(bg, offset)
        player_rect = player.draw(offset)

        laser_rects = [(l, l.draw(offset)) for l in lasers]
        asteroid_rects = [(a, a.draw(offset)) for a in asteroids]

        for a, r in asteroid_rects:
            if r.colliderect(player_rect):
                if score > highscore: save_highscore(score)
                state = "gameover"

        for l, lr in laser_rects:
            for a, ar in asteroid_rects:
                if ar.colliderect(lr):
                    if a in asteroids:
                        asteroids.remove(a)
                        score += 10
                        shake_time = 0.2
                        for _ in range(20):
                            particles.append(Particle(a.cx, a.cy))
                        if random.random() < 0.25:
                            powerups.append(PowerUp(a.cx, a.cy))
                    if l in lasers: lasers.remove(l)
                    break

        for pu in powerups:
            rect = pu.draw(offset)
            if rect.colliderect(player_rect):
                player.power = pu.type
                player.power_time = 5
                powerups.remove(pu)

        for p in particles: p.draw(offset)

        s.blit(font.render(f"Score: {score}", True, (255,255,255)), (20,20))

    elif state == "gameover":
        s.blit(font_big.render("GAME OVER", True, (255,100,100)), (W//2-200, H//2-100))
        s.blit(font.render(f"Score: {score}", True, (255,255,255)), (W//2-80, H//2))
        s.blit(font.render(f"High Score: {max(score, highscore)}", True, (255,255,0)), (W//2-120, H//2+40))
        s.blit(font.render("Press R to Restart", True, (200,200,200)), (W//2-140, H//2+100))

    pygame.display.flip()
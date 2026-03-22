import os
import random
import keyboard
import time
from colorama import Fore, init

init(autoreset=True)

# ========================
# Game settings
# ========================
world_size = 50
view = 10

player = [1, 1]
goal = [48, 48]
health = 10
score = 0
inventory = []

# ========================
# Symbols / emojis
# ========================
PLAYER_ICON = "🧑"
GOAL_ICON = "🏁"
WALL_ICON = "🧱"
GEM_ICON = "💎"
EMPTY_ICON = "⬛"
FOG_ICON = "🌫️"

WEAPON_ICON = "🗡️"

# ========================
# Generate world
# ========================
walls = set()
gems = set()
weapons = set()
enemies = []

for _ in range(300):
    walls.add((random.randint(0, world_size-1), random.randint(0, world_size-1)))

for _ in range(40):
    gems.add((random.randint(0, world_size-1), random.randint(0, world_size-1)))

for _ in range(10):
    weapons.add((random.randint(0, world_size-1), random.randint(0, world_size-1)))

# Regular enemies
for _ in range(6):
    enemies.append({
        "pos":[random.randint(0, world_size-1), random.randint(0, world_size-1)],
        "mode":"patrol",
        "type":"👾",
        "damage":1
    })

# Boss enemy
boss = {
    "pos":[random.randint(0, world_size-1), random.randint(0, world_size-1)],
    "mode":"patrol",
    "type":"🐉",
    "damage":3,
    "health": 10
}
enemies.append(boss)

# ========================
# Utility functions
# ========================
def clear():
    os.system("cls" if os.name=="nt" else "clear")

def draw():
    clear()
    start_x = max(0, player[0]-view//2)
    start_y = max(0, player[1]-view//2)
    end_x = min(world_size, start_x + view)
    end_y = min(world_size, start_y + view)

    print(Fore.CYAN + f"Score: {score}  Health: {health}  Inventory: {' '.join(inventory)}\n")

    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            # Fog of war
            if abs(x-player[0]) > view//2 or abs(y-player[1]) > view//2:
                print(FOG_ICON, end=" ")
                continue

            pos = (x,y)
            if [x,y] == player:
                print(PLAYER_ICON, end=" ")
            elif [x,y] == goal:
                print(GOAL_ICON, end=" ")
            elif pos in walls:
                print(WALL_ICON, end=" ")
            elif pos in gems:
                print(GEM_ICON, end=" ")
            elif pos in weapons:
                print(WEAPON_ICON, end=" ")
            elif any(e["pos"]==[x,y] for e in enemies):
                e = [e for e in enemies if e["pos"]==[x,y]][0]
                print(e["type"], end=" ")
            else:
                print(EMPTY_ICON, end=" ")
        print()

def move(dx, dy):
    nx, ny = player[0]+dx, player[1]+dy
    if 0<=nx<world_size and 0<=ny<world_size and (nx,ny) not in walls:
        player[0], player[1] = nx, ny

def move_enemies():
    for e in enemies:
        ex, ey = e["pos"]
        dist = abs(player[0]-ex) + abs(player[1]-ey)
        e["mode"] = "chase" if dist < 8 else "patrol"

        if e["mode"]=="chase":
            dx = 1 if ex<player[0] else -1 if ex>player[0] else 0
            dy = 1 if ey<player[1] else -1 if ey>player[1] else 0
        else:
            dx, dy = random.choice([-1,0,1]), random.choice([-1,0,1])

        nx, ny = ex+dx, ey+dy
        if 0<=nx<world_size and 0<=ny<world_size and (nx,ny) not in walls:
            e["pos"] = [nx, ny]

# ========================
# Game loop
# ========================
while True:
    draw()

    # Check win
    if player == goal:
        print(Fore.GREEN + "\n🏆 You reached the goal! Victory! 🏆")
        break

    # Check game over
    if health <= 0:
        print(Fore.RED + "\n💀 Game Over! 💀")
        break

    # Collect gems
    if tuple(player) in gems:
        gems.remove(tuple(player))
        inventory.append("💎")
        score += 10

    # Collect weapons
    if tuple(player) in weapons:
        weapons.remove(tuple(player))
        inventory.append("🗡️")
        score += 5

    # Enemy encounters
    for e in enemies[:]:
        if e["pos"] == player:
            if "🗡️" in inventory:
                # Attack with weapon
                if "🗡️" in inventory:
                    e["health"] = e.get("health",1) -1
                    print(Fore.GREEN + f"\nYou hit {e['type']} with a sword!")
                    inventory.remove("🗡️")
                    if e.get("health",1) <=0:
                        enemies.remove(e)
                        score += 20
                        print(Fore.YELLOW + f"{e['type']} defeated!")
            else:
                health -= e["damage"]
                print(Fore.RED + f"\nOuch! {e['type']} hit you for {e['damage']} damage!")

    key = keyboard.read_key()
    if key in ["w","up"]: move(0,-1)
    elif key in ["s","down"]: move(0,1)
    elif key in ["a","left"]: move(-1,0)
    elif key in ["d","right"]: move(1,0)
    elif key=="space": # optional attack
        for e in enemies:
            if abs(e["pos"][0]-player[0])<=1 and abs(e["pos"][1]-player[1])<=1:
                e["health"] = e.get("health",1)-1
                print(Fore.GREEN + f"\nYou swing at {e['type']}!")
                if e.get("health",1)<=0:
                    enemies.remove(e)
                    score += 20
                    print(Fore.YELLOW + f"{e['type']} defeated!")

    move_enemies()
    time.sleep(0.05)
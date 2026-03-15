import os
import random
import time
from colorama import Fore, init

init(autoreset=True)

def clear():
    os.system("cls" if os.name=="nt" else "clear")

def title():
    print(Fore.YELLOW + r"""
 ██████╗ ██╗██████╗ ██████╗     ██████╗ ██████╗  █████╗ ██╗    ██╗██╗
 ██╔══██╗██║██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗██║    ██║██║
 ██████╔╝██║██████╔╝██║  ██║    ██████╔╝██████╔╝███████║██║ █╗ ██║██║
 ██╔═══╝ ██║██╔══██╗██║  ██║    ██╔══██╗██╔══██╗██╔══██║██║███╗██║██║
 ██║     ██║██║  ██║██████╔╝    ██████╔╝██║  ██║██║  ██║╚███╔███╔╝███████╗
 ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝
""")

def bar(value,max_value):
    size=20
    filled=int((value/max_value)*size)
    return "█"*filled+"-"*(size-filled)

class Brawler:

    def __init__(self,name,hp,attack,super_name):
        self.name=name
        self.max_hp=hp
        self.hp=hp
        self.attack=attack
        self.super=0
        self.super_name=super_name
        self.trophies=0
        self.level=1
        self.xp=0

    def show(self):
        print(Fore.CYAN+f"🐦 {self.name}  LVL {self.level}")
        print("❤️ HP :",bar(self.hp,self.max_hp),self.hp)
        print("⚡ SP :",bar(self.super,100),self.super,"%")
        print("🏆 TR :",self.trophies)
        print("-"*30)

    def attack_enemy(self,enemy):
        crit=False
        if random.random()<0.2:
            dmg=random.randint(self.attack+5,self.attack+10)
            crit=True
        else:
            dmg=random.randint(self.attack-3,self.attack+3)

        enemy.hp-=dmg
        self.super=min(100,self.super+25)

        if crit:
            print(Fore.RED+f"💥 CRITICAL HIT! {self.name} deals {dmg}")
        else:
            print(Fore.YELLOW+f"⚔ {self.name} hits for {dmg}")

    def use_super(self,enemy):
        if self.super<100:
            print(Fore.RED+"⚡ Super not ready")
            return

        dmg=self.attack*2+random.randint(8,14)
        enemy.hp-=dmg
        self.super=0

        print(Fore.MAGENTA+f"🔥 {self.name} uses {self.super_name}")
        print(Fore.MAGENTA+f"💥 Damage {dmg}")

class Phoenix(Brawler):
    def __init__(self):
        super().__init__("Phoenix",140,18,"Flame Storm")

class Falcon(Brawler):
    def __init__(self):
        super().__init__("Falcon",120,22,"Sky Dive")

class Owl(Brawler):
    def __init__(self):
        super().__init__("Owl",150,16,"Night Blast")

class Eagle(Brawler):
    def __init__(self):
        super().__init__("Eagle",160,17,"Storm Strike")

class Raven(Brawler):
    def __init__(self):
        super().__init__("Raven",130,20,"Shadow Swarm")

class Parrot(Brawler):
    def __init__(self):
        super().__init__("Parrot",110,23,"Echo Shot")

def enemy():
    e=random.choice([Phoenix(),Falcon(),Owl(),Eagle(),Raven(),Parrot()])
    e.name="Enemy "+e.name
    return e

def gain_xp(player,amount):
    player.xp+=amount
    if player.xp>=20:
        player.level+=1
        player.xp=0
        player.max_hp+=10
        player.attack+=2
        print(Fore.GREEN+"⭐ LEVEL UP")
        time.sleep(1)

def star_drop(player):
    reward=random.choice(["coins","trophies","power"])
    if reward=="coins":
        coins=random.randint(10,30)
        print(Fore.YELLOW+"🌟 Star Drop Coins",coins)
    elif reward=="trophies":
        t=random.randint(4,8)
        player.trophies+=t
        print(Fore.CYAN+"🌟 Star Drop",t,"Trophies")
    else:
        player.attack+=2
        print(Fore.GREEN+"🌟 Power Boost +2 Attack")

def battle(player):

    enemy_brawler=enemy()

    while player.hp>0 and enemy_brawler.hp>0:

        clear()
        print(Fore.YELLOW+"⚔ BATTLE ARENA\n")

        print("PLAYER")
        player.show()

        print("ENEMY")
        enemy_brawler.show()

        print("1 Attack")
        print("2 Super")

        choice=input("> ")

        if choice=="1":
            player.attack_enemy(enemy_brawler)
        elif choice=="2":
            player.use_super(enemy_brawler)

        time.sleep(1)

        if enemy_brawler.hp<=0:
            break

        if enemy_brawler.super>=100 and random.random()<0.5:

            dmg=enemy_brawler.attack*2
            player.hp-=dmg
            enemy_brawler.super=0

            print(Fore.RED+f"🔥 Enemy used SUPER for {dmg}")

        else:

            enemy_damage=random.randint(enemy_brawler.attack-3,enemy_brawler.attack+3)

            player.hp-=enemy_damage
            enemy_brawler.super=min(100,enemy_brawler.super+20)

            print(Fore.RED+f"💥 Enemy hits {enemy_damage}")

        time.sleep(1)

    if player.hp>0:
        print(Fore.GREEN+"🏆 VICTORY")
        player.trophies+=8
        gain_xp(player,10)
        star_drop(player)
    else:
        print(Fore.RED+"☠ DEFEAT")
        player.trophies=max(0,player.trophies-5)

    player.hp=player.max_hp
    input("Press Enter")

def gem_grab(player):

    gems=0

    while gems<10:

        clear()

        print(Fore.MAGENTA+"💎 GEM GRAB")
        print("Gems:",gems)

        player.show()

        print("1 Fight enemy")
        print("2 Search gem")

        choice=input("> ")

        if choice=="1":
            battle(player)
            gems+=random.randint(1,3)

        else:
            if random.random()<0.5:
                g=random.randint(1,3)
                gems+=g
                print("Found",g,"gems")
            else:
                print("No gems found")

        time.sleep(1)

    print("Gem Grab Victory")
    player.trophies+=12
    input("Press Enter")

def showdown(player):

    enemies=4

    while enemies>0 and player.hp>0:

        clear()

        print(Fore.RED+"🔥 SHOWDOWN")
        print("Enemies left:",enemies)

        player.show()

        input("Press Enter to fight")

        battle(player)

        enemies-=1

    if player.hp>0:
        print("Showdown Winner")
        player.trophies+=15

    input("Press Enter")

def shop(player):

    coins=random.randint(40,80)

    while True:

        clear()

        print(Fore.YELLOW+"🛒 SHOP")
        print("Coins:",coins)
        print()

        print("1 +5 Attack (30 coins)")
        print("2 +20 Max HP (40 coins)")
        print("3 Exit")

        choice=input("> ")

        if choice=="1" and coins>=30:
            player.attack+=5
            coins-=30
            print("Attack upgraded")

        elif choice=="2" and coins>=40:
            player.max_hp+=20
            coins-=40
            print("HP upgraded")

        elif choice=="3":
            break

        else:
            print("Not enough coins")

        time.sleep(1)

def choose():

    clear()

    print("Choose Brawler\n")

    print("1 Phoenix")
    print("2 Falcon")
    print("3 Owl")
    print("4 Eagle")
    print("5 Raven")
    print("6 Parrot")

    choice=input("> ")

    if choice=="1":
        return Phoenix()

    if choice=="2":
        return Falcon()

    if choice=="3":
        return Owl()

    if choice=="4":
        return Eagle()

    if choice=="5":
        return Raven()

    return Parrot()

def game():

    player=choose()

    while True:

        clear()
        title()

        player.show()

        print(Fore.CYAN+"="*35)
        print("⚔ 1 Arena Battle")
        print("💎 2 Gem Grab")
        print("🔥 3 Showdown")
        print("🛒 4 Shop")
        print("🚪 5 Exit")
        print(Fore.CYAN+"="*35)

        choice=input("> ")

        if choice=="1":
            battle(player)

        elif choice=="2":
            gem_grab(player)

        elif choice=="3":
            showdown(player)

        elif choice=="4":
            shop(player)

        elif choice=="5":
            break

game()
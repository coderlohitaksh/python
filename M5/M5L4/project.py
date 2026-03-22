from colorama import Fore, Style, init
import time
import os
import sys

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def type_text(text, speed=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def cinematic_title():

    clear()

    title_lines = [
"██████╗ ███████╗██╗   ██╗███████╗██████╗ ███████╗██████╗ ",
"██╔══██╗██╔════╝██║   ██║██╔════╝██╔══██╗██╔════╝██╔══██╗",
"██████╔╝█████╗  ██║   ██║█████╗  ██████╔╝███████╗█████╗  ",
"██╔══██╗██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝  ",
"██║  ██║███████╗ ╚████╔╝ ███████╗██║  ██║███████║███████╗",
"╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝"
]

    print(Fore.BLUE)

    for line in title_lines:
        print(line)
        time.sleep(0.25)

    print(Fore.YELLOW)
    time.sleep(0.5)
    type_text("\n             REVERSER WORDS\n",0.04)

def loading():

    print(Fore.CYAN)
    type_text("Launching system...\n",0.03)

    for i in range(30):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(0.04)

    print("\n")

class Reverse:

    def __init__(self,s=""):
        self.s=s

    def set_string(self,s):
        self.s=s

    def reverse(self):
        r=""
        i=len(self.s)-1
        while i>=0:
            r=r+self.s[i]
            i=i-1
        return r

    def length(self):
        count=0
        for _ in self.s:
            count=count+1
        return count

    def upper(self):
        r=""
        for c in self.s:
            r=r+c.upper()
        return r

    def lower(self):
        r=""
        for c in self.s:
            r=r+c.lower()
        return r

    def vowels(self):
        v="aeiouAEIOU"
        count=0
        for c in self.s:
            if c in v:
                count=count+1
        return count

    def consonants(self):
        v="aeiouAEIOU"
        count=0
        for c in self.s:
            if c.isalpha() and c not in v:
                count=count+1
        return count

    def palindrome(self):
        return self.reverse()==self.s

def menu():

    print(Fore.GREEN)
    print("\n========== MENU ==========")
    print("1  Reverse Word")
    print("2  Length")
    print("3  Uppercase")
    print("4  Lowercase")
    print("5  Count Vowels")
    print("6  Count Consonants")
    print("7  Check Palindrome")
    print("8  Enter New Word")
    print("0  Exit")
    print("==========================")

def main():

    cinematic_title()
    loading()

    word=input(Fore.CYAN+"Enter a word: ")
    obj=Reverse(word)

    while True:

        menu()

        choice=input(Fore.YELLOW+"Choose option: ")

        if choice=="1":
            type_text(Fore.MAGENTA+"Reversed: "+obj.reverse())

        elif choice=="2":
            type_text(Fore.MAGENTA+"Length: "+str(obj.length()))

        elif choice=="3":
            type_text(Fore.MAGENTA+obj.upper())

        elif choice=="4":
            type_text(Fore.MAGENTA+obj.lower())

        elif choice=="5":
            type_text(Fore.MAGENTA+"Vowels: "+str(obj.vowels()))

        elif choice=="6":
            type_text(Fore.MAGENTA+"Consonants: "+str(obj.consonants()))

        elif choice=="7":
            type_text(Fore.MAGENTA+"Palindrome: "+str(obj.palindrome()))

        elif choice=="8":
            word=input(Fore.CYAN+"Enter new word: ")
            obj.set_string(word)

        elif choice=="0":
            type_text(Fore.RED+"Closing program...",0.04)
            break

        else:
            type_text(Fore.RED+"Invalid option")

if __name__=="__main__":
    main()
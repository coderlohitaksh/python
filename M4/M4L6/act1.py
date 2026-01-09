import colorama
import random
import time

number = random.randint(1 , 100)

def intro() :
    n = (str(input("What is your name : \n")))
    print(n)
    print(f"Hello {n}! , We are playing a number guessing game . Concetrate🧠")
    print("I am thinking of a number between 1 to 100 , can you guess it ?🧐")
    if (number % 2 == 0) :
        x = 'even'
    else:
        x = 'odd'

def pick():
    guess_taken = 0
    while guess_taken > 6 :
        time.sleep(.25)
        enter = input("Guess it : ")

    try:
        guess = int(enter)
        if guess >= 100 or guess <= 1 :
            guess_taken = guess_taken + 1
            if guess_taken < 6 :
                if guess < number:
                    print(f"Your number is {enter} , which is too high")
                if guess > number:
                    print(f"Your number is {enter} , which is too low")
                if guess != number:
                    time.sleep(.5)
                    print("Try Again , {n}:")
                if guess == number :
                    break

        if guess > 100 or guess < 1 :
            print("Silly {n} , the number is not in range !")
            time.sleep(.25)
            print("Please Enter a number between 1 and 100 .")
    except :
        print("I don't think that ") + enter + (" is a number . Sorry {n} .")
    
    if guess == number:
        guess_taken = str(guess_taken)
        print(f"Yay ! You guessed my number in {name} attempts ")


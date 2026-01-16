import random
import os
import time

RED="\033[91m"
BLUE="\033[94m"
GREEN="\033[92m"
YELLOW="\033[93m"
BOLD="\033[1m"
RESET="\033[0m"

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def print_score(score):
    print(f"{BOLD}{GREEN}Score: X={score['X']}  O={score['O']}  Draws={score['Draw']}{RESET}\n")

def print_board(board,last_move=None,winner_line=[]):
    display=[]
    for i,c in enumerate(board):
        char=c
        if c=="X": char=f"{RED}X{RESET}"
        elif c=="O": char=f"{BLUE}O{RESET}"
        if i in winner_line: char=f"{BOLD}{GREEN}{c}{RESET}"
        if last_move==i: char=f"{BOLD}{YELLOW}{c}{RESET}"
        display.append(char)
    print("\n")
    print(f" {display[0]} | {display[1]} | {display[2]} ")
    print("---+---+---")
    print(f" {display[3]} | {display[4]} | {display[5]} ")
    print("---+---+---")
    print(f" {display[6]} | {display[7]} | {display[8]} ")
    print("\n")

def check_winner(board,p):
    combos=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for c in combos:
        if all(board[i]==p for i in c): return c
    return []

def check_draw(board):
    return all(c in ["X","O"] for c in board)

def player_move(board,p):
    while True:
        move=input(f"Player {p}, enter position (1-9): ")
        if not move.isdigit(): continue
        move=int(move)-1
        if move<0 or move>8: continue
        if board[move] in ["X","O"]: continue
        board[move]=p
        return move

def ai_move(board):
    if random.random()<0.3:
        empty=[i for i,v in enumerate(board) if v not in ["X","O"]]
        move=random.choice(empty)
        board[move]="O"
        return move
    for i in range(9):
        if board[i] not in ["X","O"]:
            board[i]="O"
            if check_winner(board,"O"): return i
            board[i]=str(i+1)
    for i in range(9):
        if board[i] not in ["X","O"]:
            board[i]="X"
            if check_winner(board,"X"):
                board[i]="O"
                return i
            board[i]=str(i+1)
    empty=[i for i,v in enumerate(board) if v not in ["X","O"]]
    move=random.choice(empty)
    board[move]="O"
    return move

def switch_player(p):
    return "O" if p=="X" else "X"

def animate_move(board,last_move):
    for _ in range(3):
        clear_screen()
        print_board(board,last_move)
        time.sleep(0.2)
        clear_screen()
        print_board(board)
        time.sleep(0.2)

def play_game(mode,score):
    board=[str(i+1) for i in range(9)]
    current="X"
    last_move=None
    winner_line=[]
    while True:
        clear_screen()
        print_score(score)
        print_board(board,last_move,winner_line)
        time.sleep(0.2)
        if mode=="1" and current=="O":
            print(f"{BOLD}{BLUE}AI is thinking...{RESET}")
            time.sleep(0.5)
            last_move=ai_move(board)
            animate_move(board,last_move)
        else:
            last_move=player_move(board,current)
            animate_move(board,last_move)
        winner_line=check_winner(board,current)
        if winner_line:
            clear_screen()
            score[current]+=1
            print_score(score)
            print_board(board,last_move,winner_line)
            print(f"{BOLD}{GREEN}Player {current} wins!{RESET}")
            break
        if check_draw(board):
            clear_screen()
            score["Draw"]+=1
            print_score(score)
            print_board(board,last_move)
            print(f"{BOLD}{YELLOW}It's a draw!{RESET}")
            break 
        current=switch_player(current)

def main():
    score={"X" : 0 , "O" : 0,"Draw" : 0}

    clear_screen()

    print(f"{BOLD}{GREEN}Welcome to Tic Tac Toe Mini-GUI!{RESET}")
    print("Follow the steps below to enjoy the game:\n")
    print(f"{BOLD}Step 1:{RESET} Scores are initialized to zero. Let's see who will win!")
    
    while True:
        print(f"\n{BOLD}Step 2:{RESET} Select your game mode before starting.")
        mode=""
        while mode not in ["1","2"]:
            print("1 - Single Player (Play against AI)")
            print("2 - Two Player (Play with a friend)")
            mode=input("Enter your choice (1 or 2): ").strip()
            if mode not in ["1","2"]:
                print(f"{BOLD}{RED}Invalid input! Please select 1 or 2.{RESET}")
        play_game(mode,score)
        print(f"\n{BOLD}Step 5:{RESET} Would you like to play another round?")
        again=input("Play again? (y/n): ").lower().strip()
        
        if again!="y": break
        else:
            clear_screen()
            print(f"{BOLD}{GREEN}Great! Let's start a new game!{RESET}\n")
    clear_screen()
    print(f"{BOLD}{BLUE}Final Score:{RESET}")
    print_score(score)
    print(f"{BOLD}{GREEN}Thanks for playing Tic Tac Toe Mini-GUI! Come back soon!{RESET}")

if __name__=="__main__":
    main()

import pygame
import sys
import copy
import random

pygame.init()

SQUARE = 80
BOARD_SIZE = 8
WIDTH = SQUARE * BOARD_SIZE
HEIGHT = WIDTH
UI_WIDTH = 260

SCREEN = pygame.display.set_mode((WIDTH + UI_WIDTH, HEIGHT))
pygame.display.set_caption("Python Chess AI")

CLOCK = pygame.time.Clock()
FPS = 60

LIGHT = (240,217,181)
DARK = (181,136,99)
GREEN = (50,200,50)
YELLOW = (255,255,0)
BLACK = (25,25,25)
WHITE = (255,255,255)

FONT = pygame.font.SysFont("arial",22)
BIG = pygame.font.SysFont("arial",36)

PIECE_SIZE = int(SQUARE * 0.82)

board = []
turn = "white"
selected = None
legal_moves = []
winner = None
mode = None

en_passant = None

history = []

AI_LEVEL = 3

pieces = {}

piece_values = {
    "pawn":100,
    "knight":320,
    "bishop":330,
    "rook":500,
    "queen":900,
    "king":20000
}

pawn_table = [
[0,0,0,0,0,0,0,0],
[50,50,50,50,50,50,50,50],
[10,10,20,30,30,20,10,10],
[5,5,10,25,25,10,5,5],
[0,0,0,20,20,0,0,0],
[5,-5,-10,0,0,-10,-5,5],
[5,10,10,-20,-20,10,10,5],
[0,0,0,0,0,0,0,0]
]

knight_table = [
[-50,-40,-30,-30,-30,-30,-40,-50],
[-40,-20,0,0,0,0,-20,-40],
[-30,0,10,15,15,10,0,-30],
[-30,5,15,20,20,15,5,-30],
[-30,0,15,20,20,15,0,-30],
[-30,5,10,15,15,10,5,-30],
[-40,-20,0,5,5,0,-20,-40],
[-50,-40,-30,-30,-30,-30,-40,-50]
]

bishop_table = [
[-20,-10,-10,-10,-10,-10,-10,-20],
[-10,0,0,0,0,0,0,-10],
[-10,0,5,10,10,5,0,-10],
[-10,5,5,10,10,5,5,-10],
[-10,0,10,10,10,10,0,-10],
[-10,10,10,10,10,10,10,-10],
[-10,5,0,0,0,0,5,-10],
[-20,-10,-10,-10,-10,-10,-10,-20]
]

rook_table = [
[0,0,0,0,0,0,0,0],
[5,10,10,10,10,10,10,5],
[-5,0,0,0,0,0,0,-5],
[-5,0,0,0,0,0,0,-5],
[-5,0,0,0,0,0,0,-5],
[-5,0,0,0,0,0,0,-5],
[-5,0,0,0,0,0,0,-5],
[0,0,0,5,5,0,0,0]
]

queen_table = [
[-20,-10,-10,-5,-5,-10,-10,-20],
[-10,0,0,0,0,0,0,-10],
[-10,0,5,5,5,5,0,-10],
[-5,0,5,5,5,5,0,-5],
[0,0,5,5,5,5,0,-5],
[-10,5,5,5,5,5,0,-10],
[-10,0,5,0,0,0,0,-10],
[-20,-10,-10,-5,-5,-10,-10,-20]
]

king_table = [
[-30,-40,-40,-50,-50,-40,-40,-30],
[-30,-40,-40,-50,-50,-40,-40,-30],
[-30,-40,-40,-50,-50,-40,-40,-30],
[-30,-40,-40,-50,-50,-40,-40,-30],
[-20,-30,-30,-40,-40,-30,-30,-20],
[-10,-20,-20,-20,-20,-20,-20,-10],
[20,20,0,0,0,0,20,20],
[20,30,10,0,0,10,30,20]
]

castle_rights = {
    "white":{"K":True,"Q":True},
    "black":{"K":True,"Q":True}
}

def load_pieces():

    names = [
        "pawn",
        "rook",
        "knight",
        "bishop",
        "queen",
        "king"
    ]

    colors = ["white","black"]

    for color in colors:
        for name in names:

            img = pygame.image.load(
                f"{color} {name}.png"
            )

            img = pygame.transform.smoothscale(
                img,
                (PIECE_SIZE,PIECE_SIZE)
            )

            pieces[f"{color}_{name}"] = img

def reset_board():

    global board
    global turn
    global winner
    global en_passant

    board = [

        ["black_rook",
         "black_knight",
         "black_bishop",
         "black_queen",
         "black_king",
         "black_bishop",
         "black_knight",
         "black_rook"],

        ["black_pawn"] * 8,

        [None]*8,
        [None]*8,
        [None]*8,
        [None]*8,

        ["white_pawn"] * 8,

        ["white_rook",
         "white_knight",
         "white_bishop",
         "white_queen",
         "white_king",
         "white_bishop",
         "white_knight",
         "white_rook"]
    ]

    turn = "white"
    winner = None
    en_passant = None

def inside(r,c):
    return 0 <= r < 8 and 0 <= c < 8

def enemy(color):
    if color == "white":
        return "black"
    return "white"

def king_pos(color):

    for r in range(8):
        for c in range(8):

            if board[r][c] == f"{color}_king":
                return r,c

    return None
def pawn_moves(r,c,color):

    moves = []

    direction = -1 if color=="white" else 1

    if inside(r+direction,c):
        if board[r+direction][c] is None:
            moves.append((r+direction,c))

            start_row = 6 if color=="white" else 1

            if r == start_row:

                if board[r+2*direction][c] is None:
                    moves.append((r+2*direction,c))

    for dc in (-1,1):

        nr = r + direction
        nc = c + dc

        if inside(nr,nc):

            if board[nr][nc]:
                if board[nr][nc].startswith(enemy(color)):
                    moves.append((nr,nc))

    if en_passant:

        ep_r,ep_c = en_passant

        if abs(ep_c-c)==1 and ep_r==r+direction:
            moves.append((ep_r,ep_c))

    return moves


def knight_moves(r,c,color):

    moves = []

    jumps = [
        (2,1),(2,-1),
        (-2,1),(-2,-1),
        (1,2),(1,-2),
        (-1,2),(-1,-2)
    ]

    for dr,dc in jumps:

        nr = r + dr
        nc = c + dc

        if inside(nr,nc):

            if board[nr][nc] is None:
                moves.append((nr,nc))

            elif board[nr][nc].startswith(enemy(color)):
                moves.append((nr,nc))

    return moves


def sliding_moves(r,c,color,directions):

    moves = []

    for dr,dc in directions:

        nr = r + dr
        nc = c + dc

        while inside(nr,nc):

            if board[nr][nc] is None:

                moves.append((nr,nc))

            else:

                if board[nr][nc].startswith(enemy(color)):
                    moves.append((nr,nc))

                break

            nr += dr
            nc += dc

    return moves


def bishop_moves(r,c,color):

    return sliding_moves(
        r,c,color,
        [
            (1,1),
            (1,-1),
            (-1,1),
            (-1,-1)
        ]
    )


def rook_moves(r,c,color):

    return sliding_moves(
        r,c,color,
        [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
    )


def queen_moves(r,c,color):

    return sliding_moves(
        r,c,color,
        [
            (1,1),
            (1,-1),
            (-1,1),
            (-1,-1),
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
    )


def king_moves(r,c,color):

    moves = []

    for dr in (-1,0,1):

        for dc in (-1,0,1):

            if dr == 0 and dc == 0:
                continue

            nr = r + dr
            nc = c + dc

            if inside(nr,nc):

                if board[nr][nc] is None:
                    moves.append((nr,nc))

                elif board[nr][nc].startswith(enemy(color)):
                    moves.append((nr,nc))

    if color=="white":

        if castle_rights["white"]["K"]:

            if board[7][5] is None and board[7][6] is None:

                moves.append((7,6))

        if castle_rights["white"]["Q"]:

            if (
                board[7][1] is None and
                board[7][2] is None and
                board[7][3] is None
            ):

                moves.append((7,2))

    else:

        if castle_rights["black"]["K"]:

            if board[0][5] is None and board[0][6] is None:

                moves.append((0,6))

        if castle_rights["black"]["Q"]:

            if (
                board[0][1] is None and
                board[0][2] is None and
                board[0][3] is None
            ):

                moves.append((0,2))

    return moves


def raw_moves(r,c):

    piece = board[r][c]

    if piece is None:
        return []

    color,kind = piece.split("_")

    if kind=="pawn":
        return pawn_moves(r,c,color)

    if kind=="knight":
        return knight_moves(r,c,color)

    if kind=="bishop":
        return bishop_moves(r,c,color)

    if kind=="rook":
        return rook_moves(r,c,color)

    if kind=="queen":
        return queen_moves(r,c,color)

    if kind=="king":
        return king_moves(r,c,color)

    return []


def square_attacked(r,c,color):

    opponent = enemy(color)

    for rr in range(8):

        for cc in range(8):

            piece = board[rr][cc]

            if piece:

                if piece.startswith(opponent):

                    for mr,mc in raw_moves(rr,cc):

                        if mr==r and mc==c:
                            return True

    return False


def in_check(color):

    king = king_pos(color)

    if king is None:
        return False

    kr,kc = king

    return square_attacked(
        kr,
        kc,
        color
    )


def legal_moves_for(r,c):

    piece = board[r][c]

    if piece is None:
        return []

    color = piece.split("_")[0]

    legal = []

    for mr,mc in raw_moves(r,c):

        save_board = copy.deepcopy(board)

        board[mr][mc] = board[r][c]
        board[r][c] = None

        if not in_check(color):
            legal.append((mr,mc))

        board[:] = save_board

    return legal


def all_moves(color):

    moves = []

    for r in range(8):

        for c in range(8):

            piece = board[r][c]

            if piece:

                if piece.startswith(color):

                    for mr,mc in legal_moves_for(r,c):

                        moves.append(
                            (
                                r,
                                c,
                                mr,
                                mc
                            )
                        )

    random.shuffle(moves)

    return moves
def evaluate():

    score = 0

    for r in range(8):

        for c in range(8):

            piece = board[r][c]

            if piece is None:
                continue

            color,kind = piece.split("_")

            value = piece_values[kind]

            if kind == "pawn":
                value += pawn_table[r][c]

            elif kind == "knight":
                value += knight_table[r][c]

            elif kind == "bishop":
                value += bishop_table[r][c]

            elif kind == "rook":
                value += rook_table[r][c]

            elif kind == "queen":
                value += queen_table[r][c]

            elif kind == "king":
                value += king_table[r][c]

            if color == "white":
                score += value
            else:
                score -= value

    return score


def game_over():

    moves = all_moves(turn)

    if len(moves) > 0:
        return False

    return True


def check_result():

    global winner

    moves = all_moves(turn)

    if moves:
        return

    if in_check(turn):

        if turn == "white":
            winner = "Black Wins"

        else:
            winner = "White Wins"

    else:

        winner = "Stalemate"


def minimax(depth, alpha, beta, maximizing):

    if depth == 0:
        return evaluate(), None

    color = "white" if maximizing else "black"

    moves = all_moves(color)

    if not moves:
        return evaluate(), None

    best_move = None

    if maximizing:

        best_score = -99999999

        for sr,sc,tr,tc in moves:

            save_board = copy.deepcopy(board)
            save_turn = turn
            save_ep = en_passant

            make_move(sr,sc,tr,tc,False)

            score,_ = minimax(
                depth-1,
                alpha,
                beta,
                False
            )

            board[:] = save_board

            globals()["turn"] = save_turn
            globals()["en_passant"] = save_ep

            if score > best_score:

                best_score = score
                best_move = (
                    sr,
                    sc,
                    tr,
                    tc
                )

            alpha = max(alpha,score)

            if beta <= alpha:
                break

        return best_score,best_move

    else:

        best_score = 99999999

        for sr,sc,tr,tc in moves:

            save_board = copy.deepcopy(board)
            save_turn = turn
            save_ep = en_passant

            make_move(sr,sc,tr,tc,False)

            score,_ = minimax(
                depth-1,
                alpha,
                beta,
                True
            )

            board[:] = save_board

            globals()["turn"] = save_turn
            globals()["en_passant"] = save_ep

            if score < best_score:

                best_score = score

                best_move = (
                    sr,
                    sc,
                    tr,
                    tc
                )

            beta = min(beta,score)

            if beta <= alpha:
                break

        return best_score,best_move


def ai_move():

    depth_map = {
        1:1,
        2:2,
        3:3,
        4:4,
        5:5
    }

    depth = depth_map[AI_LEVEL]

    _,move = minimax(
        depth,
        -99999999,
        99999999,
        False
    )

    if move:
        make_move(*move)


def make_move(
    sr,
    sc,
    tr,
    tc,
    save_history=True
):

    global turn
    global en_passant

    if save_history:

        history.append(
            (
                copy.deepcopy(board),
                turn,
                en_passant,
                copy.deepcopy(castle_rights)
            )
        )

    piece = board[sr][sc]

    color,kind = piece.split("_")

    if kind == "pawn":

        if abs(tr-sr) == 2:

            en_passant = (
                (tr+sr)//2,
                sc
            )

        else:

            en_passant = None

    else:

        en_passant = None

    ep_target = en_passant

    if (
        kind=="pawn"
        and
        ep_target
        and
        tc != sc
        and
        board[tr][tc] is None
    ):

        board[sr][tc] = None

    board[tr][tc] = piece
    board[sr][sc] = None

    if kind == "pawn":

        if tr == 0 or tr == 7:

            board[tr][tc] = (
                color +
                "_queen"
            )

    if kind == "king":

        castle_rights[color]["K"] = False
        castle_rights[color]["Q"] = False

        if abs(tc-sc) == 2:

            if tc == 6:

                board[tr][5] = board[tr][7]
                board[tr][7] = None

            elif tc == 2:

                board[tr][3] = board[tr][0]
                board[tr][0] = None

    if kind == "rook":

        if color == "white":

            if sr == 7 and sc == 0:
                castle_rights["white"]["Q"] = False

            elif sr == 7 and sc == 7:
                castle_rights["white"]["K"] = False

        else:

            if sr == 0 and sc == 0:
                castle_rights["black"]["Q"] = False

            elif sr == 0 and sc == 7:
                castle_rights["black"]["K"] = False

    turn = enemy(turn)

    check_result()


def undo():

    global board
    global turn
    global en_passant
    global castle_rights
    global winner

    if not history:
        return

    (
        old_board,
        old_turn,
        old_ep,
        old_castle
    ) = history.pop()

    board = copy.deepcopy(
        old_board
    )

    turn = old_turn

    en_passant = old_ep

    castle_rights = copy.deepcopy(
        old_castle
    )

    winner = None
def draw_board():

    for r in range(8):

        for c in range(8):

            color = LIGHT if (r + c) % 2 == 0 else DARK

            pygame.draw.rect(
                SCREEN,
                color,
                (
                    c * SQUARE,
                    r * SQUARE,
                    SQUARE,
                    SQUARE
                )
            ) 


def draw_moves():

    if selected is None:
        return

    sr,sc = selected

    pygame.draw.rect(
        SCREEN,
        YELLOW,
        (
            sc*SQUARE,
            sr*SQUARE,
            SQUARE,
            SQUARE
        ),
        4
    )

    for r,c in legal_moves:

        pygame.draw.circle(
            SCREEN,
            GREEN,
            (
                c*SQUARE + SQUARE//2,
                r*SQUARE + SQUARE//2
            ),
            10
        )


def draw_pieces():

    for r in range(8):

        for c in range(8):

            piece = board[r][c]

            if piece:

                x = c*SQUARE + (
                    SQUARE-PIECE_SIZE
                )//2

                y = r*SQUARE + (
                    SQUARE-PIECE_SIZE
                )//2

                SCREEN.blit(
                    pieces[piece],
                    (x,y)
                )


def draw_ui():

    pygame.draw.rect(
        SCREEN,
        BLACK,
        (
            WIDTH,
            0,
            UI_WIDTH,
            HEIGHT
        )
    )

    text = FONT.render(
        f"Turn : {turn}",
        True,
        WHITE
    )

    SCREEN.blit(
        text,
        (
            WIDTH+20,
            20
        )
    )

    level_text = FONT.render(
        f"AI : {AI_LEVEL}",
        True,
        WHITE
    )

    SCREEN.blit(
        level_text,
        (
            WIDTH+20,
            60
        )
    )

    undo_text = FONT.render(
        "U = Undo",
        True,
        WHITE
    )

    SCREEN.blit(
        undo_text,
        (
            WIDTH+20,
            100
        )
    )

    if winner:

        win = BIG.render(
            winner,
            True,
            WHITE
        )

        SCREEN.blit(
            win,
            (
                WIDTH+10,
                180
            )
        )


def start_menu():

    global mode
    global AI_LEVEL

    while True:

        SCREEN.fill((40,40,40))

        title = BIG.render(
            "Chess AI",
            True,
            WHITE
        )

        SCREEN.blit(
            title,
            (
                250,
                60
            )
        )

        one_player = pygame.Rect(
            200,
            180,
            250,
            70
        )

        two_player = pygame.Rect(
            200,
            280,
            250,
            70
        )

        pygame.draw.rect(
            SCREEN,
            (120,120,120),
            one_player
        )

        pygame.draw.rect(
            SCREEN,
            (120,120,120),
            two_player
        )

        SCREEN.blit(
            FONT.render(
                "1 PLAYER",
                True,
                WHITE
            ),
            (
                280,
                205
            )
        )

        SCREEN.blit(
            FONT.render(
                "2 PLAYER",
                True,
                WHITE
            ),
            (
                280,
                305
            )
        )

        level_buttons = []

        for i in range(5):

            rect = pygame.Rect(
                120 + i*90,
                420,
                70,
                50
            )

            level_buttons.append(rect)

            pygame.draw.rect(
                SCREEN,
                (90,90,90),
                rect
            )

            SCREEN.blit(
                FONT.render(
                    str(i+1),
                    True,
                    WHITE
                ),
                (
                    rect.x+25,
                    rect.y+12
                )
            )

        level_txt = FONT.render(
            f"Level : {AI_LEVEL}",
            True,
            WHITE
        )

        SCREEN.blit(
            level_txt,
            (
                250,
                380
            )
        )

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = event.pos

                if one_player.collidepoint(pos):

                    mode = "1P"
                    return

                if two_player.collidepoint(pos):

                    mode = "2P"
                    return

                for i,rect in enumerate(level_buttons):

                    if rect.collidepoint(pos):

                        AI_LEVEL = i+1

        pygame.display.flip()


def handle_events():

    global selected
    global legal_moves

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_u:

                undo()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if winner:
                continue

            x,y = pygame.mouse.get_pos()

            if x >= WIDTH:
                continue

            r = y // SQUARE
            c = x // SQUARE

            if selected:

                if (r,c) in legal_moves:

                    make_move(
                        selected[0],
                        selected[1],
                        r,
                        c
                    )

                selected = None
                legal_moves = []

            else:

                piece = board[r][c]

                if piece:

                    if piece.startswith(turn):

                        selected = (r,c)

                        legal_moves = (
                            legal_moves_for(
                                r,
                                c
                            )
                        )


def draw():

    draw_board()

    draw_moves()

    draw_pieces()

    draw_ui()

    pygame.display.flip()


def main():

    load_pieces()

    reset_board()

    start_menu()

    while True:

        CLOCK.tick(FPS)

        handle_events()

        if (
            mode == "1P"
            and
            turn == "black"
            and
            winner is None
        ):

            ai_move()

        draw()


if __name__ == "__main__":
    main()

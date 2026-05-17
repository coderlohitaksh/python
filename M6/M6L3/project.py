import pygame
import os

pygame.init()

SQUARE = 80
BOARD_SIZE = 8
BORDER = 60

WIDTH = SQUARE * BOARD_SIZE + BORDER * 2
HEIGHT = SQUARE * BOARD_SIZE + BORDER * 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wood Chess Board")

LIGHT = (240, 217, 181)
DARK = (181, 136, 99)
WOOD = (90, 55, 35)
TEXT = (230, 230, 230)

clock = pygame.time.Clock()

current_folder = os.path.dirname(__file__)

image_path = os.path.join(current_folder, "king.png")

king = pygame.image.load(image_path)
king = pygame.transform.smoothscale(king, (70, 70))

king_row = 7
king_col = 4

font = pygame.font.SysFont("timesnewroman", 22, bold=True)

running = True

while running:

    clock.tick(8)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT and king_col > 0:
                king_col -= 1

            if event.key == pygame.K_RIGHT and king_col < 7:
                king_col += 1

            if event.key == pygame.K_UP and king_row > 0:
                king_row -= 1

            if event.key == pygame.K_DOWN and king_row < 7:
                king_row += 1

    screen.fill(WOOD)

    pygame.draw.rect(
        screen,
        (120, 75, 45),
        (
            20,
            20,
            WIDTH - 40,
            HEIGHT - 40
        ),
        border_radius=8
    )

    for row in range(8):

        for col in range(8):

            color = LIGHT if (row + col) % 2 == 0 else DARK

            pygame.draw.rect(
                screen,
                color,
                (
                    BORDER + col * SQUARE,
                    BORDER + row * SQUARE,
                    SQUARE,
                    SQUARE
                )
            )

    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]

    for i in range(8):

        text = font.render(letters[i], True, TEXT)

        screen.blit(
            text,
            (
                BORDER + i * SQUARE + 33,
                HEIGHT - 40
            )
        )

    for i in range(8):

        text = font.render(str(8 - i), True, TEXT)

        screen.blit(
            text,
            (
                30,
                BORDER + i * SQUARE + 28
            )
        )

    screen.blit(
        king,
        (
            BORDER + king_col * SQUARE + 5,
            BORDER + king_row * SQUARE + 5
        )
    )

    pygame.display.flip()

pygame.quit()
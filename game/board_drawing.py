import pygame
from game.config import DIMENTION, SQUERE_SIZE


def draw_game(gameState, screen):
    draw_board(gameState, screen)
    draw_pieces(gameState, screen)


def draw_board(gameState, screen):
    colors = [
        (247, 247, 220),
        (177, 204, 176),
        (119, 149, 201),
        (201, 119, 142),
    ]  # [light, dark, marked, target]

    for y in range(DIMENTION):
        for x in range(DIMENTION):

            color = colors[(x + y) % 2]

            if gameState.current_move and len(gameState.current_move.clicks):
                if (
                    y == gameState.current_move.clicks[0][1]
                    and x == gameState.current_move.clicks[0][0]
                ):
                    color = colors[2]

            pygame.draw.rect(
                screen,
                color,
                pygame.Rect(x * SQUERE_SIZE, y * SQUERE_SIZE, SQUERE_SIZE, SQUERE_SIZE),
            )


def draw_pieces(gameState, screen):

    for y in range(DIMENTION):
        for x in range(DIMENTION):
            piece = gameState.board[y][x]
            if piece != "--":
                pieceImg = pygame.image.load("images/pieces/" + piece + ".png")
                screen.blit(
                    pieceImg,
                    pygame.Rect(
                        x * SQUERE_SIZE,
                        y * SQUERE_SIZE,
                        SQUERE_SIZE,
                        SQUERE_SIZE,
                    ),
                )

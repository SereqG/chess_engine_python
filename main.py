import pygame

from engine.game_state import GameState
from game.board_drawing import draw_game
from game.game_manager import event_detection
from game.config import WINDOW_HEIGHT, WINDOW_WIDTH

pygame.init()
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

clock = pygame.time.Clock()

pygame.display.set_caption("Chess engine by Sergiusz")


def main():
    gameState = GameState()
    while True:

        event_detection(gameState)
        screen.fill("white")
        draw_game(gameState, screen)

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)


if __name__ == "__main__":
    main()

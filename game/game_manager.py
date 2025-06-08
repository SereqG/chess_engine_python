import pygame
import game
import math


def event_detection(gameState):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            piece_movement(event, gameState)


def piece_movement(event, gameState):
    sq_size = game.board_drawing.SQUERE_SIZE

    xAxis = math.floor(event.dict["pos"][0] // sq_size)
    yAxis = math.floor(event.dict["pos"][1] / sq_size)

    gameState.handle_movement(xAxis, yAxis)

#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## checkers
## File description:
## checkers
##
import pygame
import sys
from move import *

# Plateau settings
SIZE = WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = HEIGHT // ROWS

# Couleur
DBROWN = (100, 45, 0)
LBROWN = (245, 190, 100)

#Plateau
board = [
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2]
]

# Initialisation fenêtre
pygame.init()
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Checkers")
clock = pygame.time.Clock()

def draw_board(window): # Dessine le plateau
    for row in range(ROWS):
        for col in range(COLS):
            color = DBROWN if (row + col) % 2 == 0 else LBROWN
            pygame.draw.rect(window, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_token(window, board): # Dessine le pion
    row = 0
    col = 0
    mid = SQUARE_SIZE // 2
    while (row < ROWS):
        while (col < COLS):
            if (board[row][col] == 1):
                x = mid + SQUARE_SIZE * col
                y = mid + SQUARE_SIZE * row
                pygame.draw.circle(window, "black", (x, y), SQUARE_SIZE // 2 - 10)
            if (board[row][col] == 2):
                x = mid + SQUARE_SIZE * col
                y = mid + SQUARE_SIZE * row
                pygame.draw.circle(window, "white", (x, y), SQUARE_SIZE // 2 - 10)
            col += 1
        row += 1
        col = 0

def get_pos(mouse_pos): # Convertie la position du click de la souris en coordonnée du carré
    return [int(mouse_pos[0] * COLS / WIDTH), int(mouse_pos[1] * ROWS / HEIGHT)]

def check_winner(board): # Vérifie si il y a un gagnant
    row = 0
    col = 0
    noir = 0
    blanc = 0
    while (row < ROWS):
        while (col < COLS):
            if board[row][col] == 1:
                noir += 1
            if board[row][col] == 2:
                blanc += 1
            col += 1
        row += 1
        col =0
    if noir == 0 or blanc == 0:
        return 0
    return 1

def make_king():
    for row in range(ROWS):
        for col in range(COLS):
            if (board[0][col] == 2):
                return 0

def main():
    running = True
    selected = None
    clicked = None
    action = 0
    turn_player = 1

    while running:
        # EVENT
        for event in pygame.event.get():

            # Fermer la fenêtre
            if event.type == pygame.QUIT:
                running = False

            # Event souris
            if event.type == pygame.MOUSEBUTTONDOWN and action == 0:
                mouse_pos = event.pos
                board_mouse_pos = get_pos(mouse_pos)
                selected = True
            if event.type == pygame.MOUSEBUTTONDOWN and action == 1:
                click_pos = event.pos
                board_click_pos = get_pos(click_pos)
                selected = False
                clicked = True

        if selected == True:
            action = 1
        if selected == False and clicked == True:
            if turn_player == 1 and move_type_black(board, board_mouse_pos, board_click_pos) > 0:
                move_black(board, board_click_pos, board_mouse_pos)
                turn_player = 2
            elif turn_player == 2 and move_type_white(board, board_mouse_pos, board_click_pos) > 0:
                move_white(board, board_click_pos, board_mouse_pos)
                turn_player = 1
            selected = None
            clicked = None
            action = 0

        if check_winner(board) == 0: # Si il y a un gagnant -> ferme la fenêtre
            running = False

        # Rendu du jeu
        window.fill("black")
        draw_board(window)
        draw_token(window, board)
        if selected == True:
            pygame.draw.circle(window, "yellow", mouse_pos, 25)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()

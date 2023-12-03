#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## checkers
## File description:
## checkers
##
import pygame
import sys
import copy
from move import *

# Plateau settings
SIZE = WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = HEIGHT // ROWS
# Couleur
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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

#Historique des positions
positions = [
    [
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2],
        [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2]
    ],
]

#Historique des undo
undos = []

def draw_board(window): # Dessine le plateau
    for row in range(ROWS):
        for col in range(COLS):
            color = DBROWN if (row + col) % 2 == 0 else LBROWN
            pygame.draw.rect(window, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_token(window, board): # Dessine le pion
    mid = SQUARE_SIZE // 2

    for row in range(ROWS):
        for col in range(COLS):
            if (board[row][col] == 1):
                x = mid + SQUARE_SIZE * col
                y = mid + SQUARE_SIZE * row
                pygame.draw.circle(window, "black", (x, y), SQUARE_SIZE // 2 - 10)
            if (board[row][col] == 2):
                x = mid + SQUARE_SIZE * col
                y = mid + SQUARE_SIZE * row
                pygame.draw.circle(window, "white", (x, y), SQUARE_SIZE // 2 - 10)
            if (board[row][col] == 3):
                x = mid + SQUARE_SIZE * col
                y = mid + SQUARE_SIZE * row
                pygame.draw.circle(window, RED, (x, y), SQUARE_SIZE // 2 - 10)
            if (board[row][col] == 4):
                x = mid + SQUARE_SIZE * col
                y = mid + SQUARE_SIZE * row
                pygame.draw.circle(window, BLUE, (x, y), SQUARE_SIZE // 2 - 10)

def make_king():
    for row in range(ROWS):
        for col in range(COLS):
            if (board[0][col] == 2):
                board[0][col] = 4
            if (board[-1][col] == 1):
                board[-1][col] = 3

def get_pos(mouse_pos): # Convertie la position du click de la souris en coordonnée du carré
    return [int(mouse_pos[0] * COLS / WIDTH), int(mouse_pos[1] * ROWS / HEIGHT)]

def check_winner(board): # Vérifie si il y a un gagnant
    row = 0
    col = 0
    noir = 0
    blanc = 0
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 1:
                noir += 1
            if board[row][col] == 2:
                blanc += 1
    if noir == 0 or blanc == 0:
        return 0
    return 1

def circle_selection(window, mouse_pos): # Dessine un cercle jaune sur la selection du pion
    mid = SQUARE_SIZE // 2
    posx = int(mouse_pos[0] * COLS / WIDTH)
    posy = int(mouse_pos[1] * COLS / WIDTH)
    x = mid + SQUARE_SIZE * posx
    y = mid + SQUARE_SIZE * posy
    pygame.draw.circle(window, "yellow", (x, y), SQUARE_SIZE // 2 - 40)

def print_position(position):
    for line in position:
        print(line)
    print("")

def swap_boards(board, position):
    for i in range(0, len(board), 1):
        for j in range(0, len(board[0]), 1):
            board[i][j] = position[i][j]

def undo(board, positions):
    if len(positions) == 1:
        return
    undos.append(positions[-1])
    swap_boards(board, positions[-2])
    positions.pop()

def redo(board, positions):
    if len(undos) == 0:
        return
    positions.append(undos[-1])
    swap_boards(board, positions[-1])
    undos.pop()

def main():
    pygame.init()
    window = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Checkers")
    clock = pygame.time.Clock()
    running = True
    selected = None
    clicked = None
    action = 0
    turn_player = 2

    while running:
        for event in pygame.event.get():

                ########    EXIT    ########
            if event.type == pygame.QUIT:
                running = False

                ########    EVENT MOUSE    ########
            if event.type == pygame.MOUSEBUTTONDOWN and action == 0:
                mouse_pos = event.pos
                board_mouse_pos = get_pos(mouse_pos)
                selected = True
            if event.type == pygame.MOUSEBUTTONDOWN and action == 1:
                click_pos = event.pos
                board_click_pos = get_pos(click_pos)
                selected = False
                clicked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    undo(board, positions)
                    if turn_player == 1:
                        turn_player = 2
                    elif turn_player == 2:
                        turn_player = 1
                if event.key == pygame.K_r:
                    redo(board, positions)
                    if turn_player == 1:
                        turn_player = 2
                    elif turn_player == 2:
                        turn_player = 1

        if selected == True:
            action = 1
        if selected == False and clicked == True:
            if turn_player == 1 and move_type_black(board, board_mouse_pos, board_click_pos) > 0:
                move_black(board, board_click_pos, board_mouse_pos)
                turn_player = 2
                positions.append(copy.deepcopy(board))
                undos.clear()
            elif turn_player == 2 and move_type_white(board, board_mouse_pos, board_click_pos) > 0:
                move_white(board, board_click_pos, board_mouse_pos)
                turn_player = 1
                positions.append(copy.deepcopy(board))
                undos.clear()
            selected = None
            clicked = None
            action = 0

        if check_winner(board) == 0: # Si il y a un gagnant -> ferme la fenêtre
            running = False

        # Rendu du jeu
        window.fill(BLACK)
        draw_board(window)
        draw_token(window, board)
        if selected == True:
            circle_selection(window, mouse_pos)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


main()
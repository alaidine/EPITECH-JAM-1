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

class Token:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

class Checkerboard:
    def __init__(self):
        self.board = [[None] * COLS for _ in range(ROWS)] # Création tableau 2D 8*8
        self.populate_board()

    def populate_board(self): # Position initial des pions
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 1 and row < 3:
                    self.board[row][col] = Token(row, col, BLACK)
                elif (row + col) % 2 == 1 and row > 4:
                    self.board[row][col] = Token(row, col, WHITE)

    def draw_board(self, window): # Dessine le plateau
        for row in range(ROWS):
            for col in range(COLS):
                color = DBROWN if (row + col) % 2 == 0 else LBROWN
                pygame.draw.rect(window, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def get_pos(mouse_pos): # Convertie la position du click de la souris en coordonnée du carré
    return [int(mouse_pos[0] * COLS / 800), int(mouse_pos[1] * ROWS / 800)]

def check_winner(board): # Vérifie si il y a un gagnant
    l = 0
    c = 0
    noir = 0
    blanc = 0

    while l < 8:
        while c < 8:
            if board[l][c] == 1:
                noir += 1
            if board[l][c] == 2:
                blanc += 1
            c += 1
        l += 1
        c =0
    if noir == 0 or blanc == 0:
        return 0
    return 1

def draw_token(window, board): # Dessine le pion
    l = 0
    c = 0
    mid = 50
    while (l < ROWS):
        while (c < COLS):
            if (board[l][c] == 1):
                x = mid + 100 * c
                y = mid + 100 * l
                pygame.draw.circle(window, BLACK, (x, y), SQUARE_SIZE // 2 - 10)
            if (board[l][c] == 2):
                x = mid + 100 * c
                y = mid + 100 * l
                pygame.draw.circle(window, WHITE, (x, y), SQUARE_SIZE // 2 - 10)
            c += 1
        l += 1
        c = 0

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
    checkerboard = Checkerboard()
    running = True
    selected = None
    clicked = None
    action = 0
    turn_player = 1

    while running:
        # EVENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
        checkerboard.draw_board(window)
        draw_token(window, board)
        if selected == True:
            pygame.draw.circle(window, "yellow", mouse_pos, 25)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


main()

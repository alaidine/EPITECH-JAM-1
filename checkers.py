#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## checkers
## File description:
## checkers
##
import pygame
import copy
from move import *
from ia import *


# Plateau settings
SIZE = WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = HEIGHT // ROWS

# Mode
MENU_MODE = 0
GAME_MODE = 1
RULES_MODE = 2
CHOOSE_MODE = 3
END_MODE = 4

# Couleur
DBROWN = (100, 45, 0)
LBROWN = (245, 190, 100)
RED = (215, 0, 0)
BLUE = (0, 140, 215)

# Window settings
pygame.init()
WINDOW = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Checkers")


# Pictures
BACKGROUND = pygame.image.load("content/background.jpg").convert()
PLAY_BUTTON = pygame.image.load("content/play.png").convert_alpha()
RULES_BUTTON = pygame.image.load("content/rules.png").convert_alpha()
EXIT_BUTTON = pygame.image.load("content/exit.png").convert_alpha()
RULES = pygame.image.load("content/Rules.jpg").convert()
BACK_BUTTON = pygame.image.load("content/back.png").convert()
SELECTION = pygame.image.load("content/Selection.jpg").convert()
IA_BUTTON = pygame.image.load("content/IA.png").convert_alpha()
PVP_BUTTON = pygame.image.load("content/PVP.png").convert_alpha()
REPLAY_BUTTON = pygame.image.load("content/replay.png").convert_alpha()
WIN = pygame.image.load("content/Win.jpg").convert()

turn = ["", "Black", "White"]

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

def draw_board(WINDOW): # Dessine le plateau
    for row in range(ROWS):
        for col in range(COLS):
            color = DBROWN if (row + col) % 2 == 0 else LBROWN
            pygame.draw.rect(WINDOW, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_token(WINDOW, board): # Dessine le pion
    mid = SQUARE_SIZE // 2

    for row in range(ROWS):
        for col in range(COLS):
            if (board[row][col] == 1):
                x = mid + SQUARE_SIZE * col
                y = mid + SQUARE_SIZE * row
                pygame.draw.circle(WINDOW, "black", (x, y), SQUARE_SIZE // 2 - 10)
            if (board[row][col] == 2):
                x = mid + SQUARE_SIZE * col
                y = mid + SQUARE_SIZE * row
                pygame.draw.circle(WINDOW, "white", (x, y), SQUARE_SIZE // 2 - 10)
            if (board[row][col] == 3):
                x = mid + SQUARE_SIZE * col
                y = mid + SQUARE_SIZE * row
                pygame.draw.circle(WINDOW, RED, (x, y), SQUARE_SIZE // 2 - 10)
            if (board[row][col] == 4):
                x = mid + SQUARE_SIZE * col
                y = mid + SQUARE_SIZE * row
                pygame.draw.circle(WINDOW, BLUE, (x, y), SQUARE_SIZE // 2 - 10)

def make_queen():    # Fait une reines
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
            if (board[row][col] == 1) or (board[row][col] == 3):
                noir += 1
            if (board[row][col] == 2) or (board[row][col] == 4):
                blanc += 1
    if noir == 0 or blanc == 0:
        return 0
    return 1

def circle_selection(WINDOW, mouse_pos): # Dessine un cercle jaune sur la selection du pion
    mid = SQUARE_SIZE // 2
    posx = int(mouse_pos[0] * COLS / WIDTH)
    posy = int(mouse_pos[1] * COLS / WIDTH)
    x = mid + SQUARE_SIZE * posx
    y = mid + SQUARE_SIZE * posy
    pygame.draw.circle(WINDOW, "yellow", (x, y), SQUARE_SIZE // 2 - 40)

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
    CLOCK = pygame.time.Clock()
    RUNNING = True
    PLAY_IA = False
    SELECTED = None
    CLICKED = None
    ACTION = 0
    TURN_PLAYER = 2
    SET_MODE = 0

    while RUNNING:
        for event in pygame.event.get():

                ########    EXIT    ########
            if event.type == pygame.QUIT:
                RUNNING = False
                    ############    MENU EVENT    ############
            if event.type == pygame.MOUSEBUTTONUP and SET_MODE == MENU_MODE:
                if pygame.mouse.get_pos()[0] > 280 and pygame.mouse.get_pos()[0] < (280 + 200):
                    if pygame.mouse.get_pos()[1] > 450 and pygame.mouse.get_pos()[1] < (450 + 100):
                        SET_MODE = CHOOSE_MODE    # PLAY
            if event.type == pygame.MOUSEBUTTONDOWN and SET_MODE == MENU_MODE:
                if pygame.mouse.get_pos()[0] > 280 and pygame.mouse.get_pos()[0] < (280 + 200):
                    if pygame.mouse.get_pos()[1] > 570 and pygame.mouse.get_pos()[1] < (570 + 100):
                        SET_MODE = RULES_MODE    # RULES
            if event.type == pygame.MOUSEBUTTONDOWN and SET_MODE == MENU_MODE:
                if pygame.mouse.get_pos()[0] > 280 and pygame.mouse.get_pos()[0] < (280 + 200):
                    if pygame.mouse.get_pos()[1] > 690 and pygame.mouse.get_pos()[1] < (690 + 100):
                        RUNNING = False # EXIT

                    ############    CHOOSE MODE    ############
            if event.type == pygame.MOUSEBUTTONDOWN and SET_MODE == CHOOSE_MODE:
                if pygame.mouse.get_pos()[0] > 220 and pygame.mouse.get_pos()[0] < (220 + 200):
                    if pygame.mouse.get_pos()[1] > 340 and pygame.mouse.get_pos()[1] < (340 + 100):
                        SET_MODE = GAME_MODE # IA
                        PLAY_IA = True
            if event.type == pygame.MOUSEBUTTONDOWN and SET_MODE == CHOOSE_MODE:
                if pygame.mouse.get_pos()[0] > 220 and pygame.mouse.get_pos()[0] < (220 + 200):
                    if pygame.mouse.get_pos()[1] > 530 and pygame.mouse.get_pos()[1] < (530 + 100):
                        SET_MODE = GAME_MODE    # PVP
                        PLAY_IA = False
            if event.type == pygame.MOUSEBUTTONDOWN and SET_MODE == CHOOSE_MODE:
                if pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < (600 + 200):
                    if pygame.mouse.get_pos()[1] > 700 and pygame.mouse.get_pos()[1] < (700 + 100):
                        SET_MODE = MENU_MODE    # BACK

                    ############    RULES EVENT    ############
            if event.type == pygame.MOUSEBUTTONDOWN and SET_MODE == RULES_MODE:
                if pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < (600 + 200):
                    if pygame.mouse.get_pos()[1] > 700 and pygame.mouse.get_pos()[1] < (700 + 100):
                        RUNNING = True  # BACK
                        SET_MODE = MENU_MODE
                    ############    WIN EVENT    ############
            if event.type == pygame.MOUSEBUTTONUP and SET_MODE == END_MODE:
                if pygame.mouse.get_pos()[0] > 280 and pygame.mouse.get_pos()[0] < (280 + 200):
                    if pygame.mouse.get_pos()[1] > 360 and pygame.mouse.get_pos()[1] < (360 + 100):
                        SET_MODE = MENU_MODE    # REPLAY
            if event.type == pygame.MOUSEBUTTONUP and SET_MODE == END_MODE:
                if pygame.mouse.get_pos()[0] > 280 and pygame.mouse.get_pos()[0] < (280 + 200):
                    if pygame.mouse.get_pos()[1] > 570 and pygame.mouse.get_pos()[1] < (570+ 100):
                        RUNNING = False # EXIT

                    ############    GAME EVENT    ############
            if event.type == pygame.MOUSEBUTTONDOWN and ACTION == 0 and SET_MODE == GAME_MODE:
                mouse_pos = event.pos
                board_mouse_pos = get_pos(mouse_pos)
                SELECTED = True
            if event.type == pygame.MOUSEBUTTONDOWN and ACTION == 1 and SET_MODE == GAME_MODE:
                click_pos = event.pos
                board_click_pos = get_pos(click_pos)
                SELECTED = False
                CLICKED = True
                ########    EVENT UNDO/REDO    ########
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    undo(board, positions)
                    if TURN_PLAYER == 1:
                        TURN_PLAYER = 2
                    elif TURN_PLAYER == 2:
                        TURN_PLAYER = 1
                if event.key == pygame.K_r:
                    redo(board, positions)
                    if TURN_PLAYER == 1:
                        TURN_PLAYER = 2
                    elif TURN_PLAYER == 2:
                        TURN_PLAYER = 1

        if SELECTED == True:
            ACTION = 1
        if SELECTED == False and CLICKED == True:
            if TURN_PLAYER == 1 and move_type_black(board, board_mouse_pos, board_click_pos) > 0:
                move_black(board, board_click_pos, board_mouse_pos)
                TURN_PLAYER = 2
                positions.append(copy.deepcopy(board))
                undos.clear()
            elif TURN_PLAYER == 2 and move_type_white(board, board_mouse_pos, board_click_pos) > 0 and PLAY_IA == False:
                move_white(board, board_click_pos, board_mouse_pos)
                TURN_PLAYER = 1
                positions.append(copy.deepcopy(board))
                undos.clear()
            elif TURN_PLAYER == 2 and board[board_mouse_pos[1]][board_mouse_pos[0]] == 4 and PLAY_IA == False:
                move_white_queen(board, board_click_pos, board_mouse_pos)
                TURN_PLAYER = 1
                positions.append(copy.deepcopy(board))
                undos.clear()
            elif TURN_PLAYER == 1 and board[board_mouse_pos[1]][board_mouse_pos[0]] == 3:
                move_black_queen(board, board_click_pos, board_mouse_pos)
                TURN_PLAYER = 2
                positions.append(copy.deepcopy(board))
                undos.clear()
            SELECTED = None
            CLICKED = None
            ACTION = 0

        if check_winner(board) == 0: # Si il y a un gagnant -> ferme la fenêtre
            SET_MODE = END_MODE
        print(SET_MODE)
        if TURN_PLAYER == 2 and PLAY_IA == True and SET_MODE == GAME_MODE:
            if movement_type_ia(board) == False:
                SET_MODE = END_MODE
            TURN_PLAYER = 1


        # Rendu du jeu
        if SET_MODE == GAME_MODE:
            WINDOW.fill("black")
            draw_board(WINDOW)
            make_queen()
            draw_token(WINDOW, board)
            pygame.draw.rect(WINDOW, turn[TURN_PLAYER], (750, 375, 50, 50))
            if SELECTED == True:
                circle_selection(WINDOW, mouse_pos)
        if SET_MODE == MENU_MODE:
            WINDOW.blit(BACKGROUND, (0, 0))
            WINDOW.blit(PLAY_BUTTON, (280, 450))
            WINDOW.blit(RULES_BUTTON, (280, 570))
            WINDOW.blit(EXIT_BUTTON, (280, 690))
        if SET_MODE == RULES_MODE:
            WINDOW.blit(RULES, (0, 0))
            WINDOW.blit(BACK_BUTTON, (600, 700))
        if SET_MODE == CHOOSE_MODE:
            WINDOW.blit(SELECTION, (0, 0))
            WINDOW.blit(IA_BUTTON, (220, 340))
            WINDOW.blit(PVP_BUTTON, (220, 530))
            WINDOW.blit(BACK_BUTTON, (600, 700))
        if SET_MODE == END_MODE:
            WINDOW.blit(WIN, (0, 0))
            WINDOW.blit(REPLAY_BUTTON, (280, 360))
            WINDOW.blit(EXIT_BUTTON, (280, 570))

        pygame.display.flip()
        CLOCK.tick(60)
    pygame.quit()


main()
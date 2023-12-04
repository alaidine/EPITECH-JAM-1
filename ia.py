#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## ia
## File description:
## ia
##
from random import *

def eat_right_up(board, y, x):
    enemy = board[y - 1][x + 1]
    click = board[y - 2][x + 2]

    if (enemy == 1 or enemy == 3) and  click == 0:
        board[y - 2][x + 2] = 2
        board[y - 1][x + 1] = 0
        board[y][x] = 0
        return True
    return False

def eat_right_down(board, y, x):
    enemy = board[y + 1][x + 1]
    click = board[y + 2][x + 2]

    if (enemy == 1 or enemy == 3) and  click == 0:
        board[y + 2][x + 2] = 2
        board[y + 1][x + 1] = 0
        board[y][x] = 0
        return True
    return False

def eat_left_up(board, y, x):
    enemy = board[y - 1][x - 1]
    click = board[y - 2][x - 2]

    if (enemy == 1 or enemy == 3) and  click == 0:
        board[y - 2][x - 2] = 2
        board[y - 1][x - 1] = 0
        board[y][x] = 0
        return True
    return False

def eat_left_down(board, y, x):
    enemy = board[y + 1][x - 1]
    click = board[y + 2][x - 2]

    if (enemy == 1 or enemy == 3) and  click == 0:
        board[y + 2][x - 2] = 2
        board[y + 1][x - 1] = 0
        board[y][x] = 0
        return True
    return False

def move_right_up(board, y, x):
    if board[y - 1][x + 1] == 0:
        board[y - 1][x + 1] = 2
        board[y][x] = 0
        return True
    return False

def move_left_up(board, y, x):
    if board[y - 1][x - 1] == 0:
        board[y - 1][x - 1] = 2
        board[y][x] = 0
        return True
    return False

def move_two_corner_left(board, y, x):
    if eat_right_up(board, y, x) == True:
        return True
    elif move_right_up(board, y, x) == True:
        return True
    else:
        return False

def move_two_corner_right(board, y, x):
    if eat_left_up(board, y, x) == True:
        return True
    elif move_left_up(board, y, x) == True:
        return True
    else:
        return False

def move_two_left(board, y, x):
    if eat_right_up(board, y, x) == True:
        return True
    elif move_right_up(board, y, x) == True:
        return True
    elif move_left_up(board, y, x) == True:
        return True
    else:
        return False

def move_two_right(board, y, x):
    if eat_left_up(board, y, x) == True:
        return True
    elif move_left_up(board, y, x) == True:
        return True
    elif move_left_up(board, y, x) == True:
        return True
    else:
        return False

def move_corner_left(board, y, x):
    if move_right_up(board, y, x) == True:
        return True
    else:
        return False

def move_corner_right(board, y, x):
    if move_left_up(board, y, x) == True:
        return True
    return False

def move_after_corner_left(board, y, x):
    if eat_right_down(board, y, x) == True:
        return True
    elif move_right_up(board, y, x) == True:
        return True
    elif move_left_up(board, y, x) == True:
        return True
    else:
        return False

def move_after_corner_right(board, y, x):
    if eat_left_down(board, y, x) == True:
        return True
    elif move_right_up(board, y, x) == True:
        return True
    elif move_left_up(board, y, x) == True:
        return True
    else:
        return False

def move_side_left(board, y, x):
    if eat_right_down(board, y, x) == True:
        return True
    elif eat_right_up(board, y, x) == True:
        return True
    elif move_right_up(board, y, x) == True:
        return True
    else :
        return False

def move_side_right(board, y, x):
    if eat_left_down(board, y, x) == True:
        return True
    if eat_left_up(board, y, x) == True:
        return True
    elif move_left_up(board, y, x) == True:
        return True
    else :
        return False

def move_line_right(board, y, x):
    if eat_left_down(board, y, x) == True:
        return True
    elif eat_left_up(board, y, x) == True:
        return True
    elif move_right_up( board, y, x) == True:
        return True
    elif move_left_up(board, y, x) == True:
        return True
    else:
        return False

def move_line_left(board, y, x):
    if eat_right_down(board, y, x) == True:
        return True
    elif eat_right_up(board, y, x) == True:
        return True
    elif move_right_up( board, y, x) == True:
        return True
    elif move_left_up(board, y, x) == True:
        return True
    else:
        return False

def move_line_right(board, y, x):
    if eat_left_down(board, y, x) == True:
        return True
    elif eat_left_up(board, y, x) == True:
        return True
    elif move_right_up( board, y, x) == True:
        return True
    elif move_left_up(board, y, x) == True:
        return True
    else:
        return False

def move_line_top(board, y, x):
    if eat_left_down(board, y, x) == True:
        return True
    elif eat_right_down(board, y, x) == True:
        return True
    elif move_left_up(board, y, x) == True:
        return True
    elif move_right_up(board, y, x) == True:
        return True
    else:
        return False

def move_square_bot(board, y, x):
    if eat_left_up(board, y, x) == True:
        return True
    elif eat_right_up(board, y, x) == True:
        return True
    elif move_right_up(board, y, x) == True:
        return True
    elif move_left_up(board, y, x) == True:
        return True
    else:
        return False

def move_middle(board, y, x):
    if eat_right_down(board, y, x) == True:
        return True
    elif eat_left_down(board, y, x) == True:
        return True
    elif eat_right_up(board, y, x) == True:
        return True
    elif eat_left_up(board, y, x) == True:
        return True
    elif move_right_up(board, y, x) == True:
        return True
    elif move_left_up(board, y, x) == True:
        return True
    else:
        return False

def movement_type_ia(board):
    finding = True
    n = 0

    while finding:
        x, y = randint(0, 7), randint(0, 7)
        if board[y][x] == 2:
            if x == 0 and y > 5:
                if move_two_corner_left(board, y, x) == True:
                    finding = False
            elif x == 1 and y > 5:
                if move_two_left(board, y, x) == True:
                    finding = False
            elif x == 6 and y > 5:
                if move_two_right(board, y, x) == True:
                    finding = False
            elif x == 7 and y > 5:
                if move_two_corner_right(board, y, x) == True:
                    finding = False
            elif x == 0 and y == 1:
                if move_corner_left(board, y, x) == True:
                    finding = False
            elif x == 7 and y == 1:
                if move_corner_right(board, y, x) == True:
                    finding = False
            elif x == 6 and y == 1:
                if move_after_corner_left(board, y, x) == True:
                    finding = False
            elif x == 1 and y == 1:
                if move_after_corner_right(board, y, x) == True:
                    finding = False
            elif x == 0 and y > 0 and y < 6:
                if move_side_left(board, y, x) == True:
                    finding = False
            elif x == 7 and y > 0 and y < 6:
                if move_side_right(board, y, x) == True:
                    finding = False
            elif x == 6 and y > 1 and y < 6:
                if move_line_right(board, y, x) == True:
                    finding = False
            elif x == 1 and y > 1 and y < 6:
                if move_line_left(board, y, x) == True:
                    finding = False
            elif x > 1 and x < 6 and y > 5:
                if move_square_bot(board, y, x) == True:
                    finding = False
            elif x > 1 and x < 6 and y == 1:
                if move_line_top(board, y, x) == True:
                    finding = False
            else:
                if move_middle(board, y, x) == True:
                    finding = False
        n += 1
        if n > 600:
            return False
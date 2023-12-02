#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## move
## File description:
## move

def move_type_black(board, pos, click):
    x, y = pos[0], pos[1]
    cx, cy = click[0], click[1]

    if board[y][x] != 1:
        return 0
    if cx == x + 1 and cy == y + 1:
        return 1
    if cx == x - 1 and cy == y + 1:
        return 1
    if cx == x + 2 and cy == y + 2:
        return 2
    if cx == x - 2 and cy == y + 2:
        return 3
    return 0

def move_black(board, click, pos):
    x, y = pos[0], pos[1]
    cx, cy = click[0], click[1]

    if move_type_black(board, pos, click) == 0:
        return False
    if move_type_black(board, pos, click) == 1:
        if board[cy][cx] == 0:
            board[y][x] = 0
            board[cy][cx] = 1
            return True
    if move_type_black(board, pos, click) == 2:
        if board[cy - 1][cx - 1] == 2 and board[cy][cx] == 0:
            board[cy - 1][cx - 1] = 0
            board[y][x] = 0
            board[cy][cx] = 1
            return True
    if move_type_black(board, pos, click) == 3:
        if board[cy - 1][cx + 1] == 2 and board[cy][cx] == 0:
            board[cy - 1][cx + 1] = 0
            board[y][x] = 0
            board[cy][cx] = 1
            return True
    return False

def move_type_white(board, pos, click):
    x, y = pos[0], pos[1]
    cx, cy = click[0], click[1]

    if board[y][x] != 2:
        return 0
    if cx == x + 1 and cy == y - 1:
        return 1
    if cx == x - 1 and cy == y - 1:
        return 1
    if cx == x + 2 and cy == y - 2:
        return 2
    if cx == x - 2 and cy == y - 2:
        return 3
    return 0

def move_white(board, click, pos):
    x, y = pos[0], pos[1]
    cx, cy = click[0], click[1]

    if move_type_white(board, pos, click) == 0:
        return False
    if move_type_white(board, pos, click) == 1:
        if board[cy][cx] == 0:
            board[y][x] = 0
            board[cy][cx] = 2
            return True
    if move_type_white(board, pos, click) == 2:
        if board[cy + 1][cx - 1] == 1 and board[cy][cx] == 0:
            board[cy + 1][cx - 1] = 0
            board[y][x] = 0
            board[cy][cx] = 2
            return True
    if move_type_white(board, pos, click) == 3:
        if board[cy + 1][cx + 1] == 1 and board[cy][cx] == 0:
            board[cy + 1][cx + 1] = 0
            board[y][x] = 0
            board[cy][cx] = 2
            return True
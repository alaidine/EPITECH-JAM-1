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
        if board[cy][cx] == 0:
            return 1
    if cx == x - 1 and cy == y + 1:
        if board[cy][cx] == 0:
            return 1
    if cx == x + 2 and cy == y + 2:
        if board[cy - 1][cx - 1] == 2 and board[cy][cx] == 0:
            return 2
    if cx == x - 2 and cy == y + 2:
        if board[cy - 1][cx + 1] == 2 and board[cy][cx] == 0:
            return 3
    if cx == x + 2 and cy == y - 2:
        if board[cy + 1][cx - 1] == 2 and board[cy][cx] == 0:
            return 4
    if cx == x - 2 and cy == y - 2:
        if board[cy + 1][cx + 1] == 2 and board[cy][cx] == 0:
            return 5
    return 0

def move_black(board, click, pos):
    x, y = pos[0], pos[1]
    cx, cy = click[0], click[1]

    if move_type_black(board, pos, click) == 0:
        return False
    if move_type_black(board, pos, click) == 1:
#        if board[cy][cx] == 0:
        board[y][x] = 0
        board[cy][cx] = 1
        return True
    if move_type_black(board, pos, click) == 2:
#        if board[cy - 1][cx - 1] == 2 and board[cy][cx] == 0:
        board[cy - 1][cx - 1] = 0
        board[y][x] = 0
        board[cy][cx] = 1
        return True
    if move_type_black(board, pos, click) == 3:
#        if board[cy - 1][cx + 1] == 2 and board[cy][cx] == 0:
        board[cy - 1][cx + 1] = 0
        board[y][x] = 0
        board[cy][cx] = 1
        return True
    if move_type_black(board, pos, click) == 4:
        board[cy + 1][cx - 1] = 0
        board[y][x] = 0
        board[cy][cx] = 1
        return True
    if move_type_black(board, pos, click) == 5:
        board[cy + 1][cx + 1] = 0
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
        if board[cy][cx] == 0:
            return 1
    if cx == x - 1 and cy == y - 1:
        if board[cy][cx] == 0:
            return 1
    if cx == x + 2 and cy == y - 2:
        if board[cy + 1][cx - 1] == 1 and board[cy][cx] == 0:
            return 2
    if cx == x - 2 and cy == y - 2:
        if board[cy + 1][cx + 1] == 1 and board[cy][cx] == 0:
            return 3
    if cx == x + 2 and cy == y + 2:
        if board[cy - 1][cx - 1] == 1 and board[cy][cx] == 0:
            return 4
    if cx == x - 2 and cy == y + 2:
        if board[cy - 1][cx + 1] == 1 and board[cy][cx] == 0:
            return 5
    return 0

def move_white(board, click, pos):
    x, y = pos[0], pos[1]
    cx, cy = click[0], click[1]

    if move_type_white(board, pos, click) == 0:
        return False
    if move_type_white(board, pos, click) == 1:
 #       if board[cy][cx] == 0:
        board[y][x] = 0
        board[cy][cx] = 2
        return True
    if move_type_white(board, pos, click) == 2:
#        if board[cy + 1][cx - 1] == 1 and board[cy][cx] == 0:
        board[cy + 1][cx - 1] = 0
        board[y][x] = 0
        board[cy][cx] = 2
        return True
    if move_type_white(board, pos, click) == 3:
 #       if board[cy + 1][cx + 1] == 1 and board[cy][cx] == 0:
        board[cy + 1][cx + 1] = 0
        board[y][x] = 0
        board[cy][cx] = 2
        return True
    if move_type_white(board, pos, click) == 4:
        board[cy - 1][cx - 1] = 0
        board[y][x] = 0
        board[cy][cx] = 2
        return True
    if move_type_white(board, pos, click) == 5:
        board[cy - 1][cx + 1] = 0
        board[y][x] = 0
        board[cy][cx] = 2
        return True
    return False

def move_white_queen(board, pos, click):
    x, y = pos[0], pos[1]
    cx, cy = click[0], click[1]
    vec = (x - cx, y - cy)

    sign_x = -1 if vec[0] < 0 else 1
    sign_y = -1 if vec[1] < 0 else 1
    if abs(vec[0]) != abs(vec[1]) or board[y][x] > 0:
        return
    board[cy][cx] = 0
    board[y][x] = 4
    for i in range(0, abs(vec[0]), 1):
        if board[cy + (i * sign_y)][cx + (i * sign_x)] == 1 or board[cy + (i * sign_y)][cx + (i * sign_x)] == 3:
            board[cy + (i * sign_y)][cx + (i * sign_x)] = 0

def move_black_queen(board, pos, click):
    x, y = pos[0], pos[1]
    cx, cy = click[0], click[1]
    vec = (x - cx, y - cy)

    sign_x = -1 if vec[0] < 0 else 1
    sign_y = -1 if vec[1] < 0 else 1
    if abs(vec[0]) != abs(vec[1]) or board[y][x] > 0:
        return
    board[cy][cx] = 0
    board[y][x] = 3
    for i in range(0, abs(vec[0]), 1):
        if board[cy + (i * sign_y)][cx + (i * sign_x)] == 2 or board[cy + (i * sign_y)][cx + (i * sign_x)] == 4:
            board[cy + (i * sign_y)][cx + (i * sign_x)] = 0

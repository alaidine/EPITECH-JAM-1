#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## checkers
## File description:
## checkers
##
import pygame
import sys

# Plateau
SIZE = WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = HEIGHT // ROWS
# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DBROWN = (100, 45, 0)
LBROWN = (245, 190, 100)

class Token:    # Definie la classe Token
    def __init__(self, row, col, color):    # Initialisation de Token
        self.row = row
        self.col = col
        self.color = color

    def draw(self, window): # Fonction dessine Token
        pygame.draw.circle(window, self.color, (self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 10)   # Dessine le cercle

class Checkerboard: # Definie la classe Checkerboard
    def __init__(self): # Inisialisation de Checkboard
        self.board = [[None] * COLS for line in range(ROWS)]   # Plateau = tableau 2D (8x8)
        self.populate_board()

    def populate_board(self):   # Fonction pour placer les pions
        for row in range(ROWS): #
            for col in range(COLS):
                if (row + col) % 2 == 1 and row < 3:
                    self.board[row][col] = Token(row, col, BLACK)
                elif (row + col) % 2 == 1 and row > 4:
                    self.board[row][col] = Token(row, col, WHITE)

    def draw(self, window): # Fonction pour dessiner le board
        for row in range(ROWS):
            for col in range(COLS):
                color = LBROWN if (row + col) % 2 == 0 else DBROWN  # Definie la couleur: light_brown sinon dark_brown
                pygame.draw.rect(window, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))   # Dessine le carré
                token = self.board[row][col]
                if token:
                    token.draw(window)

def draw_circle(window):
    pygame.draw.circle(window, WHITE, (50, 50), 40.0)

def main():
    # Pygame setup
    pygame.init() # Initialisation
    window = pygame.display.set_mode(SIZE) # Taille window
    pygame.display.set_caption("Checkers") # Titre window
    clock = pygame.time.Clock()
    checkerboard = Checkerboard()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Si event == quit:
                running = False # Arrete boucle inf

        # RENDU DU JEU
        window.fill(BLACK) # Couleur fond window
        checkerboard.draw(window); # Dessine le plateau
        pygame.display.flip() # Affiche window
        clock.tick(60) # Limite 60FPS

    pygame.quit() # Ferme la window

main()

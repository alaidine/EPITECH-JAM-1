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
DBROWN = (90, 40, 0)
LBROWN = (100, 72, 34)


class Checkerboard: # Definie la classe Checkerboard
    def draw(window): # Fonction pour dessiner le board
        for row in range(ROWS): # Pour chaque lignes(8) dans le tableau ROWS(8)
            for col in range(COLS): # Pour chaque colonnes(8) dans le tableau COLS(8)
                color = LBROWN if (row + col) % 2 == 0 else DBROWN # Definie la couleur: light_brown sinon dark_brown
                pygame.draw.rect(window, color, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) # Dessine le carré

def draw_circle(window):
    pygame.draw.circle(window, WHITE, (50, 50), 40.0)

def main():
    # Pygame setup
    pygame.init() # Initialisation
    window = pygame.display.set_mode((SIZE)) # Taille window
    pygame.display.set_caption("Checkers") # Titre window
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Si event == quit:
                running = False # Arrete boucle inf

        # RENDU DU JEU
        window.fill("black") # Couleur fond window
        Checkerboard.draw(window);
        pygame.display.flip() # Affiche window
        clock.tick(60) # Limite 60FPS

    pygame.quit() # Ferme la window

main()

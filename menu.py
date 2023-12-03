#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## menu
## File description:
## menu
##
import pygame
from pygame.locals import QUIT, RESIZABLE

pygame.init()

fenetre = pygame.display.set_mode((800, 800), RESIZABLE)


running = True
set_mode = 0
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and set_mode == 0:
            if pygame.mouse.get_pos()[0] > 280 and pygame.mouse.get_pos()[0] < (280 + 200):
                if pygame.mouse.get_pos()[1] > 450 and pygame.mouse.get_pos()[1] < (450 + 100):
                    running = False
                    set_mode = 1
        if event.type == pygame.MOUSEBUTTONDOWN and set_mode == 0:
            if pygame.mouse.get_pos()[0] > 280 and pygame.mouse.get_pos()[0] < (280 + 200):
                if pygame.mouse.get_pos()[1] > 570 and pygame.mouse.get_pos()[1] < (570 + 100):
                    set_mode = 2
        if event.type == pygame.MOUSEBUTTONDOWN and set_mode == 0:
            if pygame.mouse.get_pos()[0] > 280 and pygame.mouse.get_pos()[0] < (280 + 200):
                if pygame.mouse.get_pos()[1] > 690 and pygame.mouse.get_pos()[1] < (690 + 100):
                    running = False
        if event.type == pygame.MOUSEBUTTONDOWN and set_mode == 2:
            if pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < (600 + 200):
                if pygame.mouse.get_pos()[1] > 700 and pygame.mouse.get_pos()[1] < (700 + 100):
                    running = True
                    set_mode = 0
    if set_mode == 0:
        fenetre.blit(fond, (0, 0))
        fenetre.blit(fond2, (280, 450))
        fenetre.blit(fond3, (280, 570))
        fenetre.blit(fond4, (280, 690))
    if set_mode == 2:
        fenetre.blit(fond5, (0, 0))
        fenetre.blit(fond6, (600, 700))
    pygame.display.flip()
pygame.quit()
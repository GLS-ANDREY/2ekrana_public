import pygame, model, random
from pygame import *
def allsobitiya2():
    s = pygame.event.get()
    for a in s:
        if a.type == pygame.KEYDOWN and a.key == pygame.K_ESCAPE:
            model.ekran = 0

        if a.type == pygame.KEYDOWN and a.key == pygame.K_SPACE:
            model.cifra += 1

        if a.type == pygame.MOUSEBUTTONDOWN:
            model.cifra -= 1

        if a.type == pygame.QUIT:
            exit()
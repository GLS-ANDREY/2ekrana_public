import pygame, model, random
from pygame import *


def allsobitiya():
    s = pygame.event.get()
    for a in s:

        if a.type == pygame.KEYDOWN and a.key == pygame.K_ESCAPE:
            model.ekran = 1

        if a.type == pygame.MOUSEBUTTONDOWN:
            model.color1 = random.randint(30,255)
            model.color2 = random.randint(30,255)
            model.color3 = random.randint(30,255)

        if a.type == pygame.QUIT:
            exit()
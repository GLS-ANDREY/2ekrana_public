import pygame, model, random
from pygame import *

display = display.set_mode([1000, 1000])

def risovanie():
    display.fill([0, 0, 0])
    draw.rect(display,[model.color1,model.color2,model.color3],model.rect_gl)
    pygame.display.flip()

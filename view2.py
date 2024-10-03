import pygame, model, random
from pygame import *

init()
font = pygame.font.SysFont("arial", 27, True)
font2 = pygame.font.SysFont("arial", 100, True)
display = display.set_mode([1000, 1000])
def risovanie2():
    display.fill([1, 255, 30])
    ekrani = font.render("Зеленый экран это первый экран, а экран с квадратом это второй экран", True, [255,0,1])
    esc = font.render("Esc - Переключиться на другой экран", True, [255,0,1])
    space = font.render("Space - К цифре на первом экране прибалвяется 1", True, [255,0,1])
    click_1_ekran = font.render("Если кликнуть на первом экране то от цифры отнимется 1", True, [255,0,1])
    click_2_ekran = font.render("Если кликнуть на втором экране то прямоугольник поменяет цвет на рандомный", True, [255,0,1])
    odin = font2.render(str(model.cifra), True, [model.color1, model.color2, model.color3])

    display.blit(odin,[500,500])
    display.blit(esc,[0,0])
    display.blit(space,[0,30])
    display.blit(ekrani,[0,60])
    display.blit(click_1_ekran,[0,90])
    display.blit(click_2_ekran,[0,120])
    pygame.display.flip()


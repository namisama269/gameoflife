import random
from time import sleep

import pygame
from pygame import mouse
from pygame.locals import *

from grid import GOL_Grid

pygame.init()
pygame.display.set_caption("hiskeri bundi")

WIDTH = 1270
HEIGHT = 720

CELL_SIZE = 20
DIVIDER_SIZE = 1

h, w = WIDTH//CELL_SIZE, HEIGHT//CELL_SIZE
gr = GOL_Grid(w, h)

DIVIDER_COLOR = (207,225,254)#(211,211,211)
DEAD_COLOR = (255,255,255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(DIVIDER_COLOR)

def randomcolor():
    mn, mx = 128, 255
    return (random.randint(mn,mx), random.randint(mn,mx), random.randint(mn,mx))

def draw_cells():
    for i in range(gr.dm, gr.m + gr.dm + 1):
        for j in range(gr.dn, gr.n + gr.dn + 1):
            x_pos = (j-gr.dn) * CELL_SIZE
            y_pos = (i-gr.dm) * CELL_SIZE
            color = DEAD_COLOR if gr.curr[i][j] == 0 else randomcolor()
            pygame.draw.rect(screen, color, (x_pos, y_pos, CELL_SIZE-DIVIDER_SIZE, \
            CELL_SIZE-DIVIDER_SIZE))

draw_cells()

running = True
paused = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            if paused and event.unicode == 'r':
                gr.random_fill()
                draw_cells()
            if paused and event.key == pygame.K_ESCAPE:
                gr.reset()
                draw_cells()

        if paused and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x = mouse_pos[1]//CELL_SIZE
            y = mouse_pos[0]//CELL_SIZE
            gr.set_gui(x, y)
            draw_cells()
    
    sleep(0.001)
    if not paused: 
        gr.do_next_gen()
        draw_cells()

    pygame.display.flip()
    pygame.display.update()



import pygame as py
import tkinter as tk
import numpy as np

dark = (0, 0, 0)
light = (200, 200, 200)
window = 400
size = 20
scale = int(window/size)
grid = np.random.randint(0, 2, (scale, scale), 'int8')

def game():
    py.init()
    screen = py.display.set_mode((window, window))
    py.display.set_caption("Conway's Game of Life")
    running=True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
        for x in range(len(grid[0])):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    py.draw.rect(screen, dark, (scale, scale, scale, scale), 1)
                else:
                    py.draw.rect(screen, light, (scale, scale, scale, scale), 1)

game()
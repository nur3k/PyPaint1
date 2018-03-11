import pygame
import sys
from pygame.locals import *
from tkinter import *
import time


class Meenu:
    coloursDictionaryValues = {pygame.K_UP: 'BLUE', pygame.K_LEFT: 'RED', pygame.K_RIGHT: 'WHITE'}
    color = 'RED'
    image_local = 'C:\\Users\\214896\\Pictures\\kot.jpg'

    def __init__(self, x=500, y=600):
        self.window = pygame.display.set_mode((x, y))
        self.brushThickness = 300
        pygame.display.set_caption('PaintBeta')
        loadedimage = pygame.image.load(self.image_local)
        screen = pygame.display.get_surface()
        screen.blit(loadedimage, (0, 0))
        pygame.display.flip()
        while True:
            self.input2()

    @staticmethod
    def declarecolour(colour):
        coltmp = (0, 0, 0)
        if colour == 'RED':
            coltmp = (255, 0, 0)
        elif colour == 'WHITE':
            coltmp = (255, 255, 255)
        elif colour == 'BLUE':
            coltmp = (0, 0, 255)
        return coltmp

    def change_color(self, event):
        for k, v in self.coloursDictionaryValues.items():
            if event == k:
                self.color = v
        return 0

    def choosecolourbox(self):
        pass

    def create_cross(self, brush=20):
        x, y = pygame.mouse.get_pos()
        brush = int(brush/2)
        for value in range(-brush, brush):
            self.window.set_at((x + value, y + value), (self.declarecolour(self.color)))
            self.window.set_at((x + value, y - value), (self.declarecolour(self.color)))
            self.window.set_at((x, y + value), (self.declarecolour(self.color)))
            self.window.set_at((x + value, y), (self.declarecolour(self.color)))
        pygame.display.update()
        return 0

    def create_square(self, brush=20):
        x, y = pygame.mouse.get_pos()
        brush = int(brush/2)
        for xx in range(-brush, brush):
            for yy in range(-brush, brush):
                self.window.set_at((x + xx, y + yy), (self.declarecolour(self.color)))
        pygame.display.update()
        return 0

    def create_circle(self, radius=20):
        radius = int(radius / 2)
        x0, y0 = pygame.mouse.get_pos()
        dx, dy = 1, 1
        x, y = radius - 1, 0
        err = dx - (radius << 1)
        while x >= y:
            self.window.set_at((x0 + x, y0 + y), (self.declarecolour(self.color)))
            time.sleep(0.08)
            pygame.display.update()
            self.window.set_at((x0 + y, y0 + x), (self.declarecolour(self.color)))
            self.window.set_at((x0 - y, y0 + x), (self.declarecolour(self.color)))
            self.window.set_at((x0 - x, y0 + y), (self.declarecolour(self.color)))
            self.window.set_at((x0 - x, y0 - y), (self.declarecolour(self.color)))
            self.window.set_at((x0 - y, y0 - x), (self.declarecolour(self.color)))
            self.window.set_at((x0 + y, y0 - x), (self.declarecolour(self.color)))
            self.window.set_at((x0 + x, y0 - y), (self.declarecolour(self.color)))
            if err <= 0:
                y = y+1
                err = err + dy
                dy = dy + 2
            if err > 0:
                x = x - 1
                dx = dx + 2
                err = err + dx - (radius << 1)
        pygame.display.update()

    def input2(self):
        for event in pygame.event.get():
            # print(event)
            if event.type == QUIT:
                sys.exit(0)
            elif pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                self.window.set_at((x, y), (self.declarecolour(self.color)))
                pygame.display.update()
            elif pygame.key.get_pressed()[K_SPACE]:
                self.create_square(self.brushThickness)
            elif pygame.key.get_pressed()[K_s]:
                self.create_cross(self.brushThickness)
            elif pygame.key.get_pressed()[K_c]:
                self.create_circle(self.brushThickness)
            elif pygame.key.get_pressed()[K_EQUALS]:
                self.brushThickness = self.brushThickness + 1
            elif pygame.key.get_pressed()[K_MINUS]:
                if not self.brushThickness < 3:
                    self.brushThickness = self.brushThickness - 1
            elif event.type == KEYDOWN:
                # coloursDictionaryValues. Change color by arrows
                self.change_color(event.key)
        return 0


Meenu()
#print(Meenu.create_circle(255, 255, 10))


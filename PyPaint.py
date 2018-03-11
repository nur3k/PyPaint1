import pygame
from pygame.locals import *
from tkinter import *
import time

class Meenu:
    coloursDictionaryValues = {pygame.K_UP: 'BLUE', pygame.K_LEFT: 'RED', pygame.K_RIGHT: 'WHITE'}
    brushTypeSelection = {pygame.K_c: 'CIRCLE', pygame.K_s: 'CROSS', pygame.K_SPACE: 'SQUARE', pygame.K_d: 'DOT',
                          pygame.K_e: 'EMPTYSQUARE', pygame.K_a: 'CIRCLEAA'}
    color = 'RED'
    brushtype = 'DOT'
    image_local = 'C:\\Users\\214896\\Pictures\\kot.jpg'
    brushThickness = 50

    def __init__(self, x=500, y=600):
        self.window = pygame.display.set_mode((x, y))
        pygame.display.set_caption('PaintBeta')
        # loadedimage = pygame.image.load(self.image_local)
        screen = pygame.display.get_surface()
        # screen.blit(loadedimage, (0, 0))
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

    def change_brush_type(self, event):
        for k, v in self.brushTypeSelection.items():
            if event == k:
                self.brushtype = v
        return 0

    def adjustbrush(self, event):
        if event == 4:
            self.brushThickness = self.brushThickness + 1
        elif event == 5:
            if not self.brushThickness < 3:
                self.brushThickness = self.brushThickness - 1

    def brush(self):
        if self.brushtype == 'SQUARE':
            self.create_square(self.brushThickness)
        elif self.brushtype == 'CROSS':
            self.create_cross(self.brushThickness)
        elif self.brushtype == 'CIRCLE':
            self.create_ring(self.brushThickness)
        elif self.brushtype == 'DOT':
            self.create_dot()
        elif self.brushtype == 'EMPTYSQUARE':
            self.create_empty_square(self.brushThickness)
        elif self.brushtype == 'CIRCLEAA':
            self.create_circle(self.brushThickness)
        pygame.display.update()

    def choosecolourbox(self):
        pass

    def create_dot(self):
        x, y = pygame.mouse.get_pos()
        self.window.set_at((x, y), (self.declarecolour(self.color)))

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
        for xx in range(-brush, brush+1):
            for yy in range(-brush, brush+1):
                self.window.set_at((x + xx, y + yy), (self.declarecolour(self.color)))
        pygame.display.update()
        return 0

    def create_empty_square(self, brush=20):
        x, y = pygame.mouse.get_pos()
        brush = int(brush/2)
        for xx in range(-brush, brush+1):
            for yy in range(-brush, brush+1):
                if yy == -brush or yy == brush:
                    self.window.set_at((x + xx, y + yy), (self.declarecolour(self.color)))
                if xx == -brush or xx == brush:
                    self.window.set_at((x + xx, y + yy), (self.declarecolour(self.color)))
        pygame.display.update()
        return 0

    def create_ring(self, radius=20):
        radius = int(radius / 2)
        x0, y0 = pygame.mouse.get_pos()
        dx, dy = 1, 1
        x, y = radius - 1, 0
        err = dx - (radius << 1)
        while x >= y:
            self.window.set_at((x0 + x, y0 + y), (self.declarecolour(self.color)))
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

    def create_circle(self, radius=20):
        for i in range(1, radius+1):
            self.create_ring(i)

    def input2(self):
        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                sys.exit(0)
            if pygame.mouse.get_pressed()[0]:
                # mouse button holding:
                self.brush()
            if event.type == KEYDOWN:
                # clicking keyboards button
                # coloursDictionaryValues. Change color by arrows
                self.change_color(event.key)
                # change brush type by clicking SPACE/C/S/D
                self.change_brush_type(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # clicking mouse button
                # adjust size of the brush by scrolling the wheel
                self.adjustbrush(event.button)
        return 0


Meenu(900, 900)


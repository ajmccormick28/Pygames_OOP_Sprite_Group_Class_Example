import pygame

class Canvas:

    def __init__(self, w, h, name="None"):
        self.w = w
        self.h = h
        self.screen = pygame.display.set_mode((self.w, self.h), pygame.DOUBLEBUF)

    @staticmethod
    def update():
        pygame.display.flip()

    def drawText(self, text, size, x, y):
        pygame.font.init()
        font = pygame.font.SysFont("helvetica", size)
        render = font.render(text, 1, (0,0,0))

        self.screen.draw(render, (x,y))

    def getCanvas(self):
        return self.screen

    def drawBackground(self):
        self.screen.fill("#FBFCFB")
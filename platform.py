import constants
import pygame
import random

class Platform(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.surf = pygame.Surface((random.randint(50, 100), 12))
        self.surf.fill("#CFF2FF")
        self.rect = self.surf.get_rect(center = (random.randint(0, constants.WIDTH - 10), random.randint(0, constants.HEIGHT - 30)))
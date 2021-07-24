import pygame
import constants
import os

def load_pic(name, path="img/icons"):
    return pygame.image.load(os.path.join(path, name))

class Player(pygame.sprite.Sprite):

    def __init__(self, platforms):
        super().__init__()
        #self.surf = pygame.Surface((30, 30))
        #self.surf.fill((128, 255, 40))
        self.penguinRight = load_pic("penguinRight.png")
        self.penguinRight = pygame.transform.scale(self.penguinRight, (30, 30))
        
        self.penguinLeft = load_pic("penguinLeft.png")
        self.penguinLeft = pygame.transform.scale(self.penguinLeft, (30, 30))

        self.penguinJumpRight = load_pic("penguinJumpRight.png")
        self.penguinJumpRight = pygame.transform.scale(self.penguinJumpRight, (30, 30))

        self.penguinJumpLeft = load_pic("penguinJumpLeft.png")
        self.penguinJumpLeft = pygame.transform.scale(self.penguinJumpLeft, (30, 30))

        self.surf = self.penguinRight
        self.rect = self.surf.get_rect()

        self.pos = constants.vec((10, 385))
        self.vel = constants.vec(0, 0)
        self.acc = constants.vec(0, 0)

        self.platforms = platforms

        self.dir = "right"

    def move(self):
        self.acc = constants.vec(0, 0.5)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.acc.x = -constants.ACC
            self.dir = "left"
            if self.vel.y < 0:
                self.surf = self.penguinJumpLeft
            else:
                self.surf = self.penguinLeft
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.acc.x = constants.ACC
            self.dir = "right"
            if self.vel.y < 0:
                self.surf = self.penguinJumpRight
            else:
                self.surf = self.penguinRight
        if keys[pygame.K_SPACE]:
            self.jump()

        self.acc.x += self.vel.x * constants.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > constants.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = constants.WIDTH

        self.rect.midbottom = self.pos


    def jump(self):
        hits = pygame.sprite.spritecollide(self, self.platforms, False)

        if hits:
            self.vel.y = -15
            self.surf = self.penguinJumpRight
            

    def update(self):
        hits = pygame.sprite.spritecollide(self, self.platforms, False)

        if self.vel.y > 0:
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1
                if self.dir == "left":
                    self.surf = self.penguinLeft
                else:
                    self.surf = self.penguinRight
                
    
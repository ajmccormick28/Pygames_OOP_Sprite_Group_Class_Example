import pygame
import os
import canvas
import player
import platform
import constants
import random

# Main Game Class
class Game:

    def __init__(self, width = 400, height = 450):
        pygame.init()
        self.canvas = canvas.Canvas(constants.WIDTH, constants.HEIGHT)
        #self.vec = pygame.math.Vector2
        self.framesPerSec = pygame.time.Clock()
        self.platNumMin = 5
        self.platNumMax = 6

    def levelGen(self):

        for x in range(random.randint(self.platNumMin, self.platNumMax)):
            pl = platform.Platform()
            self.platforms.add(pl)
            self.allSprites.add(pl)

    def platformGen(self):
        while len(self.platforms) < self.platNumMax + 1:
            width = random.randrange(50, 100)
            p = platform.Platform()
            p.rect.center = (random.randrange(0, constants.WIDTH - width), random.randrange(-50, 0))
            self.platforms.add(p)
            self.allSprites.add(p)

    def run(self):
        running = True

        #Creating sprite groups
        self.platforms = pygame.sprite.Group()     
        self.allSprites = pygame.sprite.Group()

        # Setting up the base platform
        platform1 = platform.Platform()
        self.platforms.add(platform1)
        self.allSprites.add(platform1)
        platform1.surf = pygame.Surface((constants.WIDTH, 20))
        platform1.surf.fill("#C6DCF5")
        platform1.rect = platform1.surf.get_rect(center = (constants.WIDTH / 2, constants.HEIGHT - 10))
        
        self.levelGen() # Call to function level Gen

        # Creating the player sprite
        player1 = player.Player(self.platforms)
        self.allSprites.add(player1)

        # Main Game loop
        while running:
            # Button and key bindings 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            if player1.rect.top < constants.HEIGHT / 3:
                player1.pos.y += abs(player1.vel.y)

                for plat in self.platforms:
                    plat.rect.y += abs(player1.vel.y)

                    if plat.rect.top >= constants.HEIGHT:
                        plat.kill()


            player1.update()
            player1.move()
            self.platformGen()
                       

            self.canvas.drawBackground()

            # Drawing all sprites with the allSprite class group
            for entity in self.allSprites:
                self.canvas.getCanvas().blit(entity.surf, entity.rect)

            self.canvas.update()
            self.framesPerSec.tick(constants.FPS)

        pygame.quit()

if __name__ == "__main__":
    Game().run()
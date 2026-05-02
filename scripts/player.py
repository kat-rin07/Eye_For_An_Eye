import pygame
from scripts.settings import WIDTH, HEIGHT

class Pip(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.images = {
            'idle': pygame.image.load('assets/images/Pip_idle.png').convert_alpha(),
            'lefty': pygame.image.load('assets/images/Pip_lefty.png').convert_alpha(),
            'righty': pygame.image.load('assets/images/Pip_righty.png').convert_alpha(),

         }
        self.image = self.images['idle']
        self.rect = self.image.get_rect(center = position)
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        self.image = self.images['idle']

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]: #use keys to swap to left sprite
            self.speedx -= 5 #left
            self.image = self.images['lefty']

        elif keys[pygame.K_RIGHT]: #use keys to swap to right sprite
            self.speedx += 5 # right
            self.image = self.images['righty']

        #vertical movements
        if keys[pygame.K_UP]:
            self.speedy -= 5
        elif keys[pygame.K_DOWN]:
            self.speedy += 5


        self.rect.x += self.speedx
        self.rect.y += self.speedy


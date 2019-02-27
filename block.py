import pygame
from pygame.sprite import Sprite


class Block(Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('images/block.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

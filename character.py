import pygame


class Character():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('images/character.bmp')
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_up:
            self.rect.y -= self.ai_settings.CHARACTER_SPEED_FACTOR
        if self.moving_down:
            self.rect.y += self.ai_settings.CHARACTER_SPEED_FACTOR
        if self.moving_left:
            self.rect.x -= self.ai_settings.CHARACTER_SPEED_FACTOR
        if self.moving_right:
            self.rect.x += self.ai_settings.CHARACTER_SPEED_FACTOR

    def blitme(self):
        self.screen.blit(self.image, self.rect)

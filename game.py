import pygame
from pygame.sprite import Group

from settings import Settings
from character import Character
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    pygame.display.set_caption(ai_settings.TITLE)
    screen = pygame.display.set_mode((ai_settings.SCREEN_WIDTH, ai_settings.SCREEN_HEIGHT))
    character = Character(screen, ai_settings)
    blocks = Group()
    gf.create_blocks(blocks, screen)

    while True:
        gf.check_events(character, blocks)
        character.update()
        gf.update_screen(screen, ai_settings, character, blocks)


run_game()

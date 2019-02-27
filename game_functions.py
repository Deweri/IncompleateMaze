import sys

import pygame

from block import Block


def create_blocks(blocks, screen):
    blocks.add(Block(screen, 300, 300))


def check_keydown_events(event, character, blocks):
    if event.key == pygame.K_UP:
        character.moving_up = True
        for block in blocks:
            if character.rect.colliderect(block.rect):
                character.rect.top = block.rect.bottom
    elif event.key == pygame.K_DOWN:
        character.moving_down = True
        for block in blocks:
            if character.rect.colliderect(block.rect):
                character.rect.bottom = block.rect.top
    elif event.key == pygame.K_LEFT:
        character.moving_left = True
        for block in blocks:
            if character.rect.colliderect(block.rect):
                character.rect.left = block.rect.right
    elif event.key == pygame.K_RIGHT:
        character.moving_right = True
        for block in blocks:
            if character.rect.colliderect(block.rect):
                character.rect.right = block.rect.left


def check_keyup_events(event, character, blocks):
    if event.key == pygame.K_UP:
        character.moving_up = False
        for block in blocks:
            if character.rect.colliderect(block.rect):
                character.rect.top = block.rect.bottom
    elif event.key == pygame.K_DOWN:
        character.moving_down = False
        for block in blocks:
            if character.rect.colliderect(block.rect):
                character.rect.bottom = block.rect.top
    elif event.key == pygame.K_LEFT:
        character.moving_left = False
        for block in blocks:
            if character.rect.colliderect(block.rect):
                character.rect.left = block.rect.right
    elif event.key == pygame.K_RIGHT:
        character.moving_right = False
        for block in blocks:
            if character.rect.colliderect(block.rect):
                character.rect.right = block.rect.left



def check_events(character, blocks):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, character, blocks)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, character, blocks)


def update_screen(screen, ai_settings, character, blocks):
    screen.fill(ai_settings.SCREEN_COLOR)
    character.blitme()
    blocks.draw(screen)
    pygame.display.flip()

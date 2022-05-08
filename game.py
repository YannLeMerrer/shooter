from player import Player
import pygame

class Game:

    def __init__(self):
        self.player = Player(self)
        self.pressed = {}

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
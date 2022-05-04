import pygame


class Monster(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.health = 100
        self.maxhealth = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy.png')
        self.velocity = 1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        super().update()
        self.rect.x -= self.velocity
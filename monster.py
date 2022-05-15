import pygame


class Monster(pygame.sprite.Sprite):

    def __init__(self, x, y, player):
        super().__init__()
        self.health = 100
        self.maxhealth = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy.png')
        self.velocity = 1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player = player

    def update(self):
        super().update()
        if not pygame.sprite.collide_mask(self, self.player):
            self.rect.x -= self.velocity

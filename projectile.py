import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(image, (50, 50))
        self.velocity = 2.5
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        super().update()
        self.rect.x += self.velocity
        self.rotate()

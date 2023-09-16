import pygame


class Gun:

    def __init__(self, screen):

        self.screen = screen
        self.images = pygame.image.load('images/ship.png')
        self.rect = self.images.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        self.screen.blit(self.images, self.rect)

    def update_gun(self):
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.mleft and self.rect.left > 0:
            self.rect.centerx -= 1

import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.settings = settings
        self.screen = screen

        self.rect = pygame.Rect((0, 0), self.settings.alien_size)

        self.moving_left = False

    def update(self):
        if self.moving_left:
            self.rect.x -= self.settings.alien_moving_speed
        else:
            self.rect.x += self.settings.alien_moving_speed

    def draw_alien(self):
        self.screen.fill(self.settings.alien_color, self.rect)

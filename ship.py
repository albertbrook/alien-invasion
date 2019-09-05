import pygame


class Ship(object):
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.rect = pygame.Rect((0, 0), self.settings.ship_size)
        self.rect.center = self.screen.get_rect().center
        self.rect.bottom = self.screen.get_rect().bottom

        self.moving_left = False
        self.moving_right = False

    def update_ship(self):
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen.get_rect().right:
            self.rect.x += self.settings.ship_speed

    def draw_ship(self):
        self.screen.fill(self.settings.ship_color, self.rect)

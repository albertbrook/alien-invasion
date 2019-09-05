import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, settings, screen, ship):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.ship = ship

        self.rect = pygame.Rect((0, 0), self.settings.bullet_size)
        self.rect.center = self.ship.rect.center
        self.rect.top = self.ship.rect.top

    def update(self):
        self.rect.y -= self.settings.bullet_speed
        if self.rect.bottom < 0:
            self.kill()

    def draw_bullet(self):
        self.screen.fill(self.settings.bullet_color, self.rect)

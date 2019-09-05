import pygame


class Button(object):
    def __init__(self, settings, screen, message):
        self.settings = settings
        self.screen = screen

        self.rect = pygame.Rect((0, 0), self.settings.button_size)
        self.rect.center = self.screen.get_rect().center

        self.message_font = pygame.font.SysFont(None, self.settings.button_font_size)
        self.message_image = self.message_font.render(message, True, self.settings.button_font_color)
        self.message_rect = self.message_image.get_rect()
        self.message_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_rect)

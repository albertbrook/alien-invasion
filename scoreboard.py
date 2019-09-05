import pygame


class Scoreboard(object):
    def __init__(self, settings, stats, screen):
        self.settings = settings
        self.stats = stats
        self.screen = screen

        self.font = pygame.font.SysFont(None, self.settings.scoreboard_font_size)

    def draw_scoreboard(self):
        for ship_number in range(self.stats.ship_life):
            ship = pygame.Rect((0, 0), self.settings.ship_size)
            ship.left = (10 + ship.width) * ship_number
            ship.top = 0
            self.screen.fill(self.settings.ship_color, ship)

        high_score = "{:,}".format(int(round(self.stats.high_score, -1)))
        high_score_image = self.font.render(high_score, True, self.settings.scoreboard_font_color)
        high_score_rect = high_score_image.get_rect()
        high_score_rect.center = self.screen.get_rect().center
        high_score_rect.top = 0
        self.screen.blit(high_score_image, high_score_rect)

        score = "{:,}".format(int(round(self.stats.score, -1)))
        score_image = self.font.render(score, True, self.settings.scoreboard_font_color)
        score_rect = score_image.get_rect()
        score_rect.right = self.screen.get_rect().right
        score_rect.top = 0
        self.screen.blit(score_image, score_rect)

        level = "{:,}".format(self.stats.level)
        level_image = self.font.render(level, True, self.settings.scoreboard_font_color)
        level_rect = level_image.get_rect()
        level_rect.right = self.screen.get_rect().right
        level_rect.top = score_rect.bottom
        self.screen.blit(level_image, level_rect)

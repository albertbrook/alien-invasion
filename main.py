import pygame
from settings import Settings
from stats import Stats
from ship import Ship
from button import Button
from scoreboard import Scoreboard
from functions import Functions


class Game(object):
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.stats = Stats(self.settings)

        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self.settings, self.screen)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.button = Button(self.settings, self.screen, "Play")
        self.scoreboard = Scoreboard(self.settings, self.stats, self.screen)
        self.functions = Functions(self.settings, self.stats, self.screen,
                                   self.ship, self.bullets, self.aliens, self.button, self.scoreboard)

    def start(self):
        while True:
            pygame.time.Clock().tick(self.settings.frames_per_second)
            self.functions.check_events()
            if self.stats.game_active:
                self.functions.update_screen()
                self.functions.check_collide()
            self.functions.draw_screen()


if __name__ == '__main__':
    game = Game()
    game.start()

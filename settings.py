class Settings(object):
    def __init__(self):
        self.screen_size = (1280, 720)
        self.background_color = (0, 0, 0)
        self.frames_per_second = 120

        self.ship_size = (50, 50)
        self.ship_color = (0, 0, 255)
        self.ship_limit = 3

        self.bullet_size = (3, 15)
        self.bullet_color = (255, 255, 255)

        self.alien_size = (50, 50)
        self.alien_color = (255, 0, 0)
        self.alien_decline_speed = 10

        self.button_size = (200, 50)
        self.button_color = (0, 255, 0)
        self.button_font_size = 48
        self.button_font_color = (255, 255, 255)

        self.scoreboard_font_size = 48
        self.scoreboard_font_color = (255, 255, 255)

        self.spend_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 5
        self.bullet_speed = 5
        self.alien_moving_speed = 5
        self.alien_point = 50

    def increase_scale(self):
        self.ship_speed *= self.spend_scale
        self.bullet_speed *= self.spend_scale
        self.alien_moving_speed *= self.spend_scale
        self.alien_point *= self.score_scale

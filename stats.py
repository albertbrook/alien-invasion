class Stats(object):
    def __init__(self, settings):
        self.settings = settings

        self.game_active = False
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        self.ship_life = self.settings.ship_limit
        self.score = 0
        self.level = 1

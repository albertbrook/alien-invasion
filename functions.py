import pygame
from time import sleep
from bullet import Bullet
from alien import Alien


class Functions(object):
    def __init__(self, settings, stats, screen, ship, bullets, aliens, button, scoreboard):
        self.settings = settings
        self.stats = stats
        self.screen = screen
        self.ship = ship
        self.bullets = bullets
        self.aliens = aliens
        self.button = button
        self.scoreboard = scoreboard

    def check_events(self):
        self.ship.moving_left = True if pygame.key.get_pressed()[pygame.K_LEFT] else False
        self.ship.moving_right = True if pygame.key.get_pressed()[pygame.K_RIGHT] else False
        if not self.aliens:
            self.create_fleet()
        for event in pygame.event.get():
            self.judge_type(event)

    def create_fleet(self):
        alien = Alien(self.settings, self.screen)
        fleet_number_x = int((self.screen.get_rect().width - 5 * alien.rect.width) /
                             alien.rect.width)
        fleet_number_y = int((self.screen.get_rect().height - 5 * alien.rect.height - self.ship.rect.height) /
                             alien.rect.height)
        for fleet_row in range(0, fleet_number_y, 2):
            for fleet_col in range(0, fleet_number_x, 2):
                alien = Alien(self.settings, self.screen)
                alien.rect.left = alien.rect.width * fleet_col
                alien.rect.top = alien.rect.height * fleet_row
                alien.add(self.aliens)

    def judge_type(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.stats.game_active:
                bullet = Bullet(self.settings, self.screen, self.ship)
                bullet.add(self.bullets)
            elif event.key == pygame.K_p:
                self.play_game()
        elif event.type == pygame.MOUSEBUTTONDOWN and not self.stats.game_active:
            mouse_point = pygame.mouse.get_pos()
            if self.button.rect.collidepoint(mouse_point):
                self.play_game()

    def play_game(self):
        pygame.mouse.set_visible(False)
        self.stats.game_active = True
        self.stats.reset_stats()
        self.settings.initialize_dynamic_settings()

    def check_collide(self):
        for alien in pygame.sprite.groupcollide(self.bullets, self.aliens, True, True).values():
            self.kill_alien(alien)
        for alien in self.aliens:
            if alien.rect.left < 0 or alien.rect.right > self.screen.get_rect().right:
                self.change_direction()
                return
            if (alien.rect.bottom > self.screen.get_rect().bottom or
                    pygame.sprite.spritecollideany(self.ship, self.aliens)):
                self.life_die()
                return

    def kill_alien(self, alien):
        self.stats.score += self.settings.alien_point * len(alien)
        if self.stats.high_score < self.stats.score:
            self.stats.high_score = self.stats.score
        if not self.aliens:
            self.stats.level += 1
            self.bullets.empty()
            self.settings.increase_scale()

    def change_direction(self):
        for alien in self.aliens:
            alien.rect.top += self.settings.alien_decline_speed
            alien.moving_left = not alien.moving_left

    def life_die(self):
        self.stats.ship_life -= 1
        self.ship.rect.center = self.screen.get_rect().center
        self.ship.rect.bottom = self.screen.get_rect().bottom
        self.bullets.empty()
        self.aliens.empty()
        if self.stats.ship_life < 0:
            pygame.mouse.set_visible(True)
            self.stats.game_active = False
        sleep(0.5)

    def update_screen(self):
        self.ship.update_ship()
        self.bullets.update()
        self.aliens.update()

    def draw_screen(self):
        self.screen.fill(self.settings.background_color)
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.ship.draw_ship()
        for alien in self.aliens:
            alien.draw_alien()
        self.scoreboard.draw_scoreboard()
        if not self.stats.game_active:
            self.button.draw_button()
        pygame.display.flip()

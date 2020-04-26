import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for bullets shoot by ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create new bullet"""
        super(Bullet, self).__init__()
        self.screen = screen

        #Create bullet in point 0,0
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx       #Follow ship position
        self.rect.top = ship.rect.top

        #Position of bullet
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moving bullet"""
        self.y -= self.speed_factor     #bullet go up, so y values are going down
        self.rect.y = self.y

    def draw_bullet(self):
        """Show bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
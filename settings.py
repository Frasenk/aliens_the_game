
class Settings():
    """Game settings"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # alien speed

        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 1
        self.fleet_direction = 1        # moving fleet to right

        #  Bullet settings:

        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3



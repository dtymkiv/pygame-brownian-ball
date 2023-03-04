import pygame
import numpy as np


additions = {
	'left': 0,              # (0 -> 180 degrees)
	'top': 3/2 * np.pi,     # (270 -> 90 degrees)
	'right': np.pi,         # (180 -> 360 degrees)
	'bottom': 1/2 * np.pi   # (90 -> 270 degrees)
}


class Robot:
    def __init__(self, diameter, speed, options, direction=0):
        self.options = options
        self.diameter = diameter
        self.radius = diameter / 2
        self.speed = speed
        self.direction_x = np.sin(direction)
        self.direction_y = np.cos(direction)

        self.obj = pygame.Rect(
			self.options.screen_width / 2 - self.radius, 
			self.options.screen_height / 2 - self.radius, 
			diameter, 
			diameter
		)

    def change_direction(self, collided_side):
        addition = additions[collided_side]
        rand_direction = np.random.uniform(0, np.pi) + addition
        self.direction_x = np.sin(rand_direction)
        self.direction_y = np.cos(rand_direction)

    def check_collisions(self):
		
		# collision at the left side, make it bounce everywhere, except left
        if self.obj.x <= 0:
            self.change_direction('left')
		# collision at the top side, make it bounce everywhere, except top 
        elif self.obj.y <= 0:
            self.change_direction('top')
        # collision at the right side, make it bounce everywhere, except right 
        elif self.obj.x >= self.options.screen_width - self.diameter:
            self.change_direction('right')
        # collision at the bottom side, make it bounce everywhere, except bottom 
        elif self.obj.y >= self.options.screen_height - self.diameter:
            self.change_direction('bottom')

    def move(self):
        self.obj.x += self.direction_x * self.speed
        self.obj.y += self.direction_y * self.speed

        self.check_collisions()
	
    @property
    def new_frame(self):
        self.move()
        return self.obj

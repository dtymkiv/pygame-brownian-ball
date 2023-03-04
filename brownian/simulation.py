import pygame, sys

from brownian.robot import Robot
from brownian.options import Options


# Colors
light_grey = (200,200,200)
bg_color = pygame.Color('grey12')

class BrownianSimulation:
	def __init__(self, robot: Robot, options: Options) -> None:
		self.robot = robot
		self.options = options
		pygame.init()
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((options.screen_width, options.screen_height))
		pygame.display.set_caption('Brownian ball')
		     
	def start(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill(bg_color)
			pygame.draw.ellipse(self.screen, light_grey, self.robot.new_frame)

			pygame.display.flip()
			self.clock.tick(60)

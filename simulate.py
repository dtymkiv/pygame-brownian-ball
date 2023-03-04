from brownian.options import Options
from brownian.robot import Robot
from brownian.simulation import BrownianSimulation

options = Options(screen_height=600, screen_width=600)

robot = Robot(30, 7, options=options)

sim = BrownianSimulation(robot, options)
sim.start()
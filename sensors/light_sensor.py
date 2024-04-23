from swarmy.perception import Perception
import pygame
import math
import numpy as np

class LightIntensitySensor(Perception):
    def __init__(self, agent, environment, config):
        super().__init__(agent, environment)
        self.agent = agent
        self.environment = environment
        self.config = config

    def sensor(self):
        """ LightIntensitySensor returns a value between 0 and 1 representing the intensity of light at the agent's current position.
        Hints:
        - x,y,gamma = self.agent.get_position() # returns the current position of the robot
        - self.environment.get_light_intensity(x, y) # returns the light intensity at the given position
        """

        robot_position_x, robot_position_y, _ = self.agent.get_position()

        # Get the light intensity at the robot's current position
        light_intensity = self.environment.get_light_intensity(robot_position_x, robot_position_y)

        return light_intensity
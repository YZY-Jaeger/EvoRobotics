from swarmy.environment import Environment
import pygame
import numpy as np

class My_environment(Environment):
    def __init__(self, config):
        self.config = config
        super().__init__(config)

        self.light_dist_surface = self.calculate_light_surface()

        self.light_dist = self.defineLight()

    def calculate_light_surface(self):#calculate it once
            light_dist = self.defineLight()
            light_dist_normalized = (light_dist / light_dist.max() * 255).astype(np.uint8)  # Normalize to range 0-255
            return pygame.surfarray.make_surface(np.stack([light_dist_normalized]*3, axis=-1))  # Create a surface from the light distribution
        
    def add_static_rectangle_object(self):
        """
        Add static rectangle object to the environment such as walls or obstacles.
        Example:
            self.staticRectList.append(color, pygame.Rect(x, y, width, height), border_width))
        Returns:
        """


    def add_static_rectangle_object(self):
        """
        Add static rectangle object to the environment such as walls or obstacles.
        Example:
            self.staticRectList.append(color, pygame.Rect(x, y, width, height), border_width))
        Returns:
        """

        wall_thickness = 10  # Increase this value to make the walls thicker

        self.staticRectList.append(['BLACK', pygame.Rect(5, 5, self.config['world_width'] - wall_thickness, wall_thickness), wall_thickness])
        self.staticRectList.append(['BLACK', pygame.Rect(5, 5, wall_thickness, self.config['world_height'] - wall_thickness), wall_thickness])
        self.staticRectList.append(['BLACK', pygame.Rect(5, self.config['world_height'] - wall_thickness, self.config['world_width'] - wall_thickness, wall_thickness), wall_thickness])
        self.staticRectList.append(['BLACK', pygame.Rect(self.config['world_width'] - wall_thickness, 5, wall_thickness, self.config['world_height'] - wall_thickness), wall_thickness])

    def add_static_circle_object(self):
        """
        Add static circle object to the environment such as sources or sinks.
        Example:
            self.staticCircList.append([color, position, border_width, radius])
        Returns:
        """
        pass



    def set_background_color(self):
        """
        Set the background color of the environment.
        Example:
            self.displaySurface.fill(self.BACKGROUND_COLOR)
        Hint: It is possible to use the light distribution to set the background color.
        For displaying a light distribution you might find pygame.surfarray.make_surface and self.displaySurface.blit useful)
        Returns:
        """
        #self.displaySurface.blit(self.light_dist_surface, (0, 0))  # Draw the precalculated light distribution on the display surface
        self.displaySurface.fill(self.BACKGROUND_COLOR)
    ###  LIGHT DISTRIBUTION ###

    def defineLight(self):
        """
        Define the light distribution of the environment.
        Returns: 3 dimensional light distribution tuple (x,y,light_intensity)
        """

        
        light_source_position = np.array([self.config['world_width'] / 2, self.config['world_height'] / 2])
        max_light_intensity = 60  # Maximum light intensity at the source

        light_dist = np.zeros((self.config['world_width'], self.config['world_height']))

        for x in range(self.config['world_width']):
            for y in range(self.config['world_height']):
                distance = np.linalg.norm(np.array([x, y]) - light_source_position)
                light_dist[x, y] = max(0, max_light_intensity - distance/3)

        return light_dist
       

import random
import pygame

class Ball():

    def __init__(self, pos, size, color, radius):
        self.pos = pos
        self.size = size
        self.color = random.choice(color)
        self.radius = radius

        self.surface = self.update_surface()

    def update_surface(self):
        x, y, = self.pos
        y += self.size
        self.pos = (x,y)

        surf = pygame.Surface((self.radius * 1.2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surf, self.color, (x, y), self.size*0.8)
        return surf


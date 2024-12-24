import pygame
import random
from settings import *

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn([])

    def spawn(self, snake_positions):
        while True:
            x = random.randint(0, (WINDOW_WIDTH-GRID_SIZE)//GRID_SIZE) * GRID_SIZE
            y = random.randint(0, (WINDOW_HEIGHT-GRID_SIZE)//GRID_SIZE) * GRID_SIZE
            self.position = (x, y)
            if self.position not in snake_positions:
                break

    def draw(self, screen):
        pygame.draw.rect(screen, RED, 
                        (self.position[0], self.position[1], GRID_SIZE-1, GRID_SIZE-1))
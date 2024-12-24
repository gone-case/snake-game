import pygame
from settings import *

class Snake:
    def __init__(self):
        self.positions = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
        self.direction = 'RIGHT'
        self.grow_pending = False
        
    def change_direction(self, new_direction):
        opposite_directions = {
            'UP': 'DOWN',
            'DOWN': 'UP',
            'LEFT': 'RIGHT',
            'RIGHT': 'LEFT'
        }
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

    def move(self):
        head_x, head_y = self.positions[0]
        if self.direction == 'UP':
            new_head = (head_x, head_y - GRID_SIZE)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + GRID_SIZE)
        elif self.direction == 'LEFT':
            new_head = (head_x - GRID_SIZE, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + GRID_SIZE, head_y)
            
        self.positions.insert(0, new_head)
        if not self.grow_pending:
            self.positions.pop()
        else:
            self.grow_pending = False

    def grow(self):
        self.grow_pending = True

    def get_head_position(self):
        return self.positions[0]

    def check_collision(self):
        return self.get_head_position() in self.positions[1:]

    def is_within_bounds(self, width, height):
        x, y = self.get_head_position()
        return 0 <= x < width and 0 <= y < height

    def draw(self, screen):
        for position in self.positions:
            pygame.draw.rect(screen, GREEN, 
                           (position[0], position[1], GRID_SIZE-1, GRID_SIZE-1))
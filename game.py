import pygame
import sys
from snake import Snake
from food import Food
from game_state import GameState
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        self.snake = Snake()
        self.food = Food()
        self.game_state = GameState()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction('RIGHT')

    def update(self):
        if not self.game_state.game_over:
            self.snake.move()
            # Check collision with food
            if self.snake.get_head_position() == self.food.position:
                self.snake.grow()
                self.food.spawn(self.snake.positions)
                self.game_state.increase_score()
            # Check collision with walls or self
            elif (self.snake.check_collision() or 
                  not self.snake.is_within_bounds(WINDOW_WIDTH, WINDOW_HEIGHT)):
                self.game_state.game_over = True

    def draw(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.game_state.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(GAME_SPEED)

if __name__ == '__main__':
    game = Game()
    game.run()
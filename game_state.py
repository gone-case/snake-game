import pygame
from settings import *

class GameState:
    def __init__(self):
        self.score = 0
        self.game_over = False
        self.font = pygame.font.Font(None, 36)

    def increase_score(self):
        self.score += 1

    def draw(self, screen):
        score_text = self.font.render(f'Score: {self.score}', True, WHITE)
        screen.blit(score_text, (10, 10))
        
        if self.game_over:
            game_over_text = self.font.render('Game Over!', True, WHITE)
            text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
            screen.blit(game_over_text, text_rect)
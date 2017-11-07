import pygame
from src.GameStates import GameStates

from src.State import State


class StartScreen(State):
    def run(self):
        background = pygame.image.load('media/start-background.bmp')
        self.display.blit(background, (0, 0))
        pygame.display.update()

        time = 0
        while True:
            time += self.clock.tick(self.FPS)
            if time > 1200:
                return GameStates.MENU

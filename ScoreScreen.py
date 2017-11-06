import pygame
from GameStates import GameStates


class ScoreScreen:
    def __init__(self, display, clock):
        self.clock = clock
        self.display = display

    def run(self):
        font = pygame.font.SysFont(None, 48)
        text = font.render('Game Over!', True, (255, 0, 0))

        time = 0
        while True:
            self.display.blit(text,)

            time += self.clock.tick(self.FPS)
            if time > 3000:
                return GameStates.EXIT
            pygame.display.update()
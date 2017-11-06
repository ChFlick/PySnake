import pygame
from GameStates import GameStates
from State import State


class StartScreen(State):
    def run(self):
        font = pygame.font.SysFont(None, 48)
        text = font.render('Welcome to Snake', True, (255, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = self.display.get_size()[0] / 2
        textrect.centery = self.display.get_size()[1] / 2

        self.display.blit(text, textrect)
        pygame.display.update()

        time = 0
        while True:
            time += self.clock.tick(self.FPS)
            if time > 3000:
                return GameStates.GAME

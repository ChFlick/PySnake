import pygame
from GameStates import GameStates
from State import State


class StartScreen(State):
    def run(self):
        self.display.fill((195,195,195))
        font = pygame.font.SysFont("Garamond", 100, bold=True)
        text = font.render('Snake', True, (54,54,54))
        textrect = text.get_rect()
        textrect.centerx = self.display.get_size()[0] / 2
        textrect.centery = 100

        self.display.blit(text, textrect)
        pygame.display.update()

        time = 0
        while True:
            time += self.clock.tick(self.FPS)
            if time > 1200:
                return GameStates.MENU

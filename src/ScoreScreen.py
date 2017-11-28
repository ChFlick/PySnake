import pygame
from src.GameStates import GameStates
from src.State import State


class ScoreScreen(State):
    def __init__(self, display, clock, gamedata):
        State.__init__(self, display, clock)
        self.gamedata = gamedata

        self.initResources()

    def initResources(self):
        self.defaultFont = pygame.font.SysFont("Garamond", 48)

    def run(self):
        text = self.defaultFont.render('Game Over!', True, (255, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = self.display.get_size()[0] / 2
        textrect.centery = 100
        self.display.blit(text, textrect)

        text = self.defaultFont.render('Score: ' + str(self.gamedata["score"]), True, (255, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = self.display.get_size()[0] / 2
        textrect.centery = 150
        self.display.blit(text, textrect)

        pygame.display.update()

        time = 0
        while True:
            time += self.clock.tick(self.FPS)
            if time > 3000:
                return GameStates.MENU

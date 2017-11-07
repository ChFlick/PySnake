from GameStates import GameStates
from Map import Map

import pygame
from pygame.locals import *

from Player import Player, Direction
from State import State


class MenuState:
    def __init__(self, text, gameState):
        self.text = text
        self.gameState = gameState


class Menu(State):
    MENU_STATES = [
        MenuState("Play", GameStates.GAME),
        MenuState("Quit", GameStates.EXIT)
    ]

    def __init__(self, display, clock):
        State.__init__(self, display, clock)

        self.selectedId = 0

    def run(self):
        headlinefont = pygame.font.SysFont("Garamond", 60, bold=True)
        headline = headlinefont.render('Main Menu', True, (54,54,54))
        headlinerect = headline.get_rect()
        headlinerect.centerx = self.display.get_size()[0] / 2
        headlinerect.centery = 50

        selectedFont = pygame.font.SysFont("Garamond", 48, bold=True)
        defaultFont = pygame.font.SysFont("Garamond", 48)

        while True:
            state = self.handleEvents()
            if state is not None:
                return state

            self.display.fill((195, 195, 195))
            self.display.blit(headline, headlinerect)

            for i in range(len(self.MENU_STATES)):
                text = None
                if self.selectedId == i:
                    text = selectedFont.render(self.MENU_STATES[i].text, True, (54,54,54))
                else:
                    text = defaultFont.render(self.MENU_STATES[i].text, True, (54,54,54))
                textrect = text.get_rect()
                textrect.centerx = self.display.get_size()[0] / 2
                textrect.centery = 120 + 50 * i
                self.display.blit(text, textrect)

            pygame.display.update()
            self.display.fill((0, 0, 0))

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return GameStates.EXIT
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    self.selectedId -= 1
                    if self.selectedId == -1:
                        self.selectedId = len(self.MENU_STATES) - 1
                elif event.key == K_DOWN:
                    self.selectedId += 1
                    if self.selectedId == len(self.MENU_STATES):
                        self.selectedId = 0
                elif event.key == K_RETURN:
                    return self.MENU_STATES[self.selectedId].gameState
                elif event.key == K_ESCAPE:
                    return GameStates.EXIT

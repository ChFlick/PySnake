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
        selectedFont = pygame.font.SysFont("Garamond", 48, bold=True)
        defaultFont = pygame.font.SysFont("Garamond", 48)

        background = pygame.image.load('media/menu-background.bmp')

        while True:
            state = self.handleEvents()
            if state is not None:
                return state

            self.display.fill((195, 195, 195))
            self.display.blit(background, (0,0))

            for i in range(len(self.MENU_STATES)):
                text = None
                if self.selectedId == i:
                    text = selectedFont.render(self.MENU_STATES[i].text, True, (54,54,54))
                else:
                    text = defaultFont.render(self.MENU_STATES[i].text, True, (54,54,54))
                textrect = text.get_rect()
                textrect.centerx = self.display.get_size()[0] / 2
                textrect.centery = 160 + 50 * i
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

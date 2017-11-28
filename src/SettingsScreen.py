from src.GameStates import GameStates

import pygame
from pygame.locals import *

from src.Settings import SettingNames, getSettingForName
from src.State import State


class SettingsScreen(State):
    MENU_STATES = SettingNames.PUBLIC_SETTINGS + ["Back"]

    def __init__(self, display, clock):
        State.__init__(self, display, clock)

        self.selectedId = 0

        self.initResources()

    def initResources(self):
        self.selectedFont = pygame.font.SysFont("Garamond", 48, bold=True)
        self.defaultFont = pygame.font.SysFont("Garamond", 48)

        self.background = pygame.image.load('media/menu-background.bmp').convert()

    def run(self):
        self.clearDisplay()

        while True:
            state = self.handleEvents()
            if state is not None:
                return state

            self.draw()

    def draw(self):
        for i in range(len(self.MENU_STATES)):
            setting = getSettingForName(self.MENU_STATES[i])
            text = None
            if setting is None:
                text = self.MENU_STATES[i]
            else:
                text = str(setting)

            renderedText = None
            if self.selectedId == i:
                renderedText = self.selectedFont.render(text, True, (54, 54, 54))
            else:
                renderedText = self.defaultFont.render(text, True, (54, 54, 54))

            textrect = renderedText.get_rect()
            textrect.centerx = self.display.get_size()[0] / 2
            textrect.centery = 160 + 50 * i
            self.display.blit(renderedText, textrect)

        self.clearDisplay()

    def clearDisplay(self):
        pygame.display.update()
        self.display.fill((195, 195, 195))
        self.display.blit(self.background, (0, 0))

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
                elif event.key == K_RETURN and self.selectedId == len(self.MENU_STATES) - 1:
                    return GameStates.MENU
                elif event.key == K_ESCAPE:
                    return GameStates.MENU
                elif event.key == K_LEFT:
                    setting = getSettingForName(self.MENU_STATES[self.selectedId])
                    if setting is not None:
                        setting.reduceVal()
                elif event.key == K_RIGHT:
                    setting = getSettingForName(self.MENU_STATES[self.selectedId])
                    if setting is not None:
                        setting.increaseVal()

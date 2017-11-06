from GameStates import GameStates
from Map import Map

import pygame
from pygame.locals import *

from Player import Player, Direction


class Game:
    FPS = 10

    def __init__(self, display, clock):
        self.clock = clock
        self.display = display

        self.player = Player()
        self.map = Map(self.player)

    def run(self):
        time = 0
        while True:
            state = self.handleEvents()
            if state != GameStates.GAME:
                return state

            self.player.update()

            time += self.clock.tick(self.FPS)
            if time > 500:
                self.player.move(self.map)
                self.map.update()
                if self.player.checkDeath():
                    return GameStates.SCORE
                time = 0

            self.map.draw(self.display)
            pygame.display.update()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return GameStates.EXIT
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return GameStates.EXIT

        return GameStates.GAME

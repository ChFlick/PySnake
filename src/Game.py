import pygame
from src.GameStates import GameStates
from src.Map import Map
from src.Player import Player
from pygame.locals import *

from src.State import State


class Game(State):
    SPEED = 500

    def __init__(self, display, clock):
        State.__init__(self, display, clock)

        self.player = Player()
        self.map = Map(self.player)
        self.forwardData = {}

    def run(self):
        time = 0
        while True:
            state = self.handleEvents()
            if state != GameStates.GAME:
                return state

            self.player.update()

            time += self.clock.tick(self.FPS)
            if time > self.SPEED:
                self.player.move(self.map)
                self.map.update()
                if self.player.checkDeath():
                    self.forwardData["score"] = self.player.score
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
                    return GameStates.MENU

        return GameStates.GAME

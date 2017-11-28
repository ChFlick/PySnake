import pygame
from pygame.locals import *

from src.GameStates import GameStates
from src.State import State
from src.game.Map import Map
from src.game.Player import Player


class Game(State):
    SPEED = 500

    def __init__(self, display, clock):
        State.__init__(self, display, clock)

        self.player = Player()
        self.map = Map(self.player)
        self.forwardData = {}

    def run(self):
        life = pygame.image.load('media/life.png').convert()
        life.set_colorkey((0, 255, 0))

        scoreFont = pygame.font.SysFont("Consolas", 25)

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
                if self.player.isDead():
                    self.forwardData["score"] = self.player.score
                    return GameStates.SCORE
                time = 0

            self.map.draw(self.display)

            for i in range(self.player.lives):
                self.display.blit(life, (27 * i, 0))

            scoreText = scoreFont.render(str(self.player.score), True, (255,0,0))
            self.display.blit(scoreText, (self.display.get_size()[0] - 25, 0))

            pygame.display.update()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return GameStates.EXIT
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return GameStates.MENU

        return GameStates.GAME

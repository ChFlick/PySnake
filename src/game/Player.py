import pygame

from src.Settings import SettingNames, getSettingForName
from src.game.Map import Map


class Direction:
    LEFT = 'LEFT'
    UP = 'UP'
    RIGHT = 'RIGHT'
    DOWN = 'DOWN'


class Player:
    def __init__(self):
        self.previousDirection = Direction.LEFT
        self.direction = Direction.RIGHT
        self.posX = 10
        self.posY = 10
        self.tail = [[9, 10],[8, 10], [7, 10], [6, 10]]
        self.score = 0
        self.lives = getSettingForName(SettingNames.LIVES).val

    def setDirection(self, direction):
        if (direction == Direction.LEFT or direction == Direction.RIGHT) and (self.previousDirection != Direction.LEFT and self.previousDirection != Direction.RIGHT) or \
                (direction == Direction.UP or direction == Direction.DOWN) and (self.previousDirection != Direction.UP and self.previousDirection != Direction.DOWN):
            self.direction = direction

    def move(self, map):
        posXnew, posYnew = self.getNextPosition(self.posX, self.posY)

        if map.isFood(posXnew, posYnew):
            self.eat()

        self.moveTail()

        self.posX = posXnew
        self.posY = posYnew
        self.previousDirection = self.direction

        self.checkWound()

    def moveTail(self):
        for i in reversed(range(len(self.tail))):
            if i > 0:
                self.tail[i] = self.tail[i - 1]
        self.tail[0] = [self.posX, self.posY]

    def getNextPosition(self, posX, posY):
        posXnew, posYnew = posX, posY

        if self.direction == Direction.RIGHT:
            posXnew = posX + 1 if posX < Map.SIZE_X - 1 else 0
        elif self.direction == Direction.LEFT:
            posXnew = posX - 1 if posX > 0 else Map.SIZE_X - 1
        elif self.direction == Direction.UP:
            posYnew = posY - 1 if posY > 0 else Map.SIZE_Y - 1
        elif self.direction == Direction.DOWN:
            posYnew = posY + 1 if posY < Map.SIZE_Y - 1 else 0

        return posXnew, posYnew

    def isDead(self):
        return self.lives == 0

    def checkWound(self):
        for tailElement in self.tail:
            if tailElement[0] == self.posX and tailElement[1] == self.posY:
                self.lives -= 1
                self.tail = self.tail[:self.tail.index(tailElement)]
                return

    def eat(self):
        self.tail.append(self.tail[len(self.tail) - 1])
        self.score += 1

    def update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.setDirection(Direction.LEFT)
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.setDirection(Direction.UP)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.setDirection(Direction.RIGHT)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.setDirection(Direction.DOWN)

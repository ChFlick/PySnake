import pygame


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
        self.tail = [[9, 10],[8, 10]]
        self.score = 0

    def setDirection(self, direction):
        if (direction == Direction.LEFT or direction == Direction.RIGHT) and (self.previousDirection != Direction.LEFT and self.previousDirection != Direction.RIGHT) or \
                (direction == Direction.UP or direction == Direction.DOWN) and (self.previousDirection != Direction.UP and self.previousDirection != Direction.DOWN):
            self.direction = direction

    def move(self, map):
        posXnew = self.posX
        posYnew = self.posY

        if self.direction == Direction.RIGHT:
            posXnew = posXnew + 1 if posXnew < map.SIZE_X - 1 else 0
        elif self.direction == Direction.LEFT:
            posXnew = posXnew - 1 if posXnew > 0 else map.SIZE_X - 1
        elif self.direction == Direction.UP:
            posYnew = posYnew - 1 if posYnew > 0 else map.SIZE_Y - 1
        elif self.direction == Direction.DOWN:
            posYnew = posYnew + 1 if posYnew < map.SIZE_Y - 1 else 0

        if map.isFood(posXnew, posYnew):
            self.eat()

        for i in reversed(range(len(self.tail))):
            if i > 0:
                self.tail[i] = self.tail[i - 1]

        self.tail[0] = [self.posX, self.posY]

        self.posX = posXnew
        self.posY = posYnew

        self.previousDirection = self.direction

    def checkDeath(self):
        dead = False
        for x in self.tail:
            dead = dead or x[0] == self.posX and x[1] == self.posY
        return dead

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

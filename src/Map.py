from random import randint

import pygame

#TODO add Unit test

class Tile:
    def __init__(self, id, color):
        self.id = id
        self.color = color


class Tiles:
    EMPTY = Tile(0, (255, 255, 255))
    PLAYER = Tile(1, (0, 102, 0))
    PLAYER_HEAD = Tile(2, (0, 153, 0))
    FOOD = Tile(3, (255, 0, 0))

    WIDTH = 25
    HEIGHT = 25
    GAP = 2


class Map:
    SIZE_X = 20
    SIZE_Y = 20

    def __init__(self, player):
        self.grid = [[Tiles.EMPTY for x in range(self.SIZE_X)] for y in range(self.SIZE_Y)]

        self.player = player

        self.grid[player.posX][player.posY] = Tiles.PLAYER_HEAD
        for pos in player.tail:
            self.grid[pos[0]][pos[1]] = Tiles.PLAYER

        self.spawnFood()

    def update(self):#
        hasFood = False
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[x][y] == Tiles.PLAYER or self.grid[x][y] == Tiles.PLAYER_HEAD:
                    self.grid[x][y] = Tiles.EMPTY

                hasFood = hasFood or self.grid[x][y] == Tiles.FOOD

        if not hasFood:
            self.spawnFood()

        self.grid[self.player.posX][self.player.posY] = Tiles.PLAYER_HEAD
        for pos in self.player.tail:
            self.grid[pos[0]][pos[1]] = Tiles.PLAYER

    def draw(self, display):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                rect = pygame.Rect(x * Tiles.WIDTH + x * Tiles.GAP, y * Tiles.HEIGHT + y * Tiles.GAP, Tiles.WIDTH, Tiles.HEIGHT)
                pygame.draw.rect(display, self.grid[x][y].color, rect)

    def isFood(self, x, y):
        return self.grid[x][y] == Tiles.FOOD

    def spawnFood(self):
        foodX = randint(0, self.SIZE_X - 1)
        foodY = randint(0, self.SIZE_Y - 1)

        while self.grid[foodX][foodY] != Tiles.EMPTY:
            foodX = randint(0, self.SIZE_X - 1)
            foodY = randint(0, self.SIZE_Y - 1)

        self.grid[foodX][foodY] = Tiles.FOOD

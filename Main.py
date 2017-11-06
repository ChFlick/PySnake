import pygame

from GameStates import GameStates
from ScoreScreen import ScoreScreen
from StartScreen import StartScreen
from Game import Game


def main():
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 640

    pygame.init()
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("SnakeClone")

    clock = pygame.time.Clock()

    state = GameStates.START

    while state != GameStates.EXIT:
        if state == GameStates.GAME:
            state = Game(display, clock).run()
        elif state == GameStates.SCORE:
            state = ScoreScreen(display, clock).run()
        elif state == GameStates.START:
            state = StartScreen(display, clock).run()


if __name__ == "__main__":
    main()
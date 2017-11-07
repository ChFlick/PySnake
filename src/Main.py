import pygame

from src.GameStates import GameStates
from src.Menu import Menu
from src.ScoreScreen import ScoreScreen
from src.StartScreen import StartScreen
from src.game.Game import Game


def main():
    WINDOW_WIDTH = 540
    WINDOW_HEIGHT = 540

    pygame.init()
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("SnakeClone")

    clock = pygame.time.Clock()

    state = GameStates.START
    gamedata = None

    while state != GameStates.EXIT:
        display.fill((0, 0, 0))

        if state == GameStates.GAME:
            game = Game(display, clock)
            state = game.run()
            gamedata = game.forwardData
        elif state == GameStates.MENU:
            state = Menu(display, clock).run()
        elif state == GameStates.SCORE:
            state = ScoreScreen(display, clock, gamedata).run()
        elif state == GameStates.START:
            state = StartScreen(display, clock).run()


if __name__ == "__main__":
    main()
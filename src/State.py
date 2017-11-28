from abc import ABCMeta, abstractmethod


class State:
    __metaclass__ = ABCMeta
    FPS = 60

    def __init__(self, display, clock):
        self.clock = clock
        self.display = display

    @abstractmethod
    def run(self):
        pass

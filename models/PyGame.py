import random
import pygame


class PyGame:

    @staticmethod
    def event_exit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def __init__(self, width=1280, height=720, fps=60, background="black"):
        pygame.init()

        self.screen = pygame.display.set_mode((width, height))
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.background = background

    def game_run(self, function):
        while not self.event_exit():
            self.screen.fill(self.background)

            function()

            pygame.display.flip()
            self.clock.tick(self.fps)
        pygame.quit()

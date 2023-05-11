import pygame
from config import Config


class Square:
    def __init__(self, index, file, rank):
        self.index = index
        color = (file + rank) % 2
        self.file = file
        self.rank = rank
        self.color = (194, 172, 141) if color == 0 else (129, 80, 33)
        x = Config.SQUARE_SIZE * file
        y = Config.SQUARE_SIZE * rank
        self.rect = pygame.Rect(x, y, Config.SQUARE_SIZE, Config.SQUARE_SIZE)
        self.figure = None

    def place_figure(self):
        pass

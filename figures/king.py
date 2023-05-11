import pygame
import os

from config import Config
from figures.figure import Figure


class King(Figure):
    def __init__(self, pos_x, pos_y, color, rank):
        super().__init__(pos_x, pos_y, color, rank)
        self.image = pygame.image.load(
            os.path.join("assets", "figures", f"{color}_king.png")
        )
        self.image = pygame.transform.scale(self.image, (Config.SQUARE_SIZE, Config.SQUARE_SIZE))

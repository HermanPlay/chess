import pygame
import os

from config import Config
from figures.figure import Figure


class Knight(Figure):
    def __init__(self, pos_x, pos_y, color, rank):
        super().__init__(pos_x, pos_y, color, rank)
        asset_color = "white" if color else "black"
        self.image = pygame.image.load(
            os.path.join("assets", "figures", f"{asset_color}_knight.png")
        )
        self.image = pygame.transform.scale(
            self.image, (Config.SQUARE_SIZE, Config.SQUARE_SIZE)
        )

    def get_possible_moves(self, board):
        possible_moves = []
        attacking_moves = []

        moves = ((-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2))

        for move in moves:
            new_x = self.pos_x + move[0]
            new_y = self.pos_y + move[1]
            possible_move = new_x + new_y * 8
            if new_x < 0 or new_x > 7 or new_y < 0 or new_y > 7:
                continue
            if board.squares[possible_move].figure is None:
                possible_moves.append(board.squares[possible_move])
            elif board.squares[possible_move].figure.color != self.color:
                attacking_moves.append(board.squares[possible_move])

        return (possible_moves, attacking_moves)

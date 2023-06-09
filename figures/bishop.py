import pygame
import os

from config import Config
from figures.figure import Figure


class Bishop(Figure):
    def __init__(self, pos_x, pos_y, color, rank):
        super().__init__(pos_x, pos_y, color, rank)
        asset_color = "white" if color else "black"
        self.image = pygame.image.load(
            os.path.join("assets", "figures", f"{asset_color}_bishop.png")
        )
        self.image = pygame.transform.scale(
            self.image, (Config.SQUARE_SIZE, Config.SQUARE_SIZE)
        )

    def get_possible_moves(self, board):
        possible_moves = []
        attacking_moves = []

        # TODO: Shorten this code
        moves_right = (9, -7)
        moves_left = (7, -9)

        for i in range(2):
            possible_move = self.pos_x + self.pos_y * 8
            for j in range(self.pos_x):
                possible_move += moves_left[i]
                if possible_move < 0 or possible_move > 63:
                    break
                if board.squares[possible_move].figure is None:
                    possible_moves.append(board.squares[possible_move])
                elif board.squares[possible_move].figure.color != self.color:
                    attacking_moves.append(board.squares[possible_move])
                    break
                else:
                    break
        for i in range(2):
            possible_move = self.pos_x + self.pos_y * 8
            for j in range(7 - self.pos_x):
                possible_move += moves_right[i]
                if possible_move < 0 or possible_move > 63:
                    break
                if board.squares[possible_move].figure is None:
                    possible_moves.append(board.squares[possible_move])
                elif board.squares[possible_move].figure.color != self.color:
                    attacking_moves.append(board.squares[possible_move])
                    break
                else:
                    break

        return (possible_moves, attacking_moves)

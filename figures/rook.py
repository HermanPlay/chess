import pygame
import os

from config import Config
from figures.figure import Figure


class Rook(Figure):
    def __init__(self, pos_x, pos_y, color, rank):
        super().__init__(pos_x, pos_y, color, rank)
        self.image = pygame.image.load(
            os.path.join("assets", "figures", f"{color}_rook.png")
        )
        self.image = pygame.transform.scale(
            self.image, (Config.SQUARE_SIZE, Config.SQUARE_SIZE)
        )
        self.first_move = True

    def get_possible_moves(self, board):
        possible_moves = []
        attacking_moves = []

        for y in range(self.pos_y + 1, 8):
            if y == 8:
                break
            possible_move = self.pos_x + y * 8
            if board.squares[possible_move].figure is None:
                possible_moves.append(board.squares[possible_move])
            elif board.squares[possible_move].figure.color != self.color:
                attacking_moves.append(board.squares[possible_move])
                break
            else:
                break
        for y in range(self.pos_y - 1, -1, -1):
            possible_move = self.pos_x + y * 8
            if board.squares[possible_move].figure is None:
                possible_moves.append(board.squares[possible_move])
            elif board.squares[possible_move].figure.color != self.color:
                attacking_moves.append(board.squares[possible_move])
                break
            else:
                break
        for x in range(self.pos_x + 1, 8):
            if x == 8:
                break
            possible_move = x + self.pos_y * 8
            if board.squares[possible_move].figure is None:
                possible_moves.append(board.squares[possible_move])
            elif board.squares[possible_move].figure.color != self.color:
                attacking_moves.append(board.squares[possible_move])
                break
            else:
                break
        for x in range(self.pos_x - 1, -1, -1):
            possible_move = x + self.pos_y * 8
            if board.squares[possible_move].figure is None:
                possible_moves.append(board.squares[possible_move])
            elif board.squares[possible_move].figure.color != self.color:
                attacking_moves.append(board.squares[possible_move])
                break
            else:
                break

        return (possible_moves, attacking_moves)

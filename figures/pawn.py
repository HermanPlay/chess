import os
import pygame

from config import Config
from figures.figure import Figure


class Pawn(Figure):
    def __init__(self, pos_x, pos_y, color, rank):
        super().__init__(pos_x, pos_y, color, rank)
        self.image = pygame.image.load(
            os.path.join("assets", "figures", f"{color}_pawn.png")
        )
        self.image = pygame.transform.scale(
            self.image, (Config.SQUARE_SIZE, Config.SQUARE_SIZE)
        )
        self.first_move = True

    def get_possible_moves(self, board):
        possible_moves = []
        attacking_moves = []

        moves = [1]
        kill_moves = [-1, 1]
        if self.first_move:
            moves.append(2)
        if self.color == "white":
            for move in moves:
                possible_move = self.pos_x + (self.pos_y - move) * 8
                if possible_move < 0 or possible_move > 63:
                    continue
                if board.squares[possible_move].figure is None:
                    possible_moves.append(board.squares[possible_move])
            for move in kill_moves:
                possible_move = self.pos_x + move + (self.pos_y - 1) * 8
                if possible_move < 0 or possible_move > 63:
                    continue
                if board.squares[possible_move].figure:
                    if board.squares[possible_move].figure.color != self.color:
                        attacking_moves.append(board.squares[possible_move])
        else:
            for move in moves:
                possible_move = self.pos_x + (self.pos_y + move) * 8
                if possible_move < 0 or possible_move > 63:
                    continue
                if board.squares[possible_move].figure is None:
                    possible_moves.append(board.squares[possible_move])
            for move in kill_moves:
                possible_move = self.pos_x + move + (self.pos_y + 1) * 8
                if possible_move < 0 or possible_move > 63:
                    continue
                if board.squares[possible_move].figure:
                    if board.squares[possible_move].figure.color != self.color:
                        attacking_moves.append(board.squares[possible_move])
        return (possible_moves, attacking_moves)

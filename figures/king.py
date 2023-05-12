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
        self.image = pygame.transform.scale(
            self.image, (Config.SQUARE_SIZE, Config.SQUARE_SIZE)
        )

        self.first_move = True

    def get_possible_moves(self, board):
        possible_moves = []
        attacking_moves = []

        moves = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))

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

    def get_castling(self, board):
        possible_moves = []
        if self.first_move:
            if board.squares[self.pos_x - 4 + self.pos_y * 8].figure:
                if board.squares[self.pos_x - 4 + self.pos_y * 8].figure.rank == 5:
                    if board.squares[self.pos_x - 4 + self.pos_y * 8].figure.first_move:
                        if (
                            not board.squares[self.pos_x - 3 + self.pos_y * 8].figure
                            and not board.squares[
                                self.pos_x - 2 + self.pos_y * 8
                            ].figure
                            and not board.squares[
                                self.pos_x - 1 + self.pos_y * 8
                            ].figure
                        ):
                            possible_moves.append(
                                board.squares[self.pos_x - 2 + self.pos_y * 8]
                            )

            if board.squares[self.pos_x + 3 + self.pos_y * 8].figure:
                if board.squares[self.pos_x + 3 + self.pos_y * 8].figure.rank == 5:
                    if board.squares[self.pos_x + 3 + self.pos_y * 8].figure.first_move:
                        if (
                            not board.squares[self.pos_x + 2 + self.pos_y * 8].figure
                            and not board.squares[
                                self.pos_x + 1 + self.pos_y * 8
                            ].figure
                        ):
                            possible_moves.append(
                                board.squares[self.pos_x + 2 + self.pos_y * 8]
                            )
        return possible_moves

    def castle(self, move, board):
        if move.file == self.pos_x - 2:
            # move rook
            board.squares[self.pos_x - 4 + self.pos_y * 8].figure.pos_x = self.pos_x - 1
            board.squares[self.pos_x - 1 + self.pos_y * 8].figure = board.squares[
                self.pos_x - 4 + self.pos_y * 8
            ].figure
            board.squares[self.pos_x - 4 + self.pos_y * 8].figure = None
            board.squares[self.pos_x - 1 + self.pos_y * 8].figure.first_move = False

            # move king
            board.squares[self.pos_x + self.pos_y * 8].figure = None
            self.pos_x = move.file
            board.squares[self.pos_x + self.pos_y * 8].figure = self
            self.first_move = False
        else:
            # move rook
            board.squares[self.pos_x + 3 + self.pos_y * 8].figure.pos_x = self.pos_x + 1
            board.squares[self.pos_x + 1 + self.pos_y * 8].figure = board.squares[
                self.pos_x + 3 + self.pos_y * 8
            ].figure
            board.squares[self.pos_x + 3 + self.pos_y * 8].figure = None
            board.squares[self.pos_x + 1 + self.pos_y * 8].figure.first_move = False

            # move king
            board.squares[self.pos_x + self.pos_y * 8].figure = None
            self.pos_x = move.file
            board.squares[self.pos_x + self.pos_y * 8].figure = self
            self.first_move = False

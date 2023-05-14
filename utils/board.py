import pygame   
import copy

from utils.square import Square
from figures import Pawn, Rook, Queen, King, Knight, Bishop


class Board:
    def __init__(self):
        self.STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.squares = []
        self.chosen: Square = None
        self.white_to_move = True

        #  Create a 8x8 board
        index = 0
        for rank in range(8):
            for file in range(8):
                self.squares.append(Square(index, file, rank))
                index += 1
        self.load_position_from_fen()

    def draw_board(self, display: pygame.Surface):
        for square in self.squares:
            pygame.draw.rect(display, square.color, square.rect)
            if square.figure:
                display.blit(square.figure.image, square.rect)
        self.draw_moves(display)

    def draw_moves(self, display: pygame.Surface):
        if self.chosen:
            pygame.draw.rect(display, (0, 0, 255), self.chosen.rect, 5)
            possible_moves, attacking_moves = self.chosen.figure.get_possible_moves(
                self
            )
            if self.chosen.figure.rank == 100:
                castling_moves = self.chosen.figure.get_castling(self)
                for move in castling_moves:
                    pygame.draw.rect(display, (255, 255, 0), move.rect, 5)
            for move in possible_moves:
                pygame.draw.rect(display, (0, 255, 0), move.rect, 5)
            for move in attacking_moves:
                pygame.draw.rect(display, (255, 0, 0), move.rect, 5)

    def load_position_from_fen(self):
        fen = self.STARTING_FEN.split(" ")[0]
        file = 0
        rank = 0

        for symbol in fen:
            if symbol == "/":
                rank += 1
                file = 0
                continue
            if symbol == "p":
                self.squares[file + rank * 8].figure = Pawn(file, rank, False, 1)
            elif symbol == "P":
                self.squares[file + rank * 8].figure = Pawn(file, rank, True, 1)
            elif symbol == "r":
                self.squares[file + rank * 8].figure = Rook(file, rank, False, 5)
            elif symbol == "R":
                self.squares[file + rank * 8].figure = Rook(file, rank, True, 5)
            elif symbol == "n":
                self.squares[file + rank * 8].figure = Knight(file, rank, False, 3)
            elif symbol == "N":
                self.squares[file + rank * 8].figure = Knight(file, rank, True, 3)
            elif symbol == "b":
                self.squares[file + rank * 8].figure = Bishop(file, rank, False, 3)
            elif symbol == "B":
                self.squares[file + rank * 8].figure = Bishop(file, rank, True, 3)
            elif symbol == "q":
                self.squares[file + rank * 8].figure = Queen(file, rank, False, 9)
            elif symbol == "Q":
                self.squares[file + rank * 8].figure = Queen(file, rank, True, 9)
            elif symbol == "k":
                self.squares[file + rank * 8].figure = King(file, rank, False, 100)
            elif symbol == "K":
                self.squares[file + rank * 8].figure = King(file, rank, True, 100)
            print(file, rank, symbol)

            file += 1

    def click(self, pos: tuple[int, int]):
        if self.chosen:
            possible_moves, attacking_moves = self.chosen.figure.get_possible_moves(
                self
            )
            castling_moves = []
            if self.chosen.figure.rank == 100:
                castling_moves = self.chosen.figure.get_castling(self)
            if not possible_moves + attacking_moves + castling_moves:
                self.chosen = None
                return
            for move in possible_moves + attacking_moves:
                if move.rect.collidepoint(pos):
                    board_copy = self.squares.copy()
                    self.make_move(move)
                    if self.is_check(self.white_to_move, self.squares):
                        print("Check")
                        self.squares = board_copy.copy()
                        break
                    break
            for move in castling_moves:
                if move.rect.collidepoint(pos):
                    self.chosen.figure.castle(move, self)
                    self.chosen = None
                    break
            else:
                self.chosen = None
        else:
            for square in self.squares:
                if square.rect.collidepoint(pos):
                    print(square.figure)
                    if square.figure:
                        if self.white_to_move and square.figure.color:
                            self.chosen = square
                            break
                        elif not self.white_to_move and not square.figure.color:
                            self.chosen = square
                            break
                    else:
                        self.chosen = None

    def make_move(self, move: Square):
        self.white_to_move = not self.white_to_move
        move.figure = self.chosen.figure
        self.chosen.figure.pos_x = move.file
        self.chosen.figure.pos_y = move.rank
        if self.chosen.figure.rank == 1:
            if self.chosen.figure.pos_y == 7 or self.chosen.figure.pos_y == 0:
                new_queen = Queen(
                    self.chosen.figure.pos_x,
                    self.chosen.figure.pos_y,
                    self.chosen.figure.color,
                    9,
                )
                self.squares[
                    self.chosen.figure.pos_x + self.chosen.figure.pos_y * 8
                ].figure = new_queen
            self.chosen.figure.first_move = False
        if self.chosen.figure.rank == 5:
            self.chosen.figure.first_move = False
        self.chosen.figure = None
        self.chosen = None

    def is_check(self, color: bool) -> bool:
        """
        Checks if the king of the given color is in check.

        :param color: True if for white, False if for black
        :return: True if the king is in check, False otherwise
        """
        attacking_moves = []
        for square in self.squares:
            if square.figure:
                if square.figure.color == color and square.figure.rank == 100:
                    king = square
                elif square.figure.color != color:
                    possible_moves, attacking = square.figure.get_possible_moves(
                        self
                    )
                    attacking_moves += attacking
        if king in attacking_moves:
            return True
        return False

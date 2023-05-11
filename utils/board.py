import pygame

from utils import Square
from figures import Pawn, Rook, Queen, King, Knight, Bishop
from figures.figure import Figure


class Board:
    def __init__(self):

        self.STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.squares = []
        self.chosen: Square = None

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
            pygame.draw.rect(display, (255, 0, 0), self.chosen.rect, 5)
            possible_moves = self.chosen.figure.get_possible_moves(self)
            for move in possible_moves:
                pygame.draw.rect(display, (0, 255, 0), move.rect, 5)


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
                self.squares[file + rank*8].figure = Pawn(file, rank, "black", 1)
            elif symbol == "P":
                self.squares[file + rank*8].figure = Pawn(file, rank, "white", 1)
            elif symbol == "r":
                self.squares[file + rank*8].figure = Rook(file, rank, "black", 5)
            elif symbol == "R":
                self.squares[file + rank*8].figure = Rook(file, rank, "white", 5)
            elif symbol == 'n':
                self.squares[file + rank*8].figure = Knight(file, rank, "black", 3)
            elif symbol == 'N':
                self.squares[file + rank*8].figure = Knight(file, rank, "white", 3)
            elif symbol == 'b':
                self.squares[file + rank*8].figure = Bishop(file, rank, "black", 3)
            elif symbol == 'B':
                self.squares[file + rank*8].figure = Bishop(file, rank, "white", 3)
            elif symbol == 'q':
                self.squares[file + rank*8].figure = Queen(file, rank, "black", 9)
            elif symbol == 'Q':
                self.squares[file + rank*8].figure = Queen(file, rank, "white", 9)
            elif symbol == 'k':
                self.squares[file + rank*8].figure = King(file, rank, "black", 100)
            elif symbol == 'K':
                self.squares[file + rank*8].figure = King(file, rank, "white", 100)
            print(file, rank, symbol)

            file += 1

    def click(self, pos: tuple[int, int]):
        if self.chosen:
            if self.chosen.rect.collidepoint(pos):
                self.chosen = None
            else:
                possible_moves = self.chosen.figure.get_possible_moves(self)
                for move in possible_moves:
                    if move.rect.collidepoint(pos):
                        move.figure = self.chosen.figure
                        self.chosen.figure.pos_x = move.file
                        self.chosen.figure.pos_y = move.rank
                        if self.chosen.figure.rank == 1:
                            self.chosen.figure.first_move = False 
                        self.chosen.figure = None
                        self.chosen = None
                        break
        else:
            for square in self.squares:
                if square.rect.collidepoint(pos):
                    if square.figure:
                        self.chosen = square
                    else:
                        self.chosen = None
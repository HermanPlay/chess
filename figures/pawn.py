import os
import pygame

from config import Config
from figures.figure import Figure
# import utils.board as board
# import utils.square as square

class Pawn(Figure):
    def __init__(self, pos_x, pos_y, color, rank):
        super().__init__(pos_x, pos_y, color, rank)
        self.image = pygame.image.load(
            os.path.join("assets", "figures", f"{color}_pawn.png")
        )
        self.image = pygame.transform.scale(self.image, (Config.SQUARE_SIZE, Config.SQUARE_SIZE))
        self.first_move = True
    
    def get_possible_moves(self, board):
        possible_moves = []
        moves = [1]
        if self.first_move: 
            moves.append(2)
        if self.color == "white":
            for move in moves:
                possible_move = self.pos_x + (self.pos_y - move) * 8
                if board.squares[possible_move].figure is None:
                    possible_moves.append(board.squares[possible_move])
        else:
            for move in moves:
                possible_move = self.pos_x + (self.pos_y + move) * 8
                if board.squares[possible_move].figure is None:
                    possible_moves.append(board.squares[possible_move])
        return possible_moves
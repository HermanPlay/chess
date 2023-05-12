class Figure:
    def __init__(self, pos_x, pos_y, color, rank):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.rank = rank
        self.image = None

    def get_possible_moves(self, board):
        return []

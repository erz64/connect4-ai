import math
from board import GameBoard
import random
class Ai:
    def __init__(self):
        self.board = GameBoard()

    def choose_move(self, board):
        move = self.minimax(5, True, board)[0]
        return move

    def minimax(self, depth, maximising, board, col=random.randint(0,6), row=0, alpha=0, beta=0, turn="yellow"):
        locations = self.get_valid_locations(board)
        for (col, row) in locations:
            print(col)
        won = self.board.check_for_win(col, row, turn, board)
        new_col = random.randint(0,6)
        if depth == 0 or won:
            if won:
                if turn == "yellow":
                    return (col, math.inf)
                else:
                    return (col, -math.inf)
            return (col, 0)
        if maximising:
            value = -math.inf
            for (col, row) in locations:
                copy = board.copy()
                self.board.place_piece(col, row, "yellow", copy)
                new_value = self.minimax(depth-1, False, copy, col, row, alpha, beta, "red")[1]
                if new_value > value:
                    new_col = col
                    value = new_value
            return (new_col, value)
        else:
            value = math.inf
            for (col, row) in locations:
                copy = board.copy()
                self.board.place_piece(col, row, "red", copy)
                new_value = self.minimax(depth-1, True, copy, col, row, alpha, beta, "yellow")[1]
                if new_value < value:
                    new_col = col
                    value = new_value
            return (new_col, value)
                    
    
    def get_valid_locations(self, board):
        locations = []
        for i in range(7):
            row = self.board.check_free_space(i, board)
            if row == 0:
                continue
            else:
                locations.append((i, row))
        return locations
    
        
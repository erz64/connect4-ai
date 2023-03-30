import math
from board import GameBoard
import random
class Ai:
    def __init__(self):
        self.board = GameBoard()

    def choose_move(self, board):
        data = self.minimax(5, True, board)
        move = data[0]
        value = data[1]
        return move

    def minimax(self, depth, maximising, board, col=0, row=0, alpha=0, beta=0, turn="yellow"):
        locations = self.get_valid_locations(board)
        (won, player) = self.board.check_for_win(col, row, turn, board)
        
        if depth == 0 or won:
            if won:
                if player == "yellow":
                    return (None, 100000)
                else:
                    return (None, -100000)
            else:
                return (None, 0)
        if len(locations) == 0:
            return (None, 0)
        if maximising:
            new_col = random.choice(locations)
            value = -math.inf
            for col in locations:
                row = self.board.check_free_space(col, board)
                if row < 0:
                    continue
                copy = [["blank","blank","blank","blank","blank","blank"] for _ in range(7)]
                for i in range(0, len(board)):
                    for j in range(0, len(board[i])):
                        copy[i][j] = board[i][j]
                self.board.place_piece(col, row, "yellow", copy)
                new_value = self.minimax(depth-1, False, copy, col, row, alpha, beta, "red")[1]
                if new_value > value:
                    new_col = col
                    value = new_value
            return new_col, value
        else:
            value = math.inf
            new_col = random.choice(locations)
            for col in locations:
                row = self.board.check_free_space(col, board)
                if row < 0:
                    continue
                copy = [["blank","blank","blank","blank","blank","blank"] for _ in range(7)]
                for i in range(0, len(board)):
                    for j in range(0, len(board[i])):
                        copy[i][j] = board[i][j]
                self.board.place_piece(col, row, "red", copy)
                new_value = self.minimax(depth-1, True, copy, col, row, alpha, beta, "yellow")[1]
                if new_value < value:
                    new_col = col
                    value = new_value
            return new_col, value
                    
    
    def get_valid_locations(self, board):
        locations = []
        for i in range(7):
            row = self.board.check_free_space(i, board)
            if row < 0:
                continue
            locations.append(i)
        return locations
    
        
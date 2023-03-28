from board import GameBoard
import math

class Ai:
    def __init__(self, board):
        self.board = board
    
    def choose_move(self):
        pass

    def minimax(self, depth, maximising, board, alpha=0, beta=0):
        arvo = 0
        game_board = GameBoard(board)
        locations = self.get_valid_locations(game_board)
        if depth == 0 or arvo == "win":
            return arvo
        if maximising:
            arvo = -math.inf
            for col in locations:
                copy = board.copy()
                board.place_piece()
    
    def get_valid_locations(self, board):
        locations = []
        for i in range(6):
            row = board.check_free_space(i, board)
            if row == 0:
                continue
            else:
                locations.append(i)
        return locations    
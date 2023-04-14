import math
from board import GameBoard
import random
import time

class Ai:
    """ Class that is used to get a move for the opponent
    when playing against the computer
    
    Attributes:
        board: Board class to help check for a winner,
        and for valid piece locations
    """
    def __init__(self):
        self.board = GameBoard()

    def choose_move(self, board):
        """Chooses a move for the Ai to play

        Args:
            board (list): The current locations of pieces in the game board

        Returns:
            move (int): the column on which the Ai places a piece
        """
        time_start = time.time()
        move = 0
        value = 0
        depth = 2
        while time.time() < time_start + 1:
            data = self.minimax(depth, True, board)
            new_move = data[0]
            new_value = data[1]
            if new_value >= 10000: # Ai won
                value = new_value
                move = new_move
            if new_value > value:
                value = new_value
                move = new_move
            depth += 1
        return move

    def minimax(self, depth, maximising, board, col=None, row=None, alpha=-math.inf, beta=math.inf, turn="yellow", count=0):
        """The algorithm for the Ai to figure out the optimal move in the current situation

        Args:
            depth (int): Tells the algorithm how deep from the current position should it look to find the best move
            maximising (bool): if the minimax algorithm is trying to maximise or minimise the value for the move
            board (list): The locations of pieces in the game board
            col (int, optional): On which column is the algorithm checkin on. Defaults to None.
            row (int, optional): On which row is the algorithm checkin on. Defaults to None.
            alpha (int, optional): Used to optize the algorithm. Defaults to -infinity.
            beta (int, optional): Used to optize the algorithm. Defaults to infinity.
            turn (str, optional): Which player's turn is at the state of the algorithm. Defaults to "yellow".
            count (int, optional): How many times it took to reach the current state. Used to prefer moves over others.

        Returns:
            move(int), value(int): the best column to place the piece on, and value for which was achieved using the algorithm
        """
        locations = self.get_valid_locations(board)
        sorted_locations = sorted(locations, key = lambda x: abs(x-locations[len(locations)//2]))

        if col != None and row != None: # Checks if called for the first time
            (won, player, score) = self.board.check_for_win(col, row, turn, board)
        else:
            won = False
        if depth == 0 or won:
            if won:
                if player == "yellow":
                    return (None, 100000-count)
                else:
                    return (None, -100000+count)
            else:
                if player == "yellow":
                    return (None, score)
                else:
                    return (None, -score)
        if len(locations) == 0:
            return (None, 0)
        new_col = random.choice(locations)
        if maximising:
            value = -math.inf
            for col in sorted_locations:
                row = self.board.check_free_space(col, board)
                copy = self.board.copy_board(board)
                self.board.place_piece(col, row, "yellow", copy)
                new_value = self.minimax(depth-1, False, copy, col, row, alpha, beta, "yellow", count+1)[1]
                if new_value > value:
                    new_col = col
                    value = new_value
                alpha = max(alpha, value)
                if value >= beta:
                    break
            return new_col, value
        else:
            value = math.inf
            for col in sorted_locations:
                row = self.board.check_free_space(col, board)
                copy = self.board.copy_board(board)
                self.board.place_piece(col, row, "red", copy)
                new_value = self.minimax(depth-1, True, copy, col, row, alpha, beta, "red", count+1)[1]
                if new_value < value:
                    new_col = col
                    value = new_value
                beta = min(beta, value)
                if value <= alpha:
                    break
            return new_col, value
                    
    
    def get_valid_locations(self, board):
        """Get valid location for the minimax algorithm
        to place pieces on the board

        Args:
            board (list): The locations of pieces in the game board

        Returns:
            locations(list): List of valid columns to place pieces
        """
        locations = []
        for col in range(7):
            row = self.board.check_free_space(col, board)
            if row < 0:
                continue
            locations.append(col)
        return locations
    
    
        
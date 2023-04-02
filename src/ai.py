import math
from board import GameBoard
import random

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
        data = self.minimax(5, True, board)
        move = data[0]
        return move

    def minimax(self, depth, maximising, board, col=None, row=None, alpha=0, beta=0, turn="yellow"):
        """The algorithm for the Ai to figure out the optimal move in the current situation

        Args:
            depth (int): Tells the algorithm how deep from the current position should it look to find the best move
            maximising (bool): if the minimax algorithm is trying to maximise or minimise the value for the move
            board (list): The locations of pieces in the game board
            col (int, optional): On which column is the algorithm checkin on. Defaults to None.
            row (int, optional): On which row is the algorithm checkin on. Defaults to None.
            alpha (int, optional): Used to optize the algorithm. Defaults to 0.
            beta (int, optional): Used to optize the algorithm. Defaults to 0.
            turn (str, optional): Which player's turn is at the state of the algorithm. Defaults to "yellow".

        Returns:
            move(int), value(int): the best column to place the piece on, and value for which was achieved using the algorithm
        """
        locations = self.get_valid_locations(board)
        if col != None and row != None:
            (won, player) = self.board.check_for_win(col, row, turn, board)
        else:
            won = False
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
        new_col = random.choice(locations)
        if maximising:
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
                new_value = self.minimax(depth-1, False, copy, col, row, alpha, beta, "yellow")[1]
                if new_value > value:
                    new_col = col
                    value = new_value
            return new_col, value
        else:
            value = math.inf
            for col in locations:
                row = self.board.check_free_space(col, board)
                if row < 0:
                    continue
                copy = [["blank","blank","blank","blank","blank","blank"] for _ in range(7)]
                for i in range(0, len(board)):
                    for j in range(0, len(board[i])):
                        copy[i][j] = board[i][j]
                self.board.place_piece(col, row, "red", copy)
                new_value = self.minimax(depth-1, True, copy, col, row, alpha, beta, "red")[1]
                if new_value < value:
                    new_col = col
                    value = new_value
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
        for i in range(7):
            row = self.board.check_free_space(i, board)
            if row < 0:
                continue
            locations.append(i)
        return locations
    
        
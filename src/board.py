class GameBoard:
    """Class that keeps track of each players pieces in the game
    Attributes:
        pieces: Players' pieces in the board
    """
    def __init__(self, board=[["blank","blank","blank","blank","blank","blank"] for _ in range(7)]):
        self.pieces = board
    
    def place_piece(self, x, y, color, board):
        board[x][y] = color
        
    def check_free_space(self, col, board):
        """Checks where there is free space available for the players piece
        Args:
            col (int): Which button was pressed
            board (list): Which board to check on
        Returns:
            row (int), the row to place the piece on
        """
        row = 0
        for piece in board[col]:
            if piece != "blank":
                break
            row += 1
        return row-1
    
    def check_for_win(self, col, row, turn, board):
        win = [self._check_vertical_win(col, row, turn, board), self._check_horizontal_win(col, row, turn, board),
            self._check_diagonal_win_left_to_right(col, row, turn, board), self._check_diagonal_win_right_to_left(col, row, turn, board)]
        if True in win:
            return True
        return False
            

    def _check_vertical_win(self, col, row, turn, board):
        count = 1
        # upwards
        for i in range(1, row):
            if board[col][row-i] != turn:
                break
            else:
                count += 1 
        # downwards
        for i in range(1, 6-row):
            if board[col][row+i] != turn:
                break
            else:
                count += 1
        if count >= 4:
            return True
        return False

    def _check_horizontal_win(self, col, row, turn, board):
        count = 1
        # left
        for i in range(1, col+1):
            if board[col-i][row] != turn:
                break
            else:
                count += 1
        # right
        for i in range(1, 7-col):
            if board[col+i][row] != turn:
                break
            else:
                count += 1
        if count >= 4:
            return True
        return False

    def _check_diagonal_win_left_to_right(self, col, row, turn, board):
        count = 1
        # smaller is the one closest to the edge
        smaller = min(col+1, 6-row)
        # left and down
        for i in range(1, smaller):
            if board[col-i][row+i] != turn:
                break
            else:
                count += 1
        smaller = min(row, 7-col)
        # right and up
        for i in range(1, smaller):
            if board[col+i][row-i] != turn:
                break
            else:
                count += 1
        if count >= 4:
            return True
        return False

    def _check_diagonal_win_right_to_left(self, col, row, turn, board):
        count = 1
        # smaller is the one closest to the edge
        smaller = min(col+1, row)
        # left and up
        for i in range(1, smaller):
            if board[col-i][row-i] != turn:
                break
            else:
                count += 1
        smaller = min(6-row, 7-col)
        # right and down
        for i in range(1, smaller):
            if board[col+i][row+i] != turn:
                break
            else:
                count += 1
        if count >= 4:
            return True
        return False
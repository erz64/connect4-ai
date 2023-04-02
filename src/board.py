class GameBoard:
    """Class that keeps track of each players pieces in the game
    Attributes:
        pieces: Players' pieces in the board
    """
    def __init__(self, board=[["blank","blank","blank","blank","blank","blank"] for _ in range(7)]):
        self.pieces = board
    
    def place_piece(self, col, row, color, board):
        """Places a piece on the board

        Args:
            col (int): On which column to place the piece on
            row (int): On which row to place the piece on
            color (str): What color is the place to place
            board (list): On which board to place the piece on
        """
        board[col][row] = color
        
    def check_free_space(self, col, board):
        """Checks where there is free space available for the players piece
        Args:
            col (int): Which column to check on
            board (list): Which board to check on
        Returns:
            row (int), the row where there is free space
        """
        row = 0
        for piece in board[col]:
            if piece != "blank":
                break
            row += 1
        return row-1
    
    def check_for_win(self, col, row, turn, board):
        """Checks if the newly placed piece results in a win

        Args:
            col (int): Which column to check for
            row (int): Which row to check for
            turn (str): Which turn was the piece placed on
            board (list): On which board to check for a win

        Returns:
            won(Bool), turn(str): Won is true if piece placed resulted in a win otherwise False.
            turn which turn was the piece placed on
        """
        win = [self._check_vertical_win(col, row, turn, board), self._check_horizontal_win(col, row, turn, board),
            self._check_diagonal_win_left_to_right(col, row, turn, board), self._check_diagonal_win_right_to_left(col, row, turn, board)]
        if True in win:
            return (True, turn)
        return (False, turn)
            

    def _check_vertical_win(self, col, row, turn, board):
        """Checks if the newly placed piece results in a win, forming a vertical 4 in a row

        Args:
            col (int): Which column to check for
            row (int): Which row to check for
            turn (str): Which turn was the piece placed on
            board (list): On which board to check for a win

        Returns:
            won(bool): True if it resulted in a vertical 4 in a row, otherwise False
        """
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
        """Checks if the newly placed piece results in a win, forming a horizontal 4 in a row

        Args:
            col (int): Which column to check for
            row (int): Which row to check for
            turn (str): Which turn was the piece placed on
            board (list): On which board to check for a win

        Returns:
            won(bool): True if it resulted in a horizontal 4 in a row, otherwise False
        """
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
        """Checks if the newly placed piece results in a win,
        forming a diagonal 4 in a row from left to right

        Args:
            col (int): Which column to check for
            row (int): Which row to check for
            turn (str): Which turn was the piece placed on
            board (list): On which board to check for a win

        Returns:
            won(bool): True if it resulted in a diagonal 4 in a row
            from left to right, otherwise False
        """
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
        """Checks if the newly placed piece results in a win,
        forming a diagonal 4 in a row from right to left

        Args:
            col (int): Which column to check for
            row (int): Which row to check for
            turn (str): Which turn was the piece placed on
            board (list): On which board to check for a win

        Returns:
            won(bool): True if it resulted in a diagonal 4 in a row
            from right to left, otherwise False
        """
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
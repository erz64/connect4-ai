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
            color (str): What color is the piece to place
            board (list): On which board to place the piece on
        """
        board[col][row] = color
    
    def copy_board(self, board):
        """Copies the board given, returns the new board

        Args:
            board (list_): The board to copy

        Returns:
            copy(list): New board
        """
        copy = [["blank","blank","blank","blank","blank","blank"] for _ in range(7)]
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                copy[i][j] = board[i][j]
        return copy

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

    def check_for_draw(self, board):
        """Checks for draw from the board given

        Args:
            board (list): The board which to check on

        Returns:
            draw (bool): True if draw found, False otherwise
        """
        for col in board:
            for row in col:
                if row not in ["red", "yellow"]:
                    return False
        return True

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
        vertical_win, vertical_count = self._check_vertical_win(col, row, turn, board)
        horizontal_win, horizontal_count = self._check_horizontal_win(col, row, turn, board)
        diagonal_left_to_right_win, diagonal_left_to_right_count = self._check_diagonal_win_left_to_right(col, row, turn, board)
        diagonal_right_to_left_win, diagonal_right_to_left_count = self._check_diagonal_win_right_to_left(col, row, turn, board)

        win = [vertical_win, horizontal_win, diagonal_left_to_right_win, diagonal_right_to_left_win]
        counts = [vertical_count, horizontal_count, diagonal_left_to_right_count, diagonal_right_to_left_count]
        total_score = self._get_total_score(counts)
        if True in win:
            return (True, turn, total_score)
        return (False, turn, total_score)
    
    def _get_total_score(self, counts):
        """Gets the total score based on number of pieces of same color forming lines

        Args:
            counts (list): How many of same color pieces in a line

        Returns:
            total_score (int): Weighted score based on counts
        """
        total_score = 0
        for count in counts:
            if count == 2:
                total_score += 5
            if count == 3:
                total_score += 25
            if count == 4:
                total_score += 100
        return total_score

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
        for i in range(1, row): # Upwards
            if board[col][row-i] != turn:
                break
            else:
                count += 1 
        for i in range(1, 6-row): # Downwards
            if board[col][row+i] != turn:
                break
            else:
                count += 1

        if count >= 4:
            return (True, count)
        return (False, count)


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
        for i in range(1, col+1): # Left
            if board[col-i][row] != turn:
                break
            else:
                count += 1
        for i in range(1, 7-col): # Right
            if board[col+i][row] != turn:
                break
            else:
                count += 1
        if count >= 4:
            return (True, count)
        return (False, count)

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
        # Smaller is the one closest to the edge
        smaller = min(col+1, 6-row)
        for i in range(1, smaller): # Left and down
            if board[col-i][row+i] != turn:
                break
            else:
                count += 1
        smaller = min(row, 7-col)
        for i in range(1, smaller): # Right and up
            if board[col+i][row-i] != turn:
                break
            else:
                count += 1
        if count >= 4:
            return (True, count)
        return (False, count)

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
        # Smaller is the one closest to the edge
        smaller = min(col+1, row)
        for i in range(1, smaller): # Left and up
            if board[col-i][row-i] != turn:
                break
            else:
                count += 1
        smaller = min(6-row, 7-col)
        for i in range(1, smaller): # Right and down
            if board[col+i][row+i] != turn:
                break
            else:
                count += 1
        if count >= 4:
            return (True, count)
        return (False, count)

    
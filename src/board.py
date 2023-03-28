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
    

class GameBoard:
    """Class that keeps track of each players pieces in the game
    Attributes:
        pieces: Players' pieces in the board
    """
    def __init__(self, board=[["blank","blank","blank","blank","blank","blank"] for i in range(7)]):
        self.pieces = board
    
    def place_piece(self, x, y, color="red"):
        self.pieces[x][y] = color
    

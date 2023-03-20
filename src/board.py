class GameBoard:
    def __init__(self):
        self.pieces = [["blank","blank","blank","blank","blank","blank"] for i in range(7)]
    
    def place_piece(self, x, y, color="red"):
        print(x)
        print(y)
        if y == -1:
            return
        self.pieces[x][y] = color
    

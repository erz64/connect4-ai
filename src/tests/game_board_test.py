import unittest
from board import GameBoard

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()
    
    def test_check_vertical_win(self):
        self.board.place_piece(0, 5, "red", self.board.pieces)
        self.board.place_piece(0, 4, "red", self.board.pieces)
        self.board.place_piece(0, 3, "red", self.board.pieces)
        self.board.place_piece(0, 2, "red", self.board.pieces)
        self.assertEqual(self.board._check_vertical_win(0, 2, "red", self.board.pieces)[0], True)
    
    def test_check_horizontal_win(self):
        self.board.place_piece(0, 5, "red", self.board.pieces)
        self.board.place_piece(1, 5, "red", self.board.pieces)
        self.board.place_piece(2, 5, "red", self.board.pieces)
        self.board.place_piece(3, 5, "red", self.board.pieces)
        self.assertEqual(self.board._check_horizontal_win(3, 5, "red", self.board.pieces)[0], True)
    
    def test_check_diagonal_win_left_to_right(self):
        self.board.place_piece(0, 5, "red", self.board.pieces)
        self.board.place_piece(1, 4, "red", self.board.pieces)
        self.board.place_piece(2, 3, "red", self.board.pieces)
        self.board.place_piece(3, 2, "red", self.board.pieces)
        self.assertEqual(self.board._check_diagonal_win_left_to_right(3, 2, "red", self.board.pieces)[0], True)

    def test_check_diagonal_win_right_to_left(self):
        self.board.place_piece(6, 5, "red", self.board.pieces)
        self.board.place_piece(5, 4, "red", self.board.pieces)
        self.board.place_piece(4, 3, "red", self.board.pieces)
        self.board.place_piece(3, 2, "red", self.board.pieces)
        self.assertEqual(self.board._check_diagonal_win_right_to_left(3, 2, "red", self.board.pieces)[0], True)
    
    def test_get_correct_score_for_the_ai_move(self):
        self.board.place_piece(2, 5, "red", self.board.pieces)
        self.board.place_piece(2, 4, "yellow", self.board.pieces)
        self.board.place_piece(3, 5, "yellow", self.board.pieces)
        self.board.place_piece(3, 4, "yellow", self.board.pieces)
        self.board.place_piece(4, 5, "red", self.board.pieces)
        self.board.place_piece(4, 4, "yellow", self.board.pieces)
        self.board.place_piece(4, 3, "red", self.board.pieces)
        
        score = self.board.check_for_win(3, 4, "yellow", self.board.pieces)[2]
        correct_score = 30
        self.assertEqual(score, correct_score)
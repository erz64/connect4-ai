import unittest
from ai import Ai
from board import GameBoard

class TestAi(unittest.TestCase):
    def setUp(self):
        self.ai = Ai()
        self.board = GameBoard()

    def test_ai_finds_a_win_in_one_move(self):
        pieces = [["blank","blank","blank","blank","blank","blank"] for _ in range(7)]
        self.board.place_piece(0, 5, "yellow", pieces)
        self.board.place_piece(1, 5, "yellow", pieces)
        self.board.place_piece(2, 5, "yellow", pieces)
        correct_move = 3
        self.assertEqual(self.ai.choose_move(pieces), correct_move)
    
    def test_ai_finds_a_forced_win_in_7_moves(self):
        pieces = [["blank","blank","blank","blank","blank","blank"] for _ in range(7)]
        self.board.place_piece(1, 5, "red", pieces)
        self.board.place_piece(1, 4, "yellow", pieces)
        self.board.place_piece(1, 3, "red", pieces)
        self.board.place_piece(1, 2, "red", pieces)
        self.board.place_piece(1, 1, "yellow", pieces)
        self.board.place_piece(1, 0, "yellow", pieces)
        self.board.place_piece(2, 5, "red", pieces)
        self.board.place_piece(2, 4, "yellow", pieces)
        self.board.place_piece(2, 3, "red", pieces)
        self.board.place_piece(2, 2, "red", pieces)
        self.board.place_piece(2, 1, "yellow", pieces)
        self.board.place_piece(2, 0, "yellow", pieces)
        self.board.place_piece(3, 5, "yellow", pieces)
        self.board.place_piece(3, 4, "yellow", pieces)
        self.board.place_piece(3, 3, "red", pieces)
        self.board.place_piece(3, 2, "red", pieces)
        self.board.place_piece(3, 1, "yellow", pieces)
        self.board.place_piece(3, 0, "red", pieces)
        self.board.place_piece(5, 5, "red", pieces)
        self.board.place_piece(5, 4, "red", pieces)
        self.board.place_piece(5, 3, "red", pieces)
        self.board.place_piece(5, 2, "yellow", pieces)
        self.board.place_piece(5, 1, "red", pieces)
        self.board.place_piece(5, 0, "red", pieces)
        self.board.place_piece(6, 5, "red", pieces)
        
        move = self.ai.choose_move(pieces)
        correct_move = 6
        self.assertEqual(move, correct_move)
    
    def test_ai_denies_player_win(self):
        pieces = [["blank","blank","blank","blank","blank","blank"] for _ in range(7)]
        self.board.place_piece(1, 5, "red", pieces)
        self.board.place_piece(1, 4, "red", pieces)
        self.board.place_piece(1, 3, "red", pieces)

        move = self.ai.choose_move(pieces)
        correct_move = 1
        self.assertEqual(move, correct_move)
    
  
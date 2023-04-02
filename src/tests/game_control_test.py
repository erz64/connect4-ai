import unittest
import pygame
from game_controller import GameControl
from board import GameBoard
from ai import Ai

class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key

class StubEventQueue:
    def __init__(self, events):
        self._events = events
    
    def get(self):
        return self._events

class TestGameControl(unittest.TestCase):
    def setUp(self):
        self.display = pygame.display.set_mode((1000,800))
        self.board = GameBoard()
        self.ai = Ai()

    def test_buttons_are_initialized_when_initializing_class(self):
        events = [StubEvent(None, None)]
        game_control = GameControl(self.display, StubEventQueue(events), self.ai, True)
        self.assertEqual(len(game_control.buttons), 7)
    
    def test_placing_piece_on_free_space_updates_the_board(self):
        events = [StubEvent(pygame.MOUSEBUTTONDOWN, None)]
        game_control = GameControl(self.display, StubEventQueue(events), self.ai, True)
        game_control.start("player")
        self.assertEqual(game_control.board.pieces[0][5], "red")


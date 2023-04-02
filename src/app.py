import pygame
from game_controller import GameControl
from board import GameBoard
from event_queue import EventQueue
from ai import Ai

def main():
    pygame.init()
    event_queue = EventQueue()
    display = pygame.display.set_mode((1000, 800))
    ai = Ai()
    game_control = GameControl(display, event_queue, ai)
    pygame.display.set_caption("Connect4")
    game_control.main_menu()

if __name__ == "__main__":
    main()
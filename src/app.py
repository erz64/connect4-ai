import pygame
from game_controller import GameControl
from board import GameBoard
def main():
    display = pygame.display.set_mode((1600, 1200))
    board = GameBoard()
    game_control = GameControl(display, board)
    pygame.display.set_caption("Connect4")
    game_control.start()

if __name__ == "__main__":
    main()
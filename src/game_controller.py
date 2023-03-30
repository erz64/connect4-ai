import pygame
import sys
import os
from board import GameBoard
from ai import Ai
class GameControl:
    """Class that controls the game

    Attributes:
        board: List of each players pieces in the game
        display: Pygames display for the game window
        clock: Pygames clock which handles time in the game
    """
    def __init__(self, display, event_queue, test=False):
        self.dirname = os.path.dirname(__file__)
        self._event_queue = event_queue
        self._display = display
        self._clock = pygame.time.Clock()
        self.buttons = self._get_buttons()
        self.test = test
        self._font_1 = pygame.font.SysFont("arial", 24)
        self.ai = Ai()

    def main_menu(self, won=False):
        """ Main menu where player can start the game"""
    
        button_text1 = self._font_1.render("Start game against another player!", True, (0, 0, 0))
        button_text2 = self._font_1.render("Start game against AI", True, (0, 0, 0))
        winner_text = self._font_1.render(f"{won}", True, (255, 255, 255))
        self._display.fill((0, 0, 0))
        button1 = pygame.draw.rect(
            self._display, (0, 200, 87), [600, 300, 300, 50])
        self._display.blit(button_text1, button1)
        button3 = pygame.draw.rect(
            self._display, (0, 200, 87), [200, 300, 300, 50])
        self._display.blit(button_text2, button3)
        if won:
            if won == "red won":
                button2 = pygame.draw.rect(
                self._display, (255, 0, 0), [450, 100, 200, 50])
            else:
                button2 = pygame.draw.rect(
                self._display, (255,255,0), [450, 100, 200, 50])
            self._display.blit(winner_text, button2)
        pygame.display.update()
        start = False
        while not start:
            x, y = pygame.mouse.get_pos()
            for event in self._event_queue.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and button1.collidepoint((x, y)):
                        start = True
                        opponent = "player"
                    if event.button == 1 and button3.collidepoint((x, y)):
                        start = True
                        opponent = "AI"
        self.start(opponent)
    
    def start(self, opponent):
        """Gets called when the program starts,
        starts the game
        """
        self.board = GameBoard([["blank","blank","blank","blank","blank","blank"] for _ in range(7)])
        turn = "red"
        while opponent == "player":
            pygame.display.update()
            self._clock.tick(60)
            self._display.fill((0, 0, 0))
            self.buttons.draw(self._display)
            turn = self._player_inputs(turn)
            if turn not in ["red", "yellow"]:
                break
            self._draw_pieces()
            if self.test:
                break
        while opponent == "AI":
            pygame.display.update()
            self._clock.tick(60)
            self._display.fill((0, 0, 0))
            self.buttons.draw(self._display)
            if turn == "red":
                turn = self._player_inputs(turn)
                if turn not in ["red", "yellow"]:
                    break
            if turn == "yellow":
                board = [["blank","blank","blank","blank","blank","blank"] for _ in range(7)]
                for i in range(0, len(self.board.pieces)):
                    for j in range(0, len(self.board.pieces[i])):
                        board[i][j] = self.board.pieces[i][j]
                col = self.ai.choose_move(board)
                if col == None:
                    break
                row = self.board.check_free_space(col, self.board.pieces)
                self.board.place_piece(col, row, "yellow", self.board.pieces)
                won = self.board.check_for_win(col, row, turn, self.board.pieces)[0]
                if won:
                    turn = "yellow won the game"
                    break
                turn = "red"
            self._draw_pieces()
            
        self.main_menu(turn)

    def _draw_pieces(self):
        """Draws each players' pieces on the display window
        """
        # x,y coordinates in the display window
        x = 0
        y = 200
        for row in self.board.pieces:
            y = 200
            for col in row:
                if col == "red":
                    pygame.draw.circle(self._display, "red", (x*150+50, y), 50)
                if col == "yellow":
                    pygame.draw.circle(self._display, "yellow", (x*150+50, y), 50)
                y += 100
            x += 1

    def _player_inputs(self, turn):
        """Checks for players' inputs

        Args:
            turn (str): Tells which players turn it is

        Returns:
            turn (str): Switches the turn if a piece is placed,
            returns the player acting next
        """
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                turn = self._check_if_button_pressed(turn)
        return turn
    
    def _check_if_button_pressed(self, turn):
        """Checks if a button was pressed,
        and calls for check free space,
        to check if there is space for a new piece

        Args:
            turn (str): Tells which players turn it is

        Returns:
            turn (str): Next players turn
        """
        col = 0
        if self.test:
            (x,y) = 50, 100
        else:
            x, y = pygame.mouse.get_pos()
        for button in self.buttons:
            if button.rect.collidepoint((x, y)):
                turn = self._button_pressed(col, turn)
            col += 1
        return turn

    def _button_pressed(self, col, turn):
        row = self.board.check_free_space(col, self.board.pieces)
        if row < 0:
            return turn
        else:
            self.board.place_piece(col, row, turn, self.board.pieces)
            won = self.board.check_for_win(col, row, turn, self.board.pieces)[0]
        if won:
            return f"{turn} won"
        if turn == "red":
            return "yellow"
        return "red"

    def _get_buttons(self):
        """Initialize buttons for to place a piece in the game
        Returns:
            buttons (list): List of buttons to be used to place a piece
        """
        buttons = pygame.sprite.Group()
        for i in range(7):
            button = pygame.sprite.Sprite()
            button.image = pygame.image.load(os.path.join(self.dirname, "assets", "arrow_button.png"))
            button.rect = button.image.get_rect()
            button.rect.center = (i*150+50, 100)
            buttons.add(button)
        return buttons
    

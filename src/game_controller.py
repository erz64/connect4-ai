import pygame
import sys
import os
from board import GameBoard


class GameControl:
    """Class that controls the game

    Attributes:
        board: List of each players pieces in the game
        display: Pygame's display for the game window
        ai: Class for the computer's moves
        dirname: Where the files are located in the system
        buttons: Buttons for players to press when they want to drop a piece
        test: If this class is run in test settings
        font: Font for the button texts
    """
    def __init__(self, display, event_queue, ai, test=False):
        pygame.init()
        self.dirname = os.path.dirname(__file__)
        self._event_queue = event_queue
        self._display = display
        self.buttons = self._get_drop_piece_buttons()
        self.test = test
        self._font_1 = pygame.font.SysFont("arial", 24)
        self.ai = ai
        self.board = GameBoard([["blank","blank","blank","blank","blank","blank"] for _ in range(7)])
        

    def main_menu(self, won=False):
        """Main menu where player can start the game

        Args:
            won (bool, optional): Tells who won the game. Defaults to False.
        """
        self.start_player_text = self._font_1.render("Start game against another player!", True, (0, 0, 0))
        self.start_ai_text = self._font_1.render("Start game against AI", True, (0, 0, 0))
        self.winner_text = self._font_1.render(f"{won}", True, (255, 255, 255))
        self._display.fill((0, 0, 0))
        if won:
            self._draw_pieces()
            if won == "red won":
                button2 = pygame.draw.rect(
                self._display, (255, 0, 0), [450, 100, 100, 50])
            if won == "yellow won":
                button2 = pygame.draw.rect(
                self._display, (255,255,0), [450, 100, 150, 50])
            if won == "draw":
                button2 = pygame.draw.rect(
                self._display, (0,0,255), [450, 100, 150, 50])
            self._display.blit(self.winner_text, button2)
        self.button1 = pygame.draw.rect(
            self._display, (0, 200, 87), [500, 300, 400, 50])
        self.button3 = pygame.draw.rect(
            self._display, (0, 200, 87), [100, 300, 300, 50])
        self._display.blit(self.start_player_text, self.button1)
        self._display.blit(self.start_ai_text, self.button3)
        
        pygame.display.update()
        start = False
        while not start:
            (start, opponent) = self.main_menu_inputs()
        self.start(opponent)
    
    def main_menu_inputs(self):
        start = False
        opponent = None
        x, y = pygame.mouse.get_pos()
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.button1.collidepoint((x, y)):
                    start = True
                    opponent = "player"
                if event.button == 1 and self.button3.collidepoint((x, y)):
                    start = True
                    opponent = "AI"
        return (start, opponent)

    def start(self, opponent):
        """Gets called when the program starts,
        starts the game

        Args:
            opponent (str): tells the game are you playing against computer or a human
        """
        self.board = GameBoard([["blank","blank","blank","blank","blank","blank"] for _ in range(7)])
        turn = "red"
        self._display.fill((0, 0, 0))
        while opponent == "player":
            if self.board.check_for_draw(self.board.pieces):
                turn = "draw"
                break
            pygame.display.update()
            self.buttons.draw(self._display)
            turn = self._player_inputs(turn)
            if turn not in ["red", "yellow"]:
                break
            self._draw_pieces()
            if self.test:
                break
        while opponent == "AI":

            pygame.display.update()
            self.buttons.draw(self._display)
            if self.board.check_for_draw(self.board.pieces):
                turn = "draw"
                break
            if turn == "red":
                turn = self._player_inputs(turn)
                if turn not in ["red", "yellow"]:
                    break
            if turn == "yellow":
                board = self._copy_board()
                col = self.ai.choose_move(board)
                row = self.board.check_free_space(col, self.board.pieces)
                self.board.place_piece(col, row, "yellow", self.board.pieces)
                won = self.board.check_for_win(col, row, turn, self.board.pieces)[0]
                if won:
                    turn = "yellow won"
                    break
                turn = "red"
                if self.test:
                    break
            self._draw_pieces()

        if not self.test:
            self.main_menu(turn)

    def _copy_board(self):
        board = [["blank","blank","blank","blank","blank","blank"] for _ in range(7)]
        for i in range(0, len(self.board.pieces)):
            for j in range(0, len(self.board.pieces[i])):
                board[i][j] = self.board.pieces[i][j]
        return board

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
        and calls for button pressed function then

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
        """ When drop piece button was pressed,
        this is called, places a piece on the board, and checks for win

        Args:
            col (int): On which column to drop the piece and check for win
            turn (str): Tells next players turn, or if someone won
            

        Returns:
            turn (str): returns the next player or the player who won
        """
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

    def _get_drop_piece_buttons(self):
        """Initialize buttons for to place a piece in the game
        Returns:
            buttons (list): List of buttons to be used to place a piece
        """
        buttons = pygame.sprite.Group()
        for col in range(7):
            button = pygame.sprite.Sprite()
            button.image = pygame.image.load(os.path.join(self.dirname, "assets", "arrow_button.png"))
            button.rect = button.image.get_rect()
            button.rect.center = (col*150+50, 100)
            buttons.add(button)
        return buttons
    

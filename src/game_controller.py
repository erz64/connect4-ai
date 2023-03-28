import pygame
import sys
import os
from board import GameBoard
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

    def main_menu(self, won=False):
        """ Main menu where player can start the game"""
    
        button_text = self._font_1.render("Start game!", True, (0, 0, 0))
        winner_text = self._font_1.render(f"{won}", True, (255, 255, 255))
        self._display.fill((0, 0, 0))
        button1 = pygame.draw.rect(
            self._display, (0, 200, 87), [450, 300, 130, 50])
        self._display.blit(button_text, button1)
        if won:
            if won == "red won the game":
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
        
        self.start()
    
    def start(self):
        """Gets called when the program starts,
        starts the game
        """
        self.board = GameBoard([["blank","blank","blank","blank","blank","blank"] for _ in range(7)])
        turn = "red"
        while True:
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
            won = self.check_for_win(col, row, turn)
        if won:
            return f"{turn} won the game"
        if turn == "red":
            return "yellow"
        return "red"

    
    def check_for_win(self, col, row, turn):
        print(row)
        win = [self._check_vertical_win(col, row, turn), self._check_horizontal_win(col, row, turn),
            self._check_diagonal_win_left_to_right(col, row, turn), self._check_diagonal_win_right_to_left(col, row, turn)]
        if True in win:
            return True
            

    def _check_vertical_win(self, col, row, turn):
        count = 1
        # upwards
        for i in range(1, row):
            if self.board.pieces[col][row-i] != turn:
                break
            else:
                count += 1 
        # downwards
        for i in range(1, 6-row):
            if self.board.pieces[col][row+i] != turn:
                break
            else:
                count += 1
        if count >= 4:
            return True
        return False

    def _check_horizontal_win(self, col, row, turn):
        count = 1
        
        # left
        for i in range(1, col+1):
            if self.board.pieces[col-i][row] != turn:
                break
            else:
                count += 1
        # right
        for i in range(1, 7-col):
            if self.board.pieces[col+i][row] != turn:
                break
            else:
                count += 1
        print(col)
        if count >= 4:
            return True
        return False

    def _check_diagonal_win_left_to_right(self, col, row, turn):
        count = 1
        # smaller is the one closest to the edge
        smaller = min(col+1, 6-row)
        # left and down
        for i in range(1, smaller):
            if self.board.pieces[col-i][row+i] != turn:
                break
            else:
                count += 1
        smaller = min(row, 7-col)
        # right and up
        for i in range(1, smaller):
            if self.board.pieces[col+i][row-i] != turn:
                break
            else:
                count += 1
        if count >= 4:
            return True
        return False
    def _check_diagonal_win_right_to_left(self, col, row, turn):
        count = 1
        # smaller is the one closest to the edge
        smaller = min(col+1, row)
        # left and up
        for i in range(1, smaller):
            if self.board.pieces[col-i][row-i] != turn:
                break
            else:
                count += 1
        smaller = min(6-row, 7-col)
        # right and down
        for i in range(1, smaller):
            if self.board.pieces[col+i][row+i] != turn:
                break
            else:
                count += 1
        if count >= 4:
            return True
        return False

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
    

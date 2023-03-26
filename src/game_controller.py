import pygame
import sys
import os

class GameControl:
    """Class that controls the game

    Attributes:
        board: List of each players pieces in the game
        display: Pygames display for the game window
        clock: Pygames clock which handles time in the game
    """
    def __init__(self, display, board, event_queue, test=False):
        self.dirname = os.path.dirname(__file__)
        self._event_queue = event_queue
        self.board = board
        self._display = display
        self._clock = pygame.time.Clock()
        self.buttons = self._get_buttons()
        self.test = test

    def start(self):
        """Gets called when the program starts,
        starts the game
        """
        turn = "red"
        while True:
            pygame.display.update()
            self._clock.tick(60)
            self._display.fill((0, 0, 0))
            self.buttons.draw(self._display)
            turn = self._player_inputs(turn)
            self._draw_pieces()
            if self.test:
                break

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
                turn = self._check_free_space(turn, col)
            col += 1
        return turn

    def _check_free_space(self, turn, col):
        """Checks where there is free space available for the players piece,
        if not any available return the player in turn,
        if space available place a piece

        Args:
            turn (str): Tells which players turn it is
            col (int): Which button was pressed

        Returns:
            turn (str), Next players turn
        """
        row = 0
        for piece in self.board.pieces[col]:
            if piece != "blank":
                break
            row += 1
        if row == 0:
            return turn
        else:
            self.board.place_piece(col, row-1, turn)
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
    

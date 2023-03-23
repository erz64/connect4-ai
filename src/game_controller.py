import pygame
import sys

class GameControl:
    def __init__(self, display=0, board=0):
        self.board = board
        self._display = display
        self._clock = pygame.time.Clock()
        self.buttons = self._get_buttons()

    def main_menu(self):
        # to be done
        pass

    def start(self):
        turn = "red"
        while True:
            pygame.display.update()
            self._clock.tick(60)
            self._display.fill((0, 0, 0))
            self.buttons.draw(self._display)
            turn = self._player_inputs(turn)
            self._draw_pieces()

    def _draw_pieces(self):
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                turn = self._check_and_place_piece(turn)
        return turn
    
    def _check_and_place_piece(self, turn):
        x, y = pygame.mouse.get_pos()
        row = 0
        col = 0
        for button in self.buttons:
            if button.rect.collidepoint((x, y)):
                for piece in self.board.pieces[row]:
                    if piece != "blank":
                        break
                    col += 1
                if col == 0:
                    return turn
                else:
                    self.board.place_piece(row, col-1, turn)
                if turn == "red":
                    return "yellow"
                return "red"
            row += 1
        return turn
    def _get_buttons(self):
        buttons = pygame.sprite.Group()
        for i in range(7):
            button = pygame.sprite.Sprite()
            button.image = pygame.image.load("assets/arrow_button.png").convert_alpha()
            button.rect = button.image.get_rect()
            button.rect.center = (i*150+50, 100)
            buttons.add(button)
        return buttons
    

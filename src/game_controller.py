import pygame
import sys

class GameControl:
    def __init__(self, display=0, board=0):
        self.board = board
        self._display = display
        self._clock = pygame.time.Clock()
        self.buttons = self._get_buttons()

    def main_menu(self):
        pass

    def start(self):
        while True:
            pygame.display.update()
            self._clock.tick(60)
            self._display.fill((0, 0, 0))
            self.buttons.draw(self._display)
            self._player_inputs()
            self._draw_pieces()

    def _draw_pieces(self):
        x = 0
        y = 200
        for row in self.board.pieces:
            y = 200
            for col in row:
                if col == "red":
                    pygame.draw.circle(self._display, "red", (x*2*100+200, y), 50)
                if col == "yellow":
                    pygame.draw.circle(self._display, "yellow", (x*2*100+200, y), 50)
                y += 100
            x += 1

    def _player_inputs(self):
        x, y = pygame.mouse.get_pos()
        i = 0
        z = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.rect.collidepoint((x, y)):
                        for piece in self.board.pieces[i]:
                            if piece != "blank":
                                break
                            z += 1
                        self.board.place_piece(i, z-1, "red")
                            
                    i += 1

    def _get_buttons(self):
        buttons = pygame.sprite.Group()
        for i in range(7):
            button = pygame.sprite.Sprite()
            button.image = pygame.image.load("assets/arrow_button.png").convert_alpha()
            button.rect = button.image.get_rect()
            button.rect.center = (i*2*100+200, 100)
            buttons.add(button)
        return buttons
    

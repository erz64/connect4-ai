import pygame

class EventQueue:
    """Class to get pygame events
    """
    def get(self):
        return pygame.event.get()
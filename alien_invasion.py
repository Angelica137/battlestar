import sys
import pygame


class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialise the game and create game rss"""
        pygame.init()
        self.screen = pygame.display.set_model((1200, 800))
        pygame.display.set_caption("Battlestar")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Whatch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screens visible.
            pygame.display.flip()

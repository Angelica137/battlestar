class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialise statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Set game active flag
        self.game_active = True

    def reset_stats(self):
        """Initialise statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit

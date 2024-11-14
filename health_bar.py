# Standard library imports
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Local folder imports
    from character import Character


# ------------ Health Bar class setup ------------
class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {"red": "\033[91m",
                    "purple": "\33[95m",
                    "blue": "\33[34m",
                    "blue2": "\33[36m",
                    "blue3": "\33[96m",
                    "green": "\033[92m",
                    "green2": "\033[32m",
                    "brown": "\33[33m",
                    "yellow": "\33[93m",
                    "grey": "\33[37m",
                    "default": "\033[0m"
                    }

    def __init__(self,
                 entity: "Character",
                 length: int = 20,
                 is_colored: bool = True,
                 color: str = ""):
        self.entity = entity
        self.length = length
        self.max_value = entity.health_max
        self.current_value = entity.health

        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]

    def update(self):
        self.current_value = self.entity.health

    def draw(self):
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s HEALTH: {self.entity.health}/{self.entity.health_max}")
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}")

# ------------ XP Bar class setup ------------
class XPBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {"xp_color": "\033[94m",  # Blue for XP
                    "default": "\033[0m"}

    def __init__(self, entity: "Character", length: int = 20):
        self.entity = entity
        self.length = length
        self.max_value = entity.xp_threshold  # XP required to level up
        self.current_value = entity.xp

    def update(self):
        self.current_value = self.entity.xp

    def draw(self):
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s LEVEL: {self.entity.level} XP: {self.entity.xp}/{self.entity.xp_threshold}")
        print(f"{self.barrier}"
              f"{self.colors['xp_color']}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default']}"
              f"{self.barrier}")
        
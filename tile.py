# Local folder imports
from color import Color as c


class Tile:
    def __init__(self, symbol: str, name: str, color: str = c.ANSI_RESET):
        self.symbol = symbol
        self.name = name
        self.legend = f"{symbol} {name.upper()}"

        self.colored_symbol = f"{color}{symbol}{c.ANSI_RESET}"
        self.colored_name = f"{color}{name.upper()}{c.ANSI_RESET}"
        self.colored_legend = f"{self.colored_symbol} {self.colored_name}"


plains = Tile(".", "clearing", c.ANSI_YELLOW)  # clairière
forest = Tile("8", "dense forest", c.ANSI_GREEN)  # forêt dense
pines = Tile("Y", "pine forest", c.ANSI_GREEN)  # forêt de pins
mountain = Tile("A", "rocky hill",)  # colline rocheuse
water = Tile("~", "forest stream", c.ANSI_CYAN)  # ruisseau de forêt
player_marker = Tile("X", "player", c.ANSI_RED)
empty = Tile(" ", "mysterious clearing")  # clairière mystérieuse
town = Tile("M", "forest village", c.ANSI_MAGENTA)  # village forestier
shop = Tile("$", "herbalist's shop", c.ANSI_YELLOW)  # herboristerie
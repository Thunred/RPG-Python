import msvcrt
from save import save_game

from item import  Weapon, Armor,PotionHeal
from item import fists, jaws, short_bow, claws, dragon_breath

# Local folder imports
from health_bar import HealthBar, XPBar
from tile import player_marker

INSTANT_INPUT = False  # Set to True for instant input (no need to press Enter)

# ------------ parent class setup ------------
class Character:
    def __init__(self,
                 name: str,
                 health: int,
                 ):
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists

    def attack(self, target):
        if self.health <= 0:
            return
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {self.weapon.damage} damage to "
              f"{target.name} with {self.weapon.name}")

    def __copy__(self):
        new_instance = self.__class__.__new__(self.__class__)
        new_instance.__dict__.update(self.__dict__)
        # Add any additional attributes that need to be copied
        return new_instance


class Player(Character):
    def __init__(self, name: str = "Player", health: int = 100):
        super().__init__(name=name, health=health)
        
        self.gold = 100  # Starting gold
        self.inventory = [PotionHeal(name="Heath Potion(+50)", healing_amount=50, value=20)]  # Player inventory (weapons, armor, potions)
        self.level = 1
        self.xp = 0  # Experience points
        self.xp_threshold = 100  # XP required for next level

        self.attack_points = 10  # Base attack points
        self.defense_points = 5  # Base defense points
        self.weapon = fists  # Default weapon
        self.armor = None  # Default no armor equipped
        self.max_health = health  # Maximum health
        
        self.health_bar = HealthBar(self, color="green")
        self.xp_bar = XPBar(self)  # Add XP bar

        self.pos = [0, 0]  # Player position (x, y) on the map
        self.marker = player_marker  # Player marker on the map

    def level_up(self):
        if self.xp >= self.xp_threshold:
            self.level += 1
            self.xp -= self.xp_threshold  # Reduce XP by the threshold amount
            self.xp_threshold = int(self.xp_threshold * 1.2)  # Increase XP required for next level
            self.attack_points += 2  # Increase attack points on level up
            self.health_max += 10  # Increase max health on level up
            self.health = self.health_max  # Restore health to max on level up
            print(f"{self.name} leveled up! Now level {self.level}, attack increased to {self.attack_points}, max health is {self.health_max}.")
            self.xp_bar.update()  # Update XP bar after level up

    def gain_xp(self, xp):
        self.xp += xp
        self.xp_bar.update()
        if self.xp >= self.xp_threshold:
            self.level_up()

    def gain_gold(self, gold):
        self.gold += gold
        print(f"{self.name} gained {gold} gold!")
        print(f"Total gold: {self.gold}")

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon
        self.attack_points += weapon.damage
        print(f"{self.name} equipped {weapon.name}, attack increased by {weapon.damage}!")

    def equip_armor(self, armor: Armor):
        self.armor = armor
        self.defense_points += armor.defense
        print(f"{self.name} equipped {armor.name}, defense increased by {armor.defense}!")

    def attack(self, target):
        if self.health <= 0:
            return
        # Reduce damage by target's defense
        damage_dealt = max(self.attack_points + self.weapon.damage - target.defense_points, 0)
        target.health -= damage_dealt
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {damage_dealt} damage to {target.name} with {self.weapon.name}")

    def drop(self):
        print(f"{self.name} dropped {self.weapon.name}!")
        self.weapon = self.default_weapon
        self.attack_points -= self.weapon.damage

    def move(self, x: int, y: int):
        self.pos[0] += x
        self.pos[1] += y

    def calculate_movement_options(self, width, height):
        self.movement_options = {
            "up": self.pos[1] > 0,  # can go up
            "down": self.pos[1] < height - 1,  # can go down
            "left": self.pos[0] > 0,  # can go left
            "right": self.pos[0] < width - 1  # can go right
        }

    def get_movement_input(self, game):
        choice = msvcrt.getch().decode('utf-8') if INSTANT_INPUT else input()

        if choice in ("p", "P"):
            game.use_potion()
        elif choice in ("quit", "QUIT"):
            exit()
        elif choice in ("save", "SAVE"):
           save_game(self, game.game_map)

        elif self.movement_options["up"] and choice in ("z", "Z"):
            self.pos[1] -= 1
        elif self.movement_options["down"] and choice in ("s", "S"):
            self.pos[1] += 1
        elif self.movement_options["left"] and choice in ("q", "Q"):
            self.pos[0] -= 1
        elif self.movement_options["right"] and choice in ("d", "D"):
            self.pos[0] += 1


# ------------ Enemy class setup ------------
class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 defense_points: int = 0,
                 weapon=None,
                 ):
        super().__init__(name=name, health=health,)
        self.weapon = weapon
        self.defense_points = defense_points

        self.health_bar = HealthBar(self, color="red")

        enemies.append(self)


enemies = []
slime = Enemy("Slime", 10,1, jaws)
goblin = Enemy("Goblin", 20,2, short_bow)
spider = Enemy("Spider", 15,3, jaws)
rat = Enemy("Rat", 6,1, claws)
troll = Enemy("Troll", 30,4, fists)
ogre = Enemy("Ogre", 35,5, fists)
dragon = Enemy("Dragon", 50,10, dragon_breath)

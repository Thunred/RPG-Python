# Standard library imports
import os
from abc import ABC, abstractmethod
from copy import deepcopy
from random import randint, choice

# Local folder imports
from map import Map
from character import Player, Enemy, enemies , boss
from shop import Shop
from item import Potion
from random import randint

SPAWN_CHANCE = 10


# ------------ abstract class setup ------------
class Game(ABC):
    def __init__(self, map_w: int, map_h: int):
        self.map_w = map_w
        self.map_h = map_h
        self.game_map = Map(map_w, map_h)
        self.player = Player()
        self.shop = Shop()

    def decorate(self, before=False, after=False):
        newline = "\n"
        print(f"{newline if before else ''}-{'-' * self.map_w}{newline if after else ''}")

    @abstractmethod
    def run(self):
        ...

    @staticmethod
    def clear():
        os.system("cls||clear")

    def spawn_enemy(self, pos: list[int]) -> Enemy | None:
        x, y = pos
        chance = randint(1, 100)
        tile = self.game_map.init_map_data[y][x]
        if chance < SPAWN_CHANCE and tile.name != "forest stream":
            return deepcopy(choice(enemies))

class RPGYnov(Game):
    def __init__(self, map_w: int = 30, map_h: int = 15):
        super().__init__(map_w, map_h)

    def run(self):
        while True:
            # ----- clear the screen
            self.clear()

            # ----- current tile check for shop
            current_tile = self.game_map.init_map_data[self.player.pos[1]][self.player.pos[0]]
            if current_tile.name == "herbalist's shop":
                self.enter_shop()

            # ----- try to spawn an enemy on the current tile, then engage in combat
            if enemy := self.spawn_enemy(self.player.pos):
                self.start_combat(enemy)

            if self.player.level == 5 :
                self.start_combat(boss)
                print("You've defeated the boss! You win!")
                break

            # ----- break out of loop if the player health pool is empty
            if self.player.health <= 0:
                input("Game Over")
                break

            # ----- calculate movement possibilities
            self.player.calculate_movement_options(self.map_w, self.map_h)

            # ----- update map with player (reveal nearby tiles)
            self.game_map.update_map(self.player.pos, self.player.marker)

            # ----- display the map, inventory, and gold
            self.display_game_info()

            self.game_map.display_movement_options(self.player.movement_options)

            # ----- ask for player input
            self.player.get_movement_input(self)

    def start_combat(self, enemy):
        while True:
            # ----- clear the screen and display game map in combat mode
            self.clear()
            self.game_map.display_map()
            self.decorate()

            # ----- display health bars and player stats
            self.player.health_bar.draw()
            enemy.health_bar.draw()
            self.decorate(True)
            
            # ----- display player's inventory and gold during combat
            self.display_inventory()
            print(f"Gold: {self.player.gold}")
            self.decorate(True)

            print("[ENTER] - ATTACK")
            print("[P] - Use Potion")

            # ----- ask for player input during combat
            action = input().lower()

            if action == "p":
                self.use_potion()  # If the player chooses to use a potion
            else:
                # ----- execute attack of combatants
                self.player.attack(enemy)
                enemy.attack(self.player)
                print("[ENTER] - CONTINUE")
                input()

            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated!")
                self.player.gain_xp(randint(5, 10))
                self.player.gain_gold(randint(0, 25))
                input("Press [ENTER] to continue.")
                break
            # ----- finish combat if one of the combatants dies
            if self.player.health <= 0 or enemy.health <= 0:
                self.clear()
                break

    def enter_shop(self):
        self.clear()
        print("You've entered the shop!")
        

        while True:
            print("You have : ",self.player.gold," gold")
            print("\n")
            self.shop.display_items()
            print("Press [Q] to exit the shop.")
            item_choice = input("Enter the number of the item you want to buy: ")
            self.clear()
            # Validate input: check if it's a number and within the correct range
            if item_choice.isdigit() and 1 <= int(item_choice) <= len(self.shop.items_for_sale):
                item_choice = int(item_choice)  # Convert to integer after validation
                self.shop.buy(self.player, item_choice)
            elif item_choice.lower() == "q":
                break
            else:
                print("Invalid choice. Please enter a valid number.")



    def display_game_info(self):
        self.game_map.display_map()
        self.decorate()
        self.player.health_bar.draw()  # Display the health bar
        self.player.xp_bar.draw()      # Display the XP bar
        self.decorate(True)
        print(f"Gold: {self.player.gold}")
        self.display_inventory()
        self.decorate(True)


    def display_inventory(self):
        print ("Equipment:")
        print(f"Weapon: {self.player.weapon.name} - Damage: {self.player.weapon.damage}")
        if self.player.armor:
            print(f"Armor: {self.player.armor.name} - Defense: {self.player.armor.defense}")
        else:
            print("Armor: None")

        print("Inventory:")
        if self.player.inventory:
            for i, item in enumerate(self.player.inventory, 1):
                print(f"{i}. {item.name}")
        else:
            print("Your inventory is empty.")

    def use_potion(self):
        self.clear()
        print("Select a potion to use:")
        potions = [item for item in self.player.inventory if isinstance(item, Potion)]
        
        if not potions:
            print("You don't have any potions!")
            input("Press [ENTER] to continue.")
            return

        for i, potion in enumerate(potions, 1):
            print(f"{i}. {potion.name} - Heals {potion.healing_amount} health")

        potion_choice = input("Choose a potion number: ")

        if potion_choice.isdigit() and 1 <= int(potion_choice) <= len(potions):
            potion_choice = int(potion_choice)
            potion = potions[potion_choice - 1]
            potion.use(self.player)
            self.player.inventory.remove(potion)  # Remove potion after use
        else:
            print("Invalid choice.")

        input("Press [ENTER] to continue.")
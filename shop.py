from item import Weapon, PotionHeal, Armor
from item import iron_sword, leather_armor, iron_armor, health_potion, health_potion_large

class Shop:
    def __init__(self):
        self.items_for_sale = [
            iron_sword,
            leather_armor,
            iron_armor,
            health_potion,
            health_potion_large
        ]

    def display_items(self):
        print("Items for sale:")
        for i, item in enumerate(self.items_for_sale, 1):
            print(f"{i}. {item.name} - {item.value} gold")

    def buy(self, player, item_index):
        item = self.items_for_sale[item_index - 1]
        if player.gold >= item.value:
            player.gold -= item.value
            if isinstance(item, Weapon):
                player.equip_weapon(item)
            elif isinstance(item, Armor):
                player.equip_armor(item)
            elif isinstance(item, PotionHeal):
                player.inventory.append(item)
            print(f"{player.name} bought {item.name}!")
        else:
            print("Not enough gold!")

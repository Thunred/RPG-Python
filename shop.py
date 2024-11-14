from item import *

class Shop:
    def __init__(self):
        self.items_for_sale = [
            # Armes de base
            Weapon(name="Sword", weapon_type="sharp", damage=3, value=2),
            Weapon(name="Bronze Sword", weapon_type="sharp", damage=4, value=3),
            Weapon(name="Silver Sword", weapon_type="sharp", damage=5, value=5),
            Weapon(name="Gold Sword", weapon_type="sharp", damage=6, value=8),
            Weapon(name="Iron Sword", weapon_type="sharp", damage=5, value=15),
            
            # Armes spéciales
            Weapon(name="Obsidian Sword", weapon_type="sharp", damage=7, value=10),
            Weapon(name="Diamond Sword", weapon_type="sharp", damage=8, value=12),
            Weapon(name="Legendary Sword", weapon_type="sharp", damage=10, value=15),

            # Armures
            Armor(name="Leather Armor", defense=10, value=5),
            Armor(name="Iron Armor", defense=20, value=10),
            Armor(name="Obsidian Armor", defense=30, value=15),

            # Potions
            PotionHeal(name="Health Potion (+20)", healing_amount=20, value=10),
            PotionHeal(name="Health Potion (+50)", healing_amount=50, value=20)
        ]

    def display_items(self):
        print("Items for sale:")
        for i, item in enumerate(self.items_for_sale, 1):
            print(f"{i}. {item.name} - {item.value} gold")
            print("\n")

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

# ------------ Base Item class setup ------------
class Item:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

# ------------ Weapon class setup ------------
class Weapon(Item):
    def __init__(self, name: str, weapon_type: str, damage: int, value: int):
        super().__init__(name, value)  # Call the parent class constructor (Item)
        self.weapon_type = weapon_type
        self.damage = damage

# ------------ Potion class setup ------------
class Potion(Item):
    def __init__(self, name: int, value: int):
        super().__init__(name, value)  # Call the parent class constructor (Item)


# ------------ Potion heal class setup ------------
class PotionHeal(Potion):
    def __init__(self, name: str, healing_amount: int, value: int):
        super().__init__(name, value)
        self.healing_amount = healing_amount
    
    def use(self, player):
        if player.health == player.max_health:
            print("You are already at full health.")
            return
        elif player.health + self.healing_amount > player.max_health:
            player.health = player.max_health
            player.health_bar.update()

        else:
            player.health += self.healing_amount
            player.health_bar.update()



# ------------ Armor class setup ------------
class Armor(Item):
    def __init__(self, name: str, defense: int, value: int):
        super().__init__(name, value)
        self.defense = defense




# ------------ object creation ------------
iron_sword = Weapon(name="Iron Sword",
                    weapon_type="sharp",
                    damage=5,
                    value=10)

short_bow = Weapon(name="Short Bow",
                   weapon_type="ranged",
                   damage=4,
                   value=8)

fists = Weapon(name="Fists",
               weapon_type="blunt",
               damage=2,
               value=0)

claws = Weapon(name="Claws",
               weapon_type="sharp",
               damage=3,
               value=0)

dragon_breath = Weapon(name="Dragon Breath",
                       weapon_type="fire",
                       damage=10,
                       value=0)


jaws = Weapon(name="Jaws",
              weapon_type="sharp",
              damage=4,
              value=0)

iron_sword = Weapon(name="Iron Sword", weapon_type="sharp", damage=5, value=15)
leather_armor = Armor(name="Leather Armor", defense=10, value=5)
iron_armor = Armor(name="Iron Armor", defense=20, value=10)
health_potion = PotionHeal(name="Health Potion(+20)", healing_amount=20, value=10)
health_potion_large = PotionHeal(name="Health Potion(+50)", healing_amount=50, value=20)

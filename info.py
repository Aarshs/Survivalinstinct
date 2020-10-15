# Course: CS 30
# Period: 1
# Date created: 2020-09-28
# Date last modified: 2020-10-15
# Name: Aarsh Shah
# Description: Creates classes for characters,
# inventories and locations with characteristics about them.

# class Inventory():
#     def __init__(self, owner, item, item_description, damage, item_num_uses):
#         self.owner = owner
#         self.item = item
#         self.item_description = item_description
#         self.damage = damage
#         self.item_num_uses = item_num_uses

#     def __str__(self):
#         return f"""
#         The items in {self.names}'s inventory include:
#         {self.item} which is a {self.item_description}
#         The {self.item} does {self.damage} damage
#         And can be used {self.item_num_uses}
#         """


class Inventory():
    def __init__(self, *items):
        self.items = list(items)

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return f"""\
The items in {self.name}'s inventory include:
{', '.join(map(lambda x: str(x), self.items))}
        """


class Item():
    def __init__(self, name, description, damage, uses):
        self.name = name
        self.description = description
        self.damage = damage
        self.uses = uses

    def __str__(self):
        return self.name


class Character():
    def __init__(self, name, description, age, health, inventory):
        self.name = name
        self.description = description
        self.age = age
        self.health = health
        inventory.set_name(name)
        self.inventory = inventory

    def __repr__(self):
        return f"""
        {self.name} is the {self.description}. 
        He is {self.age} years old and has {self.health} health
        """

    def __str__(self):
        return self.name


chainsaw = Item("Chainsaw", "Large Weapon", 125, 8),
axe = Item("Axe", "Medium Size Weapon", 50, 12),
ammo = Item("Flare Ammo", "Ammo need to use the Flaregun", 0, 1)

immortal_man = Character("Immortal Man",
                         "horrifying beast who resides in the cave", 235, 500,
                         Inventory(chainsaw, axe, ammo))

print(immortal_man.inventory)

james_dave = Character(
    "James Dave", "sole survivor of the crash", 26, 200,
    Inventory(
        Item("Knife", "Small Weapon", 25, 15),
        Item("Flaregun", "Used to signal for help", 0, 0),
        Item("Metal Shard", "Used to deflect against attacks", -50, 10),
    ))

print(james_dave.inventory)

jungle_inventory = Character(
    "Jungle Inventory", "Items that can be found", "N/A", "N/A",
    Inventory(
        Item("Sword", "High Damage Weapon", 75, 20),
        Item("Adrenaline Shot", "Consumable that increases damage", +50, 2),
    ))

print(jungle_inventory.inventory)


class Locations():
    def __init__(self, place, place_description):
        self.place = place
        self.place_description = place_description

    def location_info(self):
        print(f"The {self.place} is the {self.place_description}")


plane = Locations("Crashed Commerical Plane", "Starting area of the game")
cave = Locations("The Cave", "Home of Immortal Man")
jungle = Locations("The Jungle", "General area to explore to find items")

plane.location_info
cave.location_info()
jungle.location_info()

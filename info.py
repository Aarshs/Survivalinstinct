# Course: CS 30
# Period: 1
# Date created: 2020-09-28
# Date last modified: 2020-09-30
# Name: Aarsh Shah
# Description: Creates Nested Dictionary for characters,
# inventories and locations and prints info about them.

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

    def __str__(self):
        return f"""
        {self.name} is the {self.description}. 
        He is {self.age} years old and has {self.health} health
        """


immortal_man = Character(
    "Immortal Man", "horrifying beast who resides in the cave", "235", "500",
    Inventory(
        Item("Chainsaw", "Large Weapon", 125, 8),
        Item("Axe", "Medium Size Weapon", 50, 12),
        Item("Flare Ammo", "Ammo need to use the Flaregun", 0, 1),
    ))

print(immortal_man.inventory)

james_dave = Character("James Dave"
                       "sole survivor in the plane crash"
                       "26", "200")



def inventory1():
    """A function that creates and prints out info about inventories.
    """
    # Creates a dictionary that stores info on characters inventories.
    inventories = {
        "Immortal Man": {
            "Chainsaw": {
                "Description": "Large Weapon",
                "Damage": 125,
                "Uses": 8,
            },
            "Axe": {
                "Description": "Medium Size Weapon",
                "Damage": 50,
                "Uses": 12,
            },
            "Flare Ammo": {
                "Description": "The ammo that James needs to escape",
                "Damage": 0,
                "Uses": 1,
            },
        },
        "James Dave": {
            "Knife": {
                "Description": "Small Weapon",
                "Damage": 25,
                "Uses": 15,
            },
            "Flaregun": {
                "Description": "Uses flare ammo to signal for help",
                "Damage": 125,
                "Uses": "Dependent on ammo",
            },
            "Metal Shard": {
                "Description": "Shield used to protect against attacks",
                "Damage": -50,
                "Uses": 10,
            },
        },
        "Jungle Inventory": {
            "Sword": {
                "Description": "Large Weapon that can be found",
                "Damage": 75,
                "Uses": 20,
            },
            "Adrenaline Shot": {
                "Description":
                "Consumable that can be found and increases damage",
                "Damage": +50,
                "Uses": 2,
            },
        },
    }

    # Create multiple loops that print statements from the inventory dictionary.
    print("\n\n")
    # Creates a loop that prints out each characters inventory.
    for inventory, elements in inventories.items():
        message = f"{inventory} has a "
        for k, v in elements.items():
            message += f"{k}, "
        print(message[:-2] + ".")
        # Creates a loop that prints the characteristics of each item.
        for k, v in elements.items():
            print(f"*{k}:")
            print(f"    Description: {v['Description']}")
            print(f"    Damage: {v['Damage']}")
            print(f"    Uses: {v['Uses']}")
        print()


class Locations():
    def __init__(self, place, place_description):
        self.place = place
        self.place_description = place_description

    def __str__(self):
        return f"""
        The {self.place} is the {self.place_description}
        """


def location1():
    # Creates a dictionary that stores info about the items in each inventory.
    locations = {
        "The Commerical Plane": "Starting area of the game",
        "The Cave": "Home of Immortal Man",
        "The Jungle": "General area to explore to find items",
    }

    # A for loop that access's the locations dictionary and prints a description.
    print("\n\nThe locations of the game include:")
    for location, description in locations.items():
        print(f"{location} is the {description.lower()}.")


def info():
    character1()
    inventory1()
    location1()


info()

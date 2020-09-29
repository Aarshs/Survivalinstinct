# Course: CS 30
# Period: 1
# Date created: 2020-09-28
# Date last modified: 2020-09-29
# Name: Aarsh Shah
# Description: Creates Nested Dictionary for
# characters, inventories and locations.

# Creates a dictionary that stores information about characters.
characters = {
    "Immortal Man": {
        "Description": "is a horrifying beast whose goal is to hunt",
        "Age": "is 235 years old",
        "Health": "has 500 health"
    },
    "James Dave": {
        "Description": "is the sole survivor in the plane crash",
        "Age": "is 26 years old",
        "Health": "has 250 health"
    }
}

# A for loop that access's the characters dictionary and prints a description.
for character, about in characters.items():
    for k, v in about.items():
        print(f"{character} {v}.")


# Creates a dictionary that stores information about inventories.
inventories = {
    "Immortal Man": {
        "Chainsaw": {
            "Description": "Large Weapon",
            "Damage": 125,
            "Uses": 8
        },
        "Axe": {
            "Description": "Medium Size Weapon",
            "Damage": 50,
            "Uses": 12},
        "Flare Ammo": {
            "Description": "The ammo that James needs to escape",
            "Damage": 0,
            "Uses": 1
        }
    },
    "James Dave": {
        "Knife": {
            "Description": "Small Weapon",
            "Damage": 25,
            "Uses": 15
        },
        "Flaregun": {
            "Description": "Uses flare ammo to signal for help",
            "Damage": 125,
            "Uses": "Dependent on ammo"
        },
        "Metal Shard": {
            "Description": "Shield used to protect against attacks",
            "Damage": -50,
            "Uses": 10
        }
    },
    "Jungle Inventory": {
        "Sword": {
            "Description": "Large Weapon that can be found",
            "Damage": 75,
            "Uses": 20
        },
        "Adrenaline Shot": {
            "Description": "Consumable that can be found and increases damage",
            "Damage": +50,
            "Uses": 2
        }
    }
}

# Create multiple loops that print statements from the inventory dictionary.
print("\n")
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


# Creates a dictionary that stores info about the items in each inventory.
locations = {
    "The Commerical Plane": "Starting area of the game",
    "The Cave": "Home of Immortal Man",
    "The Jungle": "General area to explore to find items",
}

# A for loop that access's the locations dictionary and prints a description.
print("\nThe locations of the game include:")
for location, description in locations.items():
    print(f"{location} is the {description.lower()}.")

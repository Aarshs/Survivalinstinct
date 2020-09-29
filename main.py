# Course: CS 30
# Period: 1
# Date created: 2020-09-28
# Date last modified: 2020-09-28
# Name: Aarsh Shah
# Description: Creates Nested Dictionary for
# characters, inventories and locations

characters = {
    "Immortal Man": {
        "Description": "a horrifying beast whose goal is to hunt",
        "Health": 500},
    "James Dave": {
        "Description": "the sole survivor in the plane crash",
        "Health": 250},
}

for character, about in characters.items():
    print()
    for k, v in about.items():
        print(f"{character} has {v} {k.lower()}.")


inventories = {
    "Immortal Man": {
        "Chainsaw": "125 Damage per hit weapon",
        "Axe": "50 Damage per hit weapon",
        "Flare Ammo": "ammo that James need to escape"},
    "James Dave": {
        "Knife": "25 Damage per hit weapon",
        "Flaregun": "gun that holds flare ammo to signal for help",
        "Metal Shard": "shield used to protect against attacks"},
    "Jungle Inventory": {
        "Sword": "weaopn that can be found by James and does 75 Damage",
        "Adrenaline Shot": "consumable that increases damage by 50"}
}

print("\n")
for inventory, elements in inventories.items():
    message = f"{inventory} has a "
    for k, v in elements.items():
        message += f"{k}, "
    print(message[:-2] + ".")
    for k, v in elements.items():
        print(f"{k} is a {v}")
    print()

print()
locations = {
    "Commerical Plane": "Starting area of the game",
    "Cave": "Home of Immortal Man",
    "Jungle": "General area to explore to find items"
}

for location, description in locations.items():
    print(f"{location} is the {description.lower()}.")

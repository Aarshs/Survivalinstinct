# Course: CS 30
# Period: 1
# Date created: 2020-09-30
# Date last modified: 2020-10-07
# Name: Aarsh Shah
# Description: Creates a series of menus that are used to navigate
# the game/ different options such as movement and inventory.


def quit():
    """A function used within menu's so that the user can end the game
    """
    print("\nEnd Game")
    exit()


def inventory2():
    """Creates a function for the inventory of the character.
    """
    # Creates a dictionary storing both tool and heal items.
    invent = {
        "Tools": ["Knife", "Flashlight", "Flaregun", "Metal Shard"],
        "Heals": ["Medkit", "Bandages", "Painkiler"],
    }
    # A loop that allows the user to input what item they want use
    # And prints what the item does.
    while True:
        print("\nWhat would you like to use?")
        # Gets user input on what type of item they want to use.
        type1 = input("Tools or Heals?\n").lower()
        if type1 == "tools":
            # Gets input on what tool and prints a statement.
            print("\nWhat tool would you like to use")
            for tool in invent["Tools"]:
                print(tool)
            tool = input().lower()
            if tool == "knife":
                print("\nKnife does 25 damage")
            elif tool == "flashlight":
                print("\nFlashlight allows you to see around you")
            elif tool == "flaregun":
                print("\nThis allows you to signal for help")
            elif tool == "metal shard":
                print("\nThis allows you to delfect damage")
            elif tool == "quit":
                quit()
            else:
                print("\nInvalid type")
                continue
        elif type1 == "heals":
            # Gets input on what healable and prints a statement.
            print("\nWhat healable would you like to use")
            for tool in invent["Heals"]:
                print(tool)
            heal = input().lower()
            if heal == "medkit":
                print("\nRestores 50 Health")
            elif heal == "Bandages":
                print("\nRestores 25 Health")
            elif heal == "painkiler":
                print("\nAllows you do more damage")
            elif heal == "quit":
                quit()
            else:
                print("\nInvalid type")
                continue
        elif type1 == "quit":
            quit()
        else:
            print("Invalid type")



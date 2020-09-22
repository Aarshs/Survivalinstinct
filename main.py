# Course: CS 30
# Period: 1
# Date created: 2020-09-18
# Date last modified: 2020-09-21
# Name: Aarsh Shah
# Description: Creates 2 different inventories and lists them numerically

# Creates and prints a list with tools that the user can use
tools = ['Knife', 'Flaregun', 'Metal']

# Creates and prints a list with healing items the user can use
heals = ['Bandages', 'Medkit', 'Painkiller']

# Prints a statement with the available tools
print('Available Tools:')
# Creates a loop for the index and the value of each item in the tools list
for number, tool in enumerate(tools):
    print(f"{number + 1}: {tool}")

# Prints a statement with the available heals
print('\nAvailable Heals:')
# Creates a loop for the index and the value of each item in the heals list
for number, heal in enumerate(heals):
    print(f"{number + 1}: {heal}")

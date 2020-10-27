# RPG: Survival Instinct Changelog
v0.0
- added READ.me for important information
- added changelog to show modifications
- added main game file which imports functions from multiple files
- added pseudocode file with comments
- added menu file with functions
- added map file for the different maps of the game
- added info file for info about characters, locations, and items

v1.0
- changed the main game file to have allow for user input for movement
- changed map file to have classes to create the different maps
- added item file with classes to store info about different type of items
- added villian file for all the enemies that can damage the player
- added player file for the characteristics of the player
- added locations file for data for places
- game can now take user inputs and move around the map, collecting items

v2.0
- the main game file is now fully functional allowing for player inputs to heal, attack, and walk around
- added the enemy map to map file to allow the player to attack when they encounter that enemy
- changed all the items in the item file into static methods
- add a method to the main game file to prevent errors when the player goes out of the map
- added an method for the postioning of what enemy is at the players current location
- added code in main game file to allow for enemies to be removed from the map once they are killed
- added code in main game file to allow for the game to end once the player completes the goal
- Removed redunancies within the program
- optimized program
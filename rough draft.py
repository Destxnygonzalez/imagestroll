# Game instructions function
def show_instructions():
    print('Welcome Sir Cedric on your task! Navigate your way through the '
          'castle and collect all items, do this by using North, East, South, and West '
          'and defeat the Dragon!')


# Show the player's status
def show_status(current_room, item_list):
    print('---------------------------')
    print('You are in the ' + current_room)
    print('Inventory: ', item_list)


# Count number of items in the dictionary
def count_items(rooms):
    item_count = 0
    for key in rooms:
        if 'Item' in rooms[key]['Item'] is not None:
            item_count += 1
    return item_count


# Create rooms and items dictionary
rooms = {
    'Great Hall': {'North': 'Dungeon', 'South': 'Throne Room', 'East': 'Kitchen', 'West': 'Library', 'Item': 'None'},
    'Dungeon': {'East': 'Royal Lair', 'South': 'Great Hall', 'Item': 'Key to the Royal Lair'},
    'Royal Lair': {'West': 'Dungeon', 'Item': 'DRAGON'},
    'Dining Room': {'South': 'Kitchen', 'Item': 'Potion of Strength'},
    'Kitchen': {'West': 'Great Hall', 'North': 'Dining Room', 'Item': 'Shield'},
    'Throne Room': {'North': 'Great Hall', 'East': 'Cellar', 'Item': 'Armor'},
    'Cellar': {'West': 'Throne Room', 'Item': 'Sword'},
    'Library': {'East': 'Great Hall', 'Item': 'Book of Wisdom'}
}

# Declare variables needed for game
inventory = []
valid_moves = ['North', 'South', 'East', 'West']
num_items = count_items(rooms)
current_room = 'Great Hall'

# Call show_instructions function to display game instructions
show_instructions()

while True:
    # Show current status
    show_status(current_room, inventory)

    # Prompt the player to enter a move
    player_move = input("What's your next move? (North, South, East, West) or 'Grab to collect item: ")

    # Validate the moves
    if player_move == 'Exit':
        print('Goodbye!')
        exit(0)
    elif player_move not in valid_moves and player_move != 'Grab':
        print('Enter a valid move: ')
    elif player_move in valid_moves and player_move not in rooms[current_room]:
        print('There is a wall in that direction, Please try again: ')
    else:
        # Move player into room
        if player_move != 'Grab':
            current_room = rooms[current_room][player_move]

        # Check if player is in danger room and won or lost the game
        if current_room == 'Royal Lair':
            if len(inventory) != num_items:
                print("You lost, you didn't have all the items to defeat the dragon!")
            else:
                print("Congratulations! You have defeated the Dragon!")
            exit(0)

        # Get item if it is there and not in inventory
        if 'Item' in rooms[current_room] and rooms[current_room]['Item'] is not None:
            item = rooms[current_room]['Item']
            if item not in inventory:
                inventory.append(item)
                print('You have picked up {}'.format(item))

                # Validate if player won game after adding item
                if len(inventory) == num_items:
                    print('You WIN, you obtained all the items')
                    exit(0)
            else:
                print('Item already in inventory')
        else:
            print('Nothing to pick up in this room')

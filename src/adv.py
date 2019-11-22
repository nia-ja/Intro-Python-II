from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# declare all the items
item = {
    'outside': Item('book', "Whould you like to read?"),
    'foyer': Item('shoe', 'Or you want to stay barefoot?'),
    'overlook': Item('mobile phone', "Take some photos"),
    'narrow': Item('flash-light', 'It could be dark inside'),
    'treasure': Item('coffee', 'It\'s a real treasure in the morning')
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Link item to room
room['outside'].add_item(item['outside'])
room['foyer'].add_item(item['foyer'])
room['overlook'].add_item(item['overlook'])
room['narrow'].add_item(item['narrow'])
room['treasure'].add_item(item['treasure'])

#
# Main
#
def try_direction(direction, current_room):
    attribute = direction + '_to'
#see is the inputted direction is one we can move to
    if hasattr(current_room, attribute):
        #get the new room
        return getattr(current_room, attribute)
    else:
        print("You can't go that way")
        return current_room

def display_item(item):
    room_items = player.curr_room.item_list
    return any(i.name == item for i in room_items)

# Make a new player object that is currently in the 'outside' room.
player = Player(input('Please enter your name here: '), room['outside'])


# Write a loop that:
#
while True:
    room_items = player.current_room.display_item()
    if len(room_items) > 0:
        print(f"There is a {room_items}\n")
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    print(player.name + ", you are in " + player.current_room.name + "\n" + player.current_room.description)
    print(
        'commands: \nq=Quit\nn=North\ne=Eastn\nw=West\ns=South\n')
    # * Waits for user input and decides what to do.
    action = input("\n>").lower().split()
    # * Waits for user input and decides what to do.
    
    # If the user enters "q", quit the game.
    if len(action) == 1:
        action = action[0][0]
        if action == 'q':
            print("see you soon!")
            break
        player.current_room = try_direction(action, player.current_room)
    else:
        print("Wrong command! But you can try again.")
        continue



# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
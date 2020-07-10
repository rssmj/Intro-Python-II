from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms
room = {
    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),
    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),
    'nowhere': Room("nothing exists here", "choose a direction -- n | s | e | w"),
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}

# add items to rooms
room['nowhere'].items.append(Item('portal', 'one way through'))
room['outside'].items.append(Item('unknown', 'it does something'))
room['narrow'].items.append(Item('key', 'it opens something'))

# Link rooms together
room['nowhere'].s_to = room['outside']
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main
playing = True
no = 'nope\n'
err = 'err\n'

# Make a new player object that is currently in the 'outside' room.
subject = Player(input('\n> name or no name: '), room['nowhere'])

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.
while playing:
    print(f'{subject.location.name}')
    print((f'{subject.location.description}'))
    choice = input('decide:\n> ')
    print('')

    if len(choice) == 1:
        # north
        if (choice == 'n'):
            if subject.location.n_to:
                print(f'>>> taveling to {subject.location.n_to.name}\n')
                subject.location = subject.location.n_to
            else: print(no)
        # south
        elif (choice == 's'):
            if subject.location.s_to:
                print(f'>>> taveling to {subject.location.s_to.name}\n')
                subject.location = subject.location.s_to
            else: print(no)
        # east
        elif (choice == 'e'):
            if subject.location.e_to:
                print(f'>>> taveling to {subject.location.e_to.name}\n')
                subject.location = subject.location.e_to
            else: print(no)
        # west
        elif (choice == 'w'):
            if subject.location.w_to:
                print(f'>>> taveling to {subject.location.w_to.name}\n')
                subject.location = subject.location.w_to
            else: print(no)
        # items
        elif (choice == 'i'):
            print('items:')
            if len(subject.inventory) == 0:
                print('nothing here\n')
            else:
                for item in subject.inventory:
                    print(f'{item.name} : {item.description}')
        # quit
        elif (choice == 'q'):
            print('Quitting Game...')
            playing = False
        # err
        else:
            print(err)
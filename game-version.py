# define rooms and items

couch = {
    "name": "couch",
    "type": "furniture",
}

piano = {
    "name": "piano",
    "type": "furniture",
}

crystal_ball= {
    "name": "crystal ball",
    "type": "furniture",
}

table_of_spells = {
    "name": "table of spells",
    "type": "furniture",
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

dining_table = {
    "name": "dining table",
    "type": "furniture",
}

paint = {
    "name": "paint",
    "type": "furniture",
}

laser_saber = {
    "name": "Yoda lasersaber",
    "type": "furniture",
}

chair_1 = {
    "name": "chair",
    "type": "furniture",
}

leather_couch = {
    "name": "leather couch",
    "type": "furniture",
    }

television = {
    "name": "television",
    "type": "furniture",
}

door_a = {
    "name": "door a",
    "type": "door",
}

door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}

door_d = {
    "name": "door d",
    "type": "door",
}

door_e = {
    "name": "door e",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

key_e = {
    "name": "key for door e",
    "type": "key",
    "target": door_e,
}

game_room = {
    "name": "game room",
    "type": "room",
}

bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
}

bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
}

living_room = {
    "name": "living room",
    "type": "room",
}

library_1 = {
    "name": "library",
    "type": "room",
}

outside = {
    "name": "outside"
}

# all_rooms = [game_room, outside, room_1, room_2, living_room]
all_rooms = [game_room, bedroom_1, bedroom_2, living_room, library_1, outside]

all_doors = [door_a, door_b, door_c, door_d, door_e]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a],
    "piano": [key_a],
    "bedroom 1": [door_a, door_b, door_c, queen_bed],
    "queen bed": [key_b],
    "bedroom 2": [door_b, table_of_spells, crystal_ball, double_bed, dresser],
    "double bed": [key_c],
    "dresser": [key_d],
    "living room": [door_d, dining_table, door_e],
    "outside": [door_d],
    "door a": [game_room, bedroom_1],
    "door b": [bedroom_1, bedroom_2],
    "door c": [bedroom_1, library_1],
    "door d": [living_room, outside],
    "door e": [living_room, library_1],
    "Yoda lasersaber": [key_e],
    "library": [door_e, door_c, paint, laser_saber, chair_1, leather_couch, television]
    }

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}


def linebreak():
    """
    Print a line break
    """
    print("\n\n")


def start_game():
    """
    Start the game
    """
    print(
        "You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. \nYou don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state["current_room"])
    # play_room(outside)


def play_room(room):
    # print(game_room)
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if (game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the room!")
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
        elif intended_action == "guess":
            cat(room)
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()

def cat(room):
# import random module
    import random
# create a range of random numbers between 1-10
    n = random.randrange(1,100)
# take a user input to enter a number
    guess = int(input("\nThe cat says: miauuu, if you guess the right number, I will tell you, were the key for door e is!\nPlease enter any number: "))
    while n!= guess: # means if n is not equal to the input guess
# if guess is smaller than n
        if guess < n:
            print("Too low")
# again ask for input
            guess = int(input("Enter number again: "))
# if guess is greater than n
        elif guess > n:
            print("Too high!")
# to again ask for the user input
            guess = int(input("Enter number again: "))
# if guess gets equals to n terminate the while loop
        else:
            break
    return("Congratulations !!\nThe key is in Yoda lasersaber !!")


def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))


def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if (not current_room == room):
            return room


def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None

    for item in object_relations[current_room["name"]]:
        if (item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if (item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if (key["target"] == item):
                        have_key = True
                if (have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if (item["name"] in object_relations and len(object_relations[item["name"]]) > 0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if (output is None):
        print("The item you requested is not found in the current room.")

    if (next_room and input("\nDo you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)


game_state = INIT_GAME_STATE.copy()
start_game()

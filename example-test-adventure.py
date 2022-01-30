#
# The [p]oor ones textadventure-engine
#

import types
import time

# Create a place.
class Place():

    def __init__(self, name, directions):
        self.name = name
        self.directions = directions
        self.description = ""
        self.object = []

    def set_description(self,description):
        self.description = description


# Create an object.
class Object():

    def __init__(self, name, description = ""):
        self.name = name
        self.description = description


# The Game-Engine itselfs.
class Engine():

    def __init__(self):
         self.e = "x"
         self.current_place = place[0]

    def play(self):

        # How to navigate
        def choose_direction():
            global task_done, task_todo
            directions = self.current_place.directions
            print("\nYou can leave to: ")
            for i in range(1, (len(directions)+1)):
                place_name = place[directions[i-1]].name
                print(str(i) + ": " + place_name, end = " ")
            e = input("\nChoose a number, [s]tay or [e]xit the game: ")
            if e == "s":
                return
            elif e == "e":
                print("\nYou managed " + str(len(task_done)) + " of " + str(len(task_todo)) + " tasks.")
                print("\nSee you next time!")
                quit()
            try:
                e = int(e)
                if e > 0 and e <= len(directions):
                    self.current_place = place[directions[e-1]]
                    return
                else:
                    print("\nSorry, number " + str(e) + " does not exist.")
            except:
                print("\nSorry, something went wrong...")
                return

        # How to choose an object
        def choose_object():
            print("\nYou see: ")
            for i in range(1, (len(self.current_place.object)+1)):
                object_name = self.current_place.object[i-1].name
                print(str(i) + ": " + object_name, end = " ")
            e = input("\nChoose a number or [l]eave: ")
            if e == "l":
                return
            try:
                e = int(e)
                if e > 0 and  e <= len(self.current_place.object)+1:
                    self.current_place.object[e-1].start()
                    return
                else:
                    print("\nSorry, number " + str(e) + " does not exist.")
            except:
                print("\nSorry, something went wrong...")
                return

        # How to show items and crafting them
        def items():
            if item:
                print("\nYour items: ")
                item_list = [key for key, value in item.items()]
                print ("{:<8} {:<15} {:<10}".format("Number", "Item", "Count"))
                for i in range(1, (len(item_list)+1)):
                    x = item[item_list[i-1]]
                    if type(x) == bool:
                        x = 1
                    print("{:<8} {:<15} {:<10}".format((str(i) + ":"), item_list[i-1], str(x)))
                while 1 == 1:
                    e = input("\nDo you want to [c]raft something? ")
                    if e == "c":
                        try:
                            first_item = int(input("Number of the first item: "))
                            if first_item < 1 or first_item > len(item_list)+1:
                                print("\nMay this number is out of range!")
                                continue
                            second_item = int(input("Number of the second item: "))
                            if second_item < 1 or second_item > len(item_list)+1:
                                print("\nMay this number is out of range!")
                                continue
                        except:
                            print("\nSorry, may it was not a number...")
                            continue
                        i = 0
                        for i in craft:
                            if item_list[first_item-1] == i[0] and item_list[second_item-1] == i[1] or item_list[first_item-1] == i[1] and item_list[second_item-1] == i[0]:
                                print("\nYou crafted a new item: " + i[2])
                                if type(item[i[0]]) == int:
                                    if item[i[0]] == 1:
                                        item.pop(i[0])
                                    else:
                                        item[i[0]] -= 1
                                if type(item[i[1]]) == int:
                                    if item[i[1]] == 1:
                                        item.pop(i[1])
                                    else:
                                        item[i[1]] -= 1
                                if i[2] in item:
                                    item[i[2]] += 1
                                else:
                                    item[i[2]] = 1
                                return
                        print("\nThis make no sense...")
                    else:
                        return
            else:
                print("\nSorry, at this time you do not have any items.")
                return

        # The main menue
        while 1 == 1:
            print("------------------------------------------------------------------------")
            print("\n" + self.current_place.name + " - " + self.current_place.description)
            e = input("Do you want to look [a]round, to view your [i]tems or to [l]eave? ")
            if e == "l":
                choose_direction()
            elif e == "a":
                choose_object()
            elif e == "i":
                items()


# Create an emty list of places
place = []

# Create an emty list of objects
object = []

# Use item in functions as "global item".
# Items can be int (countable) or True (you have it, but it stay after crafting in your items)
item = {}

# Some examples of itemes.
# Eating a banana is minus one.
item["Banana"] = 2
# After using a knive, it still exist.
item["Knive"] = True

# Use first item (index[0]) and second item (index[1]) to craft a new item (index[2])
# An example of crafting rules:
# If you craft a banana with milk, you get a shake! Or you can slice an apple.
craft = [
        ["Cat food", "Knive", "Open-cat-food"],
        ["Open-cat-food", "Feeding dish", "Lucky-cat"],
        ["Apple", "Knive", "Slices"]
        ]

# May you have to do a task_done to go further. Use as "global" in the beginnning of a function.
task_done = []

# Overview about tasks to do
task_todo = ["relax", "art_expert", "eat_a_banana", "watering_flowers", "feed-the-cat"]

#
# Working with a list in a list. Be carefull with counting the indices!
#
# Create the starting place[0]. Directions are the indices of other places[index]!
# After creation you must care about the indices.
place.append(Place(name = "Floor", directions = [1, 2]))
# directions = [1, 2] means, that there are definitions of place[1] and place[2].

# Add a discription, if you want
place[0].set_description("It is long and dark")

# Add an object to the place[0]
place[0].object.append(Object(name = "Picture"))

# Create a function for the object[0] with the same name as above
def picture(self):
    print("\nWhat a wondefull picture!")
    e = input("Do you [l]ike it? ")
    if e == "l":
        print("You are an expert!")
        task_done.append("art_expert")
        return
    else:
        print("You should better go to school again...")
        return

# Bind the function to the object[0]. Care about the indices! In this case zero.
place[0].object[0].start = types.MethodType(picture, place[0].object[0])

# Add another object. This create the next entry with a index plus one!
place[0].object.append(Object(name = "Door"))

# Create a function for the object with the same name as above
def door(self):
    global item
    print("\nThe door is locked.")
    if not "Key" in item:
        print("Sorry...")
        return
    elif "Key" in item:
        e = input("But you have a key in your pocket. Do you want to [u]se it? ")
        if e == "u":
            print("\nGratulation! Now you can go outside.")
            # Here an example to add a new direction
            place[0].directions.append(4)
            item.pop("Key")
            return
        else:
            return

# Bind the function to the new object[1] with the same name as above and the new index[1]!
place[0].object[1].start = types.MethodType(door, place[0].object[1])

# Create another place
place.append(Place(name = "Living Room", directions = [0, 3]))
place[1].set_description("Feel like home")
place[1].object.append(Object(name = "Table"))

# Example to use the task_done and task_todo lists
def table(self):
    global item, task_done
    if "Key" in item:
        print("\nThe table is empty.")
        return
    elif not "Key" in item:
        if "relax" in task_done:
            print("\nThere is a key on the table.")
            e = input("Do you want to [t]ake the key? ")
            if e == "t":
                print("You put the key in your pocket.")
                # Example to grab a new item
                item["Key"] = 1
                return
            else:
                print("You leave the key on the table.")
                return
        else:
            print("\nYou are very nervous. May relax a little bit?")

place[1].object[0].start = types.MethodType(table, place[1].object[0])
place[1].object.append(Object(name = "Sofa"))
def sofa(self):
    global task
    e = input("\nWhat a nice Sofa. Do you want to [s]it down? ")
    if e == "s":
        print("Great! You relax a moment...")
        # More fun with time
        for i in range(0, 4):
            print(".")
            time.sleep(1)
        print("Ahh! It is good to take a rest.")
        task_done.append("relax")
        return
    else:
        print("You are a little bit nervous, right?")
        return
place[1].object[1].start = types.MethodType(sofa, place[1].object[1])

# Create another place with all stuff
place.append(Place(name = "Kitchen", directions = [0]))
place[2].set_description("A little bit dirty")
place[2].object.append(Object(name = "Dustbin"))

def dustbin(self):
    global item
    print("\nUrg... The dustbin smells like...")
    if "Banana" in item:
        print("\nBut wait, you are hungry. The perfect place to eat your banana.")
        e = input("Do you want to [e]at a banana? ")
        if e == "e":
            print("\nPerfect taste! You throw the banana peel on the floor.")
            # After eating you can not have it.
            item.pop("Banana")
            task_done.append("eat_a_banana")
            return
        else:
            return
    elif not "Banana" in item:
        print("\nWaahhh! You slip and fall. Which idiot throw a banana peel on the floor?")
        return

place[2].object[0].start = types.MethodType(dustbin, place[2].object[0])

place[2].object.append(Object(name = "Sink"))

def sink(self):
    global item, task
    if "watering_flowers" not in task:
        e = input("\nNear the sink is a full watering can. Do you [t]ake it? ")
        if e == "t":
            item["Watering can"] = True
            print("\nOh, it is heavy.")
            return
        else:
            print("\nWhat a rubbish!")
            return
    else:
        print("\nA mess like the rest. Horrible!")
        return

place[2].object[1].start = types.MethodType(sink, place[2].object[1])

# Eat an apple
def kitchen_table(self):
    pass

# Take cat's food
def kitchen_cupboard(self):
    pass

# Create another place with all stuff
place.append(Place(name = "Balcony", directions = [1]))
place[3].set_description("What a wonderfull place!")
place[3].object.append(Object(name = "Flowerpot"))

def flowerpot(self):
    global task, item
    if "watering_flowers" in task:
        print("\nThe flowers are so lovly... Nice!")
    else:
        e = input("\nThe flowers are toasted. May you [w]ater them? ")
        if e == "w":
            if "Watering can" in item:
                print("\nWell done! They look better. You leave the watering can on the balcony.")
                item.pop("Watering can")
                task_done.append("watering_flowers")
                return
            else:
                print("\nUps... You have no water.")
                return
        return

place[3].object[0].start = types.MethodType(flowerpot, place[3].object[0])

# Create another place with all stuff
place.append(Place(name = "Garden", directions = [0]))
place[4].set_description("Flowers and trees are around.")

# Print some prologe:
print("\nWellcome to the poor ones textadventure engine.")
print("\nNavigation:")
print("[a] means, that you can press this key and then ENTER for this action")
print("If you only press ENTER, you go back.")

# Start the game!
game = Engine()
game.play()

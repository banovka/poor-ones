#
# The [p]oor ones textadventure-engine
#

import types
import time

end = False

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
            global task_done, task_todo, end
            directions = self.current_place.directions
            print("\nYou can leave to: ")
            for i in range(1, (len(directions)+1)):
                place_name = place[directions[i-1]].name
                print(str(i) + ": " + place_name, end = " ")
            e = input("\nChoose a number, [s]tay or [e]xit the game: ")
            if e == "s":
                return
            elif e == "e":
                end = True
                return
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
        global end
        while end == False:
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
item["Banana"] = 1
# After using a knive, it still exist.
item["Knive"] = True

# Use first item (index[0]) and second item (index[1]) to craft a new item (index[2])
# An example of crafting rules:
# If you craft a banana with milk, you get a shake! Or you can slice an apple.
craft = [
        ["Cats food", "Knive", "Open cats food bag"],
        ["Open cats food bag", "Feeding dish", "Full feeding dish"],
        ]

# May you have to do a task_done to go further. Use as "global" in the beginnning of a function.
task_done = []

# Overview about tasks to do
task_todo = ["relax", "art_expert", "eat_a_banana", "watering_flowers", "feed_the_cat"]

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
    global task_done
    if "art_expert" in task_done:
        print("\nYou know this picture, you little expert.")
        return
    else:
        print("\nWhat a wondefull picture!")
        e = input("Do you [l]ike it? ")
        if e == "l":
            print("You are an expert!")
            task_done.append("art_expert")
            return
        else:
            print("May you change your judgement later...")
            return

# Bind the function to the object[0]. Care about the indices! In this case zero.
place[0].object[0].start = types.MethodType(picture, place[0].object[0])

# Add another object. This create the next entry with a index plus one!
place[0].object.append(Object(name = "Door"))

# Create a function for the object with the same name as above
def door(self):
    global item, task_done
    print("\nThe door is locked.")
    if "Key" in item:
        e = input("But you have a key in your pocket. Do you want to [u]se it? ")
        if e == "u":
            print("\nGratulation! Now you can go outside.")
            # Here an example to add a new direction
            place[0].directions.append(4)
            item.pop("Key")
            return
        else:
            return
    else:
        print("Sorry...")
        return

# Bind the function to the new object[1] with the same name as above and the new index[1]!
place[0].object[1].start = types.MethodType(door, place[0].object[1])


# Create a living room
place.append(Place(name = "Living Room", directions = [0, 3]))
place[1].set_description("Feel like home")

# Add a table to the living room
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

# Add a sofa to the living room
place[1].object.append(Object(name = "Sofa"))

def sofa(self):
    global item, task_done
    if not "relax" in task_done:
        e = input("\nWhat a nice Sofa. Do you want to [s]it down? ")
        if e == "s":
            print("Great! You relax a moment...")
            # More fun with time
            for i in range(0, 4):
                print(".")
                time.sleep(1)
            print("Ahh! It is good to take a rest.")
            print("But wait... Oh f**k! You forgot to feed the cat.")
            task_done.append("relax")
            return
        else:
            print("You are a little bit nervous, right?")
            return
    else:
        print("\n No time to relax. I have to do somethig... But what?")
        return

place[1].object[1].start = types.MethodType(sofa, place[1].object[1])

# Add a cat to the living room
place[1].object.append(Object(name = "Cat"))

def cat(self):
    global item, task_done, task_todo, end
    print("\nHow sweet! Your cat is so lovely.")
    if "Full feeding dish" in item:
        print("Now you can feed the cat.")
        print("You go to your sofa, sit down. Relax again.")
        print("What a wonderfull day.")
        task_done.append("feed_the_cat")
        for i in range(0, 4):
            print(".")
            time.sleep(1)
        # Add the end
        end = True
        return
    else:
        print("Your cat run around you. Meow! May she is hungry?")
        return

place[1].object[2].start = types.MethodType(cat, place[1].object[2])

# Create a kitchen
place.append(Place(name = "Kitchen", directions = [0]))
place[2].set_description("A little bit dirty")

# Add a dustbin to the kitchen
place[2].object.append(Object(name = "Dustbin"))

def dustbin(self):
    global item, task_done
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

# Add a sink to the kitchen
place[2].object.append(Object(name = "Sink"))

def sink(self):
    global item, task_done
    if "watering_flowers" not in task_done:
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

# Add a cupboard to the Kitchen
place[2].object.append(Object(name = "Cupboard"))

def kitchen_cupboard(self):
    global item, task_done
    if "Cats food" in item:
        print("\nThe cupboard is empty.")
        return
    else:
        print("\nOn the cupboard you find some cats food.")
        e = input("Do you [t]ake it? ")
        if e == "t":
            print("You grab the cats food. Mmmhh... How can I open it?")
            item["Cats food"] = 1
            return
        else:
            print("You leave the cats food on the cupboard.")
            return

place[2].object[2].start = types.MethodType(kitchen_cupboard, place[2].object[2])


# Create a balcony
place.append(Place(name = "Balcony", directions = [1]))
place[3].set_description("What a wonderfull place!")

# Add a flowerpot to the balcony
place[3].object.append(Object(name = "Flowerpot"))

def flowerpot(self):
    global item, task_done
    if "watering_flowers" in task_done:
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

item["Key"] = True
# Create a garden
place.append(Place(name = "Garden", directions = [0]))
place[4].set_description("Flowers and trees are around.")

# Add a terrace
place[4].object.append(Object(name = "Terrace"))

#item["Feeding dish"] = True
def terrace(self):
    global item, task_done
    if ("Feeding dish" or "Full feeding dish") in item:
        print("\nThe terrace is tidy. But may you forgot something...")
        return
    else:
        print("\nAt the corner of the terrace you find a feeding dish.")
        e = input("Do you [t]ake it? ")
        if e == "t":
            print("You grab the feeding dish.")
            item["Feeding dish"] = True
            return
        else:
            print("You leave the feeding dish at the corner.")
            return

place[4].object[0].start = types.MethodType(terrace, place[3].object[0])

# Print some prologe:
print("\nWellcome to the poor ones textadventure engine.")
print("\nNavigation:")
print("[a] means, that you can press this key and then ENTER for this action")
print("If you only press ENTER, you go back.")

# Start the game!
game = Engine()
game.play()

# Informations after theend of game
print("\nYou solved " + str(len(task_done)) + " of " + str(len(task_todo)) + " tasks.")
print("\nSee you next time!\n")

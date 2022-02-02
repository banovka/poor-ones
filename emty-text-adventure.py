#
# The [p]oor [o]nes [t]extadventure-engine
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

# Create an emty dict for items
item = {}

# Add crafting rules.
craft = [
        ["a", "b", "c"],
        ]
# Emty list to collect your task
task_done = []

# Overview about tasks to do
task_todo = []

# Create a place
place.append(Place(name = "Room 1", directions = [0]))

# Add some discription
place[0].set_description(" ")

# Append an object
place[0].object.append(Object(name = "Something"))

# Define a function
def something(self):
    global item, task_done, task_todo, end
    pass

# Add the function to the object
place[0].object[0].start = types.MethodType(something, place[0].object[0])

# Print something befor start the game
print("Hello")

# Start the game!

game = Engine()
game.play()

# Print something after the game
print("End")

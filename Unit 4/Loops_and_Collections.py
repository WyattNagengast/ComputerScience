#Python has 4 types of collections
#Tuple
#Set
#>list
#>Dictionary

# Today we are foucosing o lists
#A list is a way to store more thann one value in a single variable
#The values in a list are called ITEMS
#Items can be accessed by their index (position in the list) indices
#Index                          0                   1                2                3            4
best_elden_ring_weapons = ["Blastphemous Blade", "Moonveil", "Rivers of Blood", "Iron Ball", "Bloodhoud's Fang"]
best_years = [1776, 1985, 1994, 1957, 2016]

print(len(best_elden_ring_weapons))

print(best_years[0])
print(best_elden_ring_weapons[0])
print(best_elden_ring_weapons[len(best_elden_ring_weapons) - 1])

#List items can be changed!!!
best_elden_ring_weapons[3]= "Spiked Fist"
print(best_elden_ring_weapons[3])

#List functions
#.pop()
# removes an item at a given index
best_elden_ring_weapons.pop(1) #removes Moonveil from the game

#.remove()
# Removes an item by value, removes the first instance of the value
best_elden_ring_weapons.remove("Blasphemous Blade") #if the value doesn't exist, it errors

#.append()
# Adds the value as a new item to the end of the list
best_elden_ring_weapons.append("Death's Poker")
import random
roll5random_numbers = {random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)}
print(roll5random_numbers)

#.sort()
# Sorts numbers from smallest to greatest
roll5random_numbers.sort()
print(roll5random_numbers)

#max()
#prints the largest number in the list
print(max(roll5random_numbers))
#min()
#prints the smallest number in the list
print(min(roll5random_numbers))

# Strings ... are just lists of characters :0
print("Owsowski"[2])
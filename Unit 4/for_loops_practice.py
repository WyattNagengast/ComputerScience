#For Loops allow us to iterate through a list!
#iterate: perform repeatedly
# to do something repeatedly
# to look at every itam in a list, one by one

# basic syntax
#Syntax: the grammar of a code

pokemon_cards = ["Squirtle", "Bidoof", "Zigzagoon", "Charizard"]

for card in pokemon_cards:
    print("The next car is...")
    print(card)

route = ["Home", "Taco Bell", "The Park", "Goofwill", "Home"]
#Changing your mind can sometimes be the most difficult thing you ever do.

#You need to look at multiple list items durring one iteration,
# Doing for item in list dose not really work
# for item in list only lets you access one list item per iteration
#for location in route:
#    print("You are traveling from " + location + " to " + location[1])
    #this doesn't work

#if you need to access multiple list items durring the same iteration
# using for variable in range is perferred
for i in range(0, len(route)):  #creates a list  [0, 1, 2, 3, 4, 5]
    #use a try/except block to hanble index out of error
    #errror will happen on the last iteration
    #because i+1 would be larger than the number of items in the list
    try:
        print("You ar traveling from " + route[1] + " to " + route[i+1])
    except:
        print("Route finished!")

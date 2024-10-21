def start_adventure():
    print("You are grabing one weapon before you leave your house to go to the forest to hunt. Do you:")
    print("1. Grab the hatchet")
    print("2. Grab the crossbow")
    print("3. Grab the dagger")

    wc = input("> ")        #wc = weapon choice
    if wc == "1":
        wc = "hatchet"
    elif wc == "2":
        wc = "crossbow"
    elif wc == "3":
        wc = "dagger"
    else:
        print("Invalid answer please try again.")
        start_adventure()
    
    print("You grab the " + wc + " and head for the forest.")
    reach_forest()

def reach_forest():
    print("Once you reach the forest you begin to reconsider going hunting today, because it is very dark out now. Do you:")
    print("1. enter the forest to hunt")
    print("2. head home")

    choice = input("> ")
    if choice == "1":
        enter_forest()
    elif choice == "2":
        head_home()         #ending 1
    else:
        print("Invalid answer please try again.")
        reach_forest()

def head_home():
    print("You decide that its better to head home, but your adventure ends here.")

def enter_forest():
    print("You bravely head into the forest to hunt.")
    print("After a while of walking you hear an animal nearby, but you are not sure what animal you hear. Do you:")
    print("1. check out what animal it is")
    print("2. continue on and look for a different animal")

    choice = input("> ")
    if choice == "1":
        find_animal1()
    elif choice == "2":
        continue_search()
    else:
        print("Invalid answer please try again.")
        enter_forest()

def find_animal1():
    print("You find the animal and it is a black bear. Do you")
    print("1. prepare to atack")
    print("2. sneak away and flea")
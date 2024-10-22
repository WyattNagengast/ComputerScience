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
            head_home()         #endding 1
        else:
            print("Invalid answer please try again.")
            reach_forest()

    def head_home():        #endding 1
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

        choice = input("> ")
        if choice == "1":
            attack_prep()
        elif choice == "2":
            flea()
        else:
            print("Invalid answer please try again.")
            find_animal1()

    def flea():
        print("After you flea you start to consider just heading back for the night. Do you:")
        print("1. head home")
        print("2. countinue search")

        choice = input("> ")
        if choice == "1":
            head_home()     #endding 1
        elif choice == "2":
            continue_search()
        else:
            print("Invalid answer please try again.")
            flea()

    def continue_search():
        print("You continue searching for prey, but after awhile you start to debate giving up in defeat. Do you:")
        print("1. countinue searching")
        print("2. give up and head home without food")

        choice = input("> ")
        if choice == "1":
            search_continues()
        elif choice == "2":
            attempt_to_head_home()      #endding 2
        else:
            print("Invalid answer please try again.")
            continue_search()
    
    def search_continues():

    def attempt_to_head_home():         #endding 2
        print("You begin to head home.\nBut you collapse out of hunger half way home.")
        print("You do not make it home.")

    def attack_prep():
        print("You decide that you are going to attempt to hunt the Black Bear. Do you:")
        if wc == "hatchet":
            hatchet_attacks()
        elif wc == "crossbow":
            crossbow_attacks()
        elif wc == "dagger":
            dagger_attacks()
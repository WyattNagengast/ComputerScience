import random
def start_adventure():
    print("Please note that all rolls will use d20s, please enjoy the game.")
    print("You are grabing one weapon before you leave your house to go to the forest to hunt. Do you:")
    print("1. Grab the hatchet")                #choice 1
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
        print("1. enter the forest to hunt")              #choice 2
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

    def enter_forest():             #choice 3
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

    def find_animal1():         #choice 4
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

    def flea():         #choice 5
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

    def continue_search():      #choice 4 or 6
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
    
    def search_continues():     #choice 5 or 7
        print("You continue searching for prey, after awhile you find a heard of deer. Do you:")
        print("1. prepare to attack")
        print("2. leave them be")

        choice = input("> ")
        if choice == "1":
            attack_deer()
        elif choice == "2":
            ignor_deer()
        else:
            print("Invalid answer please try again.")
            search_continues()

    def ignor_deer():
        print("You decide not to hunt the deer.\nBecause of how late it is you attempt to head home.")
        attempt_to_head_home()      #endding 2

    def attack_deer():          #choice set 6 or 8
        print("You decide to hunt the deer. Do you:")
        if wc == "hatchet":
            hatchet_a_d()
        elif wc == "crossbow":
            crossbow_a_d()
        elif wc == "dagger":
            dagger_a_d()

    def attempt_to_head_home():         #endding 2
        print("You begin to head home.\nBut you collapse out of hunger half way home.")
        print("You do not make it home.")

    def attack_prep():              #choice set 5
        print("You decide that you are going to attempt to hunt the Black Bear. Do you:")
        if wc == "hatchet":
            hatchet_a_b()
        elif wc == "crossbow":
            crossbow_a_b()
        elif wc == "dagger":
            dagger_a_b()

    def hatchet_a_b():      #choice 5
        print("1. cut trees to make traps for the bear")
        print("2. throw hatchet at bear")
        print("3. charge at and hit the bear with the hatchet")

        choice = input("> ")
        if choice == "1":
            make_trapb()
        elif choice == "2":
            throw_or_shoot_weaponb()
        elif choice == "3":
            mele_attackb()
        else:
            print("Invalid answer please try again.")
            hatchet_a_b()

    def make_trapb():           #choice 6
        print("You have decided to make a trap, but what type of trap will you make?")
        print("1. hidden partialy dug in wood spears")
        print("2. swinging log")
        print("3. falling trees")

        choice = input("> ")
        if choice == "1":
            wood_spearsb()
        elif choice == "2":
            swinging_log()
        elif choice == "3":
            falling_trees()
        else:
            print("Invalid answer please try again.")
            make_trapb()
    
    def wood_spearsb():         #choice 7
        print("Now that you have made the wood spear trap, how are you going to lure the bear into it?")
        print("1. use your self as bait while running to the trap")
        print("2. throw something at the bear from the other side of the trap")

        choice = input("> ")
        if choice == "1":
            self_bait()
        elif choice == "2":
            throw_b()
        else:
            print("Invalid answer please try again.")
            wood_spearsb()

    def self_bait():
        print("Roll for success.")
        roll = random.randrand(1,20)
        if roll >= 14:
            success_survivetb()
        elif roll >= 9:
            success_deathtb()         #endding 4
        elif roll < 9:
            death_failtb()         #endding 3
    
    def success_survivetb():        #choice 8
        print("You have successfuly managed to kill the bear and survive.\nNow it is time to head home but you are extremly hungry. Do you:")
        print("1. attempt to head home")
        print("2. stop and eat before heading home")

        choice = input("> ")
        if choice == "1":
            attempt_to_head_home()      #endding 2
        elif choice == "2":
            head_home_after_eating()

    def head_home_after_eating():       #endding 5
        print("You waited to eat before heading home.")

    def success_deathtb():        #endding 4
        print("You succeded to kill the bear in the trap, but before the bear hit the trap it kiled you.")

    def death_failtb():            #endding 3
        print("You failed to get the bear to hit the spears and died.\nGAME OVER!!")
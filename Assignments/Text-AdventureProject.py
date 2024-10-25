import random
wc = "none"
def start_adventure():          #encouter 1
    global wc
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

def reach_forest():         #encounter 2
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
    game_over()

def enter_forest():             #choice 3       #encounter
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

def find_animal1():         #choice 4       #encounter
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

def flea():         #choice 5       #encounter
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

def continue_search():      #choice 4 or 6      encounter
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

def search_continues():     #choice 5 or 7      #encounter
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

def attack_deer():          
    global wc          #choice set 6 or 8
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
    game_over()

def hatchet_a_d():
    print("1. cut trees to make traps for the deer")
    print("2. throw hatchet at deer")
    print("3. charge at and hit the deer with the hatchet")
    choice = input("> ")
    if choice == "1":
        make_trapd()
    elif choice == "2":
        throw_weapond()
    elif choice == "3":
        mele_attackd()
    else:
        print("Invalid answer please try again.")
        hatchet_a_d()

def throw_weapond():
    print("You decide to throw your weapon at the deer.\nRoll for success.")
    roll = random.randrange(1,20)
    print(roll)
    if roll >= 16:
        successb_throw_shoot()
    elif roll >= 10:
        miss_throw()
    elif roll < 10:
        fail_throw()

def miss_throw():             #encounter
    print("After throwing your weapons you miss all your targets, and they run away. Do you:")
    print("1. try to catch them without picking up your weapon")
    print("2. get your weapon and try to catch them")
    print("3. give up and just pickup your weapon")

    choice = input("> ")
    if choice == "1":
        chase_deer_no_wc()
    elif choice == "2":
        chase_deer_with_wc()
    elif choice == "3":
        zero_deer()
    else:
        print("Invalid answer please try again.")
        miss_throw()

def chase_deer_no_wc():         #roll
    print("Roll for successfull chase.")
    roll = random.randrange(1,20)
    print(roll)
    if roll >= 15:
        catch_up_to_deer_nowc()
    elif roll < 15:
        fail_to_catch_up()

def catch_up_to_deer_nowc():        #roll
    print("With no weapon you attempt to grapple with one of the deer. Roll for success.")
    roll = random.randrange(1,20)
    print(roll)
    if roll >= 16:
        one_deer_collectwc()
    elif roll >= 12:
        zero_deer()
    else:
        dead_faild()

def one_deer_collectwc():           #roll
    print("After killing the deer you grapled with you attempt to locate your weapon. Roll for succes.")
    roll = random.randrange(1,20)
    print(roll)
    if roll >= 15:
        findwc_one_deer()
    else:
        fail_findwc_one_deer()

def chase_deer_with_wc():       #roll
    print("Roll for successfull chase.")
    roll = random.randrange(1,20)
    print(roll)
    if roll >= 15:
        catch_up_to_deerwc()
    elif roll < 15:
        fail_to_catch_up()

def catch_up_to_deerwc():           #encouter
    print("You caught up to the deer. Do you")
    print("1. try for mele")
    print("2. throw weapon again")

    choice = input("> ")
    if choice == "1":
        mele_attackd()
    elif choice == "2":
        throw_weapond()
    else:
        print("Invalid answer please try again.")
        catch_up_to_deerwc()

def fail_to_catch_up():             #encounter
    print("You failed to catch up to the deer and gave up. Do you:")
    print("1. make camp")
    print("2. give up and attempt to head home")
    
    choice = input("> ")
    if choice == "1":
        make_camp()
    elif choice == "2":
        attempt_to_head_home()
    else:
        print("Invalid answer please try again.")
        fail_to_catch_up()

def zero_deer():            
    print("You failed to kill any deer and gave up. Do you:")
    print("1. make camp")
    print("2. give up and attempt to head home")

    choice = input("> ")
    if choice == "1":
        make_camp()
    elif choice == "2":
        attempt_to_head_home()
    else:
        print("Invalid answer please try again.")
        zero_deer()

def mele_attackd():         #roll
    print("You charge at the deer herd to kill as many as you can. Roll for success.")
    roll = random.randrang(1,20)
    print(roll)
    if roll >= 16:
        three_deer()
    elif roll >= 12:
        two_deer()
    elif roll >= 8:
        one_deer()
    else:
        zero_deer_mele()

def three_deer():
    print("You manage to catch three deer, and decide that your hunt was a complete success and head home, thus endding your hunt.")
    game_over()

def two_deer():
    print("You manage to catch two deer, and decide that your hunt was a success and head home, thus endding your hunt.")
    game_over()

def one_deer():
    print("You manage to catch one deer, and decide that your hunt was a success and head home, thus endding your hunt.")
    game_over()

def zero_deer_mele():            #encounter
    print("You failed to kill any deer and broke an ankle. Do you:")
    print("1. make camp")
    print("2. give up and attempt to head home")

    choice = input("> ")
    if choice == "1":
        make_camp()
    elif choice == "2":
        attempt_head_home_broke_ankle()
    else:
        print("Invalid answer please try again.")
        zero_deer_mele()

def make_camp():            #endding
    print("You decide to make camp, before you go to bed you catch a rabbit for dinner.\nYou decide to head home in the morning.")
    print("The next morning, you make it home with the remains of the rabbit you caught.")
    game_over()

def attempt_head_home_broke_ankle():                #endding
    print("You attampted to head home with your broken ankle, but you fell into a pit before you left the forest and never got out.")
    game_over()

def attack_prep():              #choice set 5
    global wc
    print("You decide that you are going to attempt to hunt the Black Bear. Do you:")
    if wc == "hatchet":
        hatchet_a_b()
    elif wc == "crossbow":
        crossbow_a_b()
    elif wc == "dagger":
        dagger_a_b()

def crossbow_a_b():         #encounter
    print("1. shoot for vitals first")
    print("2. shoot to disable first")

    choice = input("> ")
    if choice == "1":
        shoot_vitals()
    elif choice == "2":
        shoot_dissable()
    else:
        print("Invalid answer please try again.")
        crossbow_a_b()

def shoot_dissable():       #roll
    print("Roll for success.")
    roll = random.randrange(1,20)
    print(roll)
    if roll >= 15:
        dissable_successb()
    elif roll >= 10:
        dissable_successb0()
    elif roll < 10:
        fail_shootb()

def dissable_successb():
    print("After you dissable the bear, you successfully finish it off with a few more bolts.")
    success_hunt()

def dissable_successb0():           #encounter
    print("You successfully dissabled the bear but ran out of bolts to finish it off. Do you:")
    print("1. attemt to finish it off witt a wooden spike")
    print("2. wait for it to bleed out")

    choice = input("> ")
    if choice == "1":
        wooden_spike()
    elif choice == "2":
        bleed_bear()
    else:
        print("Invalid answer please try again.")
        dissable_successb0()

def wooden_spike():         #endding
    print("You attempt to finish the bear with a wooden spike, and die in the process.")
    game_over()

def shoot_vitals():         #roll
    print("Roll for success.")
    roll = random.randrange(1,20)
    print(roll)
    if roll >= 17:
        successb_throw_shoot()
    elif roll >= 13:
        successb_shoot_two()
    elif roll < 13:
        fail_shootb()

def fail_shootb():              #encounter
    print("Before feling the bear, or dissabling it you run out of bolts. Do you:")
    print("1. flea")
    print("2. clime for safety and wait for the bear to die of blood loss")

    choice = input("> ")
    if choice == "1":
        flea_crossbow()
    elif choice == "2":
        bleed_bear()
    else:
        print("Invalid answer please try again.")
        fail_shootb()

def flea_crossbow():
    print("After fleaing from the bear you decide to head home, because you are out of crossbow bolts.")
    head_home()

def bleed_bear():
    print("After waiting a while the bear collapses.")
    success_hunt()

def successb_shoot_two():
    print("After shooting a few bolts you hit a vital spot.")
    success_hunt()

def dagger_a_b():           #encounter
    print("1. enter a mele with the bear")
    print("2. throw dagger")

    choice = input("> ")
    if choice == "1":
        mele_attackb()
    elif choice == "2":
        throw_weaponb()
    else:
        print("Invalid answer please try again.")
        dagger_a_b

def hatchet_a_b():      #choice 5       encounter
    print("1. cut trees to make traps for the bear")
    print("2. throw hatchet at bear")
    print("3. charge at and hit the bear with the hatchet")
    choice = input("> ")
    if choice == "1":
        make_trapb()
    elif choice == "2":
        throw_weaponb()
    elif choice == "3":
        mele_attackb()
    else:
        print("Invalid answer please try again.")
        hatchet_a_b()

def mele_attackb():         #roll
    print("You decide to charge at the bear and attack it in mele.\nRoll for success.")
    roll = random.randrange(1,20)
    print(roll)
    if roll >= 16:
        eyeb_stab()
    elif roll >= 12:
        bear_mele_live()
    elif roll >= 8:
        bear_mele_tie()
    elif roll < 8:
        bear_mele_fail()

def bear_mele_fail():       #endding
    print("You were killed by the bear in the mele.")
    game_over()

def bear_mele_tie():        #ending
    print("After an intense fight you and the bear both died.")
    game_over()

def bear_mele_live():
    print("After an intense fight, you won.")
    success_hunt()

def eyeb_stab():
    print("On your first stab/cut you managed to hit the eye fataly.")
    success_hunt()

def throw_weaponb():        #roll
    print("You throw your weapon at the bear.\nRoll for success")
    roll = random.randrange(1,20)
    print(roll)
    if roll >= 16:
        successb_throw_shoot()
    elif roll >= 10:
        bear_charge()
    elif roll < 10:
        fail_throw()            #endding 6

def successb_throw_shoot():
    print("You hit the bear in the eye.")
    success_hunt()

def bear_charge():          #roll
    print("The bear lives and charges at you. You attempt to flea, Roll for survival.")
    roll = random.randrange(1,20)
    print(roll)
    if roll >= 15:
        success_flea()
    else:
        fail_flea()         #endding 7

def success_flea():
    print("You have successfully fled the bear.")

def fail_flea():
    print("You failed to escape, and have been killed.")
    game_over()

def fail_throw():           #endding 6
    print("When you attempted to throw your weapon you accidential stabbed your self in the head instead.\nYou never got up again")
    game_over()

def make_trapb():           #choice 6       #encounter
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

def falling_trees():            #roll
    print("With you hatchet and some vines you cut trees in a way that will make them fall at the bear, while holding the trees up until the vines are cut.")
    print("Roll for success")
    roll = random.randrange(1,20)
    print(roll)
    if roll >= 10:
        success_hunt()
    elif roll < 10:
        fail_fall_treesb()

def fail_fall_treesb():          #encounter
    print("The beer tried to run from the falling trees, while the bear did not get out of the area the trees were falling in,\n the bear did end up in an area that the trees missed. Do you:")
    print("1. flea since your trap has failed")
    print("2. throw axe at the bear")
    print("3. charge in for mele")

    choice = input("> ")
    if choice == "1":
        flea_falling_trees()
    elif choice == "2":
        throw_weaponb()
    elif choice == "3":
        mele_attackb()
    else:
        print("Invalid answer please try again.")
        fail_fall_treesb()

def flea_falling_trees():           #roll
    print("After the trees failed to hit your target you decided to start running. Roll for survival.")
    roll = random.randrange(1,20)
    print(roll)
    if roll >= 15:
        success_flea()
    else:
        fail_flea()

def swinging_log():         #roll
    print("With some vines you successfully make a swinging log trap, and relese it at your target. Roll for success.")
    roll = random.randrange(1,20)
    print(roll)
    if roll >= 15:
        success_hunt()
    elif roll >= 10:
        two_swing_hit()
    else:
        fail_swing_logb()

def two_swing_hit():
    print("You see your trap miss and the bear begining to charge at you and then the log swings back and hits the bear.")
    success_hunt()

def fail_swing_logb():          #encounter repeate word change
    print("The log missed the Bear. Do you:")
    print("1. flea since your trap has failed")
    print("2. throw axe at the bear")
    print("3. charge in for mele")

    choice = input("> ")
    if choice == "1":
        flea_swing_log()
    elif choice == "2":
        throw_weaponb()
    elif choice == "3":
        mele_attackb()
    else:
        print("Invalid answer please try again.")
        fail_swing_logb()

def flea_swing_log():
    print("After missing with the log you decide to flea. Roll for survival")
    roll = random.randrange(1,20)
    print(roll)
    if roll >= 15:
        success_flea()
    else:
        fail_flea()


def success_hunt():         #encounter
    print("You successfully captured/killed your pray.")
    print("1. attempt to head home")
    print("2. stop and eat before heading home")
    choice = input("> ")
    if choice == "1":
        attempt_to_head_home()      #endding 2
    elif choice == "2":
        head_home_after_eating()
    else:
        print("Invalid answer please try again.")
        success_hunt()

def wood_spearsb():         #choice 7       #encounter
    print("Now that you have made the wood spear trap, how are you going to lure the bear into it?")
    print("1. use your self as bait while running to the trap")
    print("2. throw your weapon at the bear from the other side of the trap")
    choice = input("> ")
    if choice == "1":
        self_bait()
    elif choice == "2":
        throw_weaponb()
    else:
        print("Invalid answer please try again.")
        wood_spearsb()

def self_bait():        #roll
    print("Roll for success.")
    roll = random.randrand(1,20)
    print(roll)
    if roll >= 14:
        success_hunt()
    elif roll >= 9:
        success_deathtb()         #endding 4
    elif roll < 9:
        death_failtb()         #endding 3

def head_home_after_eating():       # endding 5
    print("You waited to eat before heading home.")
    print("You make it home.")
    home_success()

def home_success():             #endding 3
    print("You have reached home and are preparing for bed. This is the end of your adventure.")
    game_over()

def game_over():
    print("GAME OVER!!\nPlay Again?")
    print("1. Yes")
    print("2. No")
    choice = input("> ")
    if choice == "1":
        start_adventure()
    elif choice == "2":
        print("Please play again in the future")
    else:
        print("Invalid answer please try again.")
        game_over()

def success_deathtb():        #endding 4
    print("You succeded to kill the bear in the trap, but before the bear hit the trap it kiled you.")
    game_over()

def death_failtb():            #endding 5
    print("You failed to get the bear to hit the spears and died.")
    game_over()
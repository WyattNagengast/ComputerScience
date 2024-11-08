# Loop cntrol statements
# Allow you to change loop operations
# they do thing like quit the loop early, skip the current loop, or even do nothing at all
#break, countinue, pass

# break
# exits a loop permanently, before it is supposed to end
#  happens imediatly when ran
# program countinues where the loop ended

# ex.

bag_fruit = ["apple", "orange", "bug", "kiwi", "melon", "mango"]

for fruit in bag_fruit:
    if fruit == "bug":
        print("You found a nasty bug...")
        break       #break exits the loop immediately, and countinues on
    print("You ate a " + fruit)

print("All done!")

# Countine skips the current loop
# it doesn't exit the entire loop, just moves on to the next iteration

#ex.
orders = [15, 30, 35, 23, 100, 3, 10, 22]

# Discount applying program
# Only apply discount for orders above $20

for order in orders:
    if order < 20:
        print("$" + str(order))
        continue
    print("$" + str(order) + " order discounted 5% to $" + str(order * 0.95))

#pass
# does nothing
# usualy used as a placeholder while writing code
# Text-Adventure project

def enter_forest():
    pass

if True:
    pass
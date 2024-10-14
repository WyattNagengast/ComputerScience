# Create a function called free_shipping
# That tells you if you qualify for free shipping
# You only get free shipping if
# You are a Prime member or order is at least $25
# You are at least 18 years old or have parent consent
# Your function should take 4 parameters
# prime (bool), cost (float), age (int), consent (bool)
# you can use more than one logical operator in a condition
# use parenthesis to group if neeeded

def free_shipping(prime, cost, age, consent):
    if (prime == True or cost >= 25) and (age >= 18 or consent == True):
        print("You qualify for free shipping.")
    else:
        print("You do not qualify for free shipping.")

free_shipping(True, 18, 11, False)
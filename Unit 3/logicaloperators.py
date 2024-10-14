# Logical Operators
# Arithmatic Operators + - * / // ** %
# Comparison Operators > < >= <= ==
# Logical Operators and or ! (! = not)
# ! (not) means the inverse, ex. != (not equal to)

def check_eledgibility(age, exp):
    if age >= 18 and exp >= 1:      # and means both conditions must be true
        print("You are elidgible")      # or means at least one must be true
    else:
        print("You are not elidgible...")

check_eledgibility(18, 1)
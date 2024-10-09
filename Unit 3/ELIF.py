# the if statement has 2 buddies
# the first buddy is the else statement

x = 10
if x > 0:       #not every if needs an else
    print("x is a positive number.")
# the second little buddy is the ELIF statement (else if)
elif x < 0:
    print("x is a negative number.")
else:           # else allways needs an if
    print("x is zero.")


light = input("What color is the light?\n> ")
if light.lower() == "green":
    print("GO")
elif light.lower() == "yellow":
    print("STOP IF SAFE")
elif light.lower() == "red":
    print("STOP")
else:
    print("YIELD")


if x > 5:
    print("x is greater than 5")
elif x > 8:
    print("x is greater than 8")

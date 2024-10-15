# nested if statements

prime = True
cost = 20
age = 17
consent = False

if prime == True:
    if age >= 18:
        print("FREE SHIPPING APPLIED!")
    elif consent == True:
        print("FREE SHIPPING APPLIED!")
    else:
        print("No free shipping for you...")
elif cost <= 25:
    if age >= 18:
        print("FREE SHIPPING APPLIED!")
    elif consent == True:
        print("FREE SHIPPING APPLIED!")
    else:
        print("No free shipping for you...")
else:
    print("No free shipping for you...")

# decide if we need to take an umbrela
#need umbrela if it is raining and you are going outside that day

raining = input("Is it raining outside>\n> ")
outside = input("Do you plan on going outside?\n> ")

if raining.lower() == "yes":
    outside = input("Do you plan on going outside?\n> ")
    if outside.lower() == "yes":
        print("BRING AN UMBRELA")
    else:
        print("NO UMBRELA")
else:
    print("NO UMBRELA")
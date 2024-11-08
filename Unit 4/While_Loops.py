# Theres a couple types of loops in python
# The for loop lets you iterate through a list
# great for looping a set number of times
# but what if we need to loop an uncertain number of times????
# ex. Entering your password
# you can't know how many trys it will take.



real_pass = "ninjalowtaper"
entered_pass = ""
attempts = 0

while entered_pass != real_pass:
    #ask for password
    entered_pass = input("Please enter the password\n>")

    # check if password is correct
    if entered_pass == real_pass:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
        attempts = int(attempts)
        attempts += 1
        attempts = str(attempts)
        print("attempt number " + attempts)
        print("try again...")

print("Welcome!")

#with while loops you need to be carful for infinite loops
# an infinant loop hapens when you enter a loop that can never be escaped
# like black holes
# Don't create a black hole

#real world ex.

user_input = ""

while user_input != "exit":
    user_input = input("Enter something!")
    print("Type 'exit' to quit")
    print("You typed: " + user_input)

print("All done!")

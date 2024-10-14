# Exception Handling
# Write a program that askes for two numbers and divides them

# if = try
# elif = except with error type
# else = except

def divide_two_numbers():
    try:        # We always enter the try block, there is no condition
        x = int(input("What is the first number?\n> "))
        y = int(input("What is the second number?\n> "))
        print(x / y)
    except ZeroDivisionError:
        print("Cannot divide by zero, try again")
        divide_two_numbers()
    except ValueError:
        print("Please enter a valid nummerical number, please try again")
    except:     # If anything in the try block creates an error
            # the try block stops imediatly and then the except is ran
            # The rest of the try block is skipped
            # if try block executes without an error the except is skipped
            # the only way to get into the except is to throw an error
        print("I don't know what you did but try again.")
        divide_two_numbers()

divide_two_numbers()

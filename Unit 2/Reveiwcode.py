# 2 basic functions
# Know this is a function because it has () at the end
# Stuff that goes in () are called parameters
# parameters are info the function needs to run
print("Hello World!")   # "Hello World!" is the parameter
input("What is your favorite animal?\n>")
# \n is called an escape character
# input is never requried, only use when necasery

# Variables: a way to store data for later use in the program
# Syntax (grammar)
# <name> = <value>
x = 5       # x is the variable name, 5 is the value
#syntax naming convention - all lowercase
#  CONCISE: Short and descriptive
username = "Wolff"      # define string
fav_animal = "Wolf"     # define string
total_poptarts = 12         # define integer
percent_complet = 23.52     # define float
is_cool = True      # define Boolean  (True/Fa;se values)
first_letter = 'c'      # define character

total_poptarts = 8      #reasining variable

# Arithmatic operators (basic math)
#   +   -   *   /   **  %   //
print(2 + 2)
print("2 + 2")      #>22
print("cat" + "dog")        #>catdog
print("cat" * 3)        #>catcatcat
print("cat" + 3)        #>ERROR
print("cat" * "dog")        #>ERROR

my_variable = 2 + 3

# Make working programs
#1. add two numbers using input
x = int(input("What is x?\n>"))  # input returns a string

y = input("What is y?\n>")
y = int(x)

print(x + y)        #Print results

#2. Convert Celcius to Farenheight
temp_celcius = input("What is the temperature in celcius")
temp_celcius = int(temp_celcius)
temp_farenheight = (temp_celcius *  1.8) + 32
print(temp_celcius + " deg C is " + temp_farenheight + " deg F")

# Conversion functions
str()
int()
float()
bool()
bin()

# Functions are a lot like variable
# have names
# can be recaled from memory by calling their name
# store info
# variables store a value, functions store code
# def <name>():
def potato():
    print("tomato")

potato()        #every function call needs parenthesis wether it has parameters or not

def jump(how_high):
    how_high = str(how_high)
    print("You jumped " + how_high + " inches high.")

jump(14)

# Scope is Global vs Local variables
todd = "cool guy"       #global variable

def my_function():
    smith = "not cool guy"
    print(todd)
    print(smith)    #works

# Return functions
# Functions can also return values
# value that is returned is sent back to where function is called
def jfunction(x, y):
    solution = x + y
    return solution

answer = jfunction(10, 16)
print(answer)

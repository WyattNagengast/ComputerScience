#For Loops
#This is a big deal
#For loops allow the proggramar to repeat or what we call loop

#Write a program that prints the numbers one through ten
#Each on a new line

fav_foods = ["Chicken Wings", "Burritos", "Ribs"]

#for <var> in <list>:

for i in range(90, 101):
    print(i)

for food in fav_foods:
    print(food)
    #runs all the lines in the for loop
    #When it reaches the bottom of the list, it runs again
    #and moves on to the next item in the list
    #It ends when there are no list items left


for i in range(10, 0, -1):
    print(i)

num = [1, 2, 3, 4, 5]
sum = 0

for n in num:
    sum = sum + n
print(sum)

#Square each number
newlist = []

for nir in num:
    newlist.append(nir*nir)
print(newlist)

#character count

stringy = input("Please enter a string\n>")
numvowel = 0
for s in stringy:
    if s.lower() in ["a", "e", "i", "o", "u"]:
        numvowels = numvowels + 1

print(numvowels)

#print multiplacation table
try:
    multi = int(input("Gimme an int yo!\n> "))
except:
    print("womp womp")

for i in range(0,multi+1):
    print(str(multi) + " x " + str(i) + " = " + str(multi*1))

#list of names
names = ["Pete", "John", "Luke", "Paul"]
for name in names:
    print("Hello, " + name + "!")


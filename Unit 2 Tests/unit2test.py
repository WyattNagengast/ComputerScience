#1
Sandwitch = input("What is your favorite sandwitch?\n>")    #askes favorite sandwitch
Hate = input("What is the thing you hate the most?\n>")     #askes for hate
Movie = input("What is your favorite movie?\n>")            #askes favorite movie
print("Your favorite snadwitch is " + Sandwitch + ".\nThe thing you hate the most is " + Hate + ".\nYour favorite movie is " + Movie + ".")     #print answers to questions

#2
def add_three():        #creates function
    print(x + y + z)    #prints x + y + z

x = input("x\n>")   #askes for x
x = int(x)          #makes x int
y = input("y\n>")   #askes y
y = int(y)          #makes y int
z = input("z\n>")   #askes z
z = int(z)          #makes z int

add_three()     #runs function

#3
def data_three():       #make function
    word = input("Word\n>")     #askes word
    integer = input("Integer\n>")       #askes integer
    float1 = input("Float\n>")      #askes float
    answer = integer + float1       #adds integer and float
    print(word * answer)        #print sum and answer concatenated

data_three()        #play function

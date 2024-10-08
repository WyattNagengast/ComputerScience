#String Functions
# String functions are a group of functions that modifiy a strings
# .lower()
# .upper()
# .capitalize() changes entire string to lowercase, then cappitlies the first letter
# .title() changes entire string to tittlecase (capitlizes first letter of every word)
# .swapcase() inverses capitlization of each character

x = "Lord of the Rings"
x = x.lower()
print(x)        # prints lord of the rings

answer_1 = int(input("Give a number equal to or less than 50\n> "))
answer_2 = str(input("What is the name of the movie that starts the first word with a P and the second word with a R?\n> ")).title()
answer_3 = str(input("What is the part of a computer that connects all the other parts?\n> ")).capitalize()
answer_4 = str(input("True or False: RAM stands for random acess memory.\n> ")).capitalize()
answer_5 = str(input("Who was the best pig to have ever lived?\n> ")).upper()
def tally_score():
    score = 0
    if answer_1 <= 50:
        score = score + 1 
    if answer_2 == "Pacific Rim":
        score = score + 1
    if answer_3 == "Motherboard":
        score = score + 1
    if answer_4 == "True":
        score = score + 1
    if answer_5 == "TECHNOBLADE":
        score = score + 1
    print(str(score) + "/5")

tally_score()
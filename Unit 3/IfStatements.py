# If Statements evaluate  boolean expressions!
# Make decisions about which code to run next

# Take a temp
# print <temp> is hot if it is >= 80
# Otherwise, print <temp> is not hot
temp = input("what is the temperature in F?\n> ")
temp = int(temp)

# if <boolean expression>:
if temp >= 80:
    print(str(temp) + "F(degres) is hot!")

else:       #Otherwise....
    print(str(temp) + "F(degres) is not hot...")
#not all if statments need an else in fact none need an else
#else statements are optionnal
#else statements must have a corisponding if statement
# If statements can only have one else

# create program that askes for password
#if password correct print access granted
#else print access denied
# password is skipidi68
real_pass ="skipidi68"
password = input("Whats the password\n> ")
if password == real_pass:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")

# activity 2. electric boogalo
# create a five question quiz that prints your score at end
# choose any five questions

answer_1 = input("Give a number equal to or less than 10 but greater than 0\n> ")
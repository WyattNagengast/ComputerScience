# Dictionary is a type of collection like a list
# a list is a collection of items in a sequence
# a dictionary is different
# dictionaries store data in key-value pairs
# You can retrieve data quickly by using a unique key
# instead of retrieving it by index

#ex.
# lists use [], and dictionaries use {}

wyatt = {
    "name": "Wyatt",
    "age": 15,
    "city": "St. Michael",
    "pets": 4,
    "height": 6
}

# each kew must be unique

# retrieve values from a dictionary
print(wyatt["name"])    # prints the name
print(wyatt["age"])     # prints the age

# this will error if you give a key that does not exist
#print(wyatt["nation"]) this errors!

# .get allows you to retrieve a calue without erroring
# when the key dosen't exist
# the second parameter is what is giving if the value is not found
print(wyatt.get("height"))
print(wyatt.get("country", "Country not found"))

# You can add new values to an existing dictionary
wyatt["country"] = "USA"

# modify
wyatt["age"] = 16

# remove
wyatt.pop("pets")

# Iterate through a dictionary usig a for loop
for key, values in wyatt.items():
    print(key + " = " + str(values))

#dictionary Fuctions
print(wyatt.keys())             #returns all the keys
print(wyatt.values())           #returns all the values
print(wyatt.items())            #prints everything
print(wyatt.clear())            #removes all the items
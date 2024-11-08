
students = {
    "Ryan": "A-",
    "Bill": "A",
    "Dillanger": "B+",
    "Matt": "A",
    "Jerry": "B"
}

matt = {
    "name": "Matt",
    "age": 14,
    "grade": "A"
}

matt["grade"] = "A+"
print(matt.items())

movies = {
    "Pacific Rim Uprising": "March 23, 2018",
    "Pacific Rim": "July 12, 2013",
    "Pirates of the Caribbean: The Curse of the Black Pearl": "July 9, 2003"
}

x = input("Please give a movie\n> ")
movies[x] = input("Please provide the release date of the movie\n> ")
print(movies.items())


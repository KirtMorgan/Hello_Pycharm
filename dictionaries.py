# Dictionaries
# Used to keep information with keys and value pairs
# In dictionaries you look at a key instead of a index number
# Key = reference to object
# Value Whatever data is stored - could be a string, list, number even other dictionaries

# Defining/Creating a dictionary, also known as hash in ruby or object in javascript
# student_1 = {
#     'name': 'Kirt',
#     'stream': 'Dev-Ops',
#     'grade': 5,
#     'completed modules': ['Git', 'Git-Hub', 'Business Week', 'Variables', 'Data Types']
# }
# Checking the class
# print(type(student_1))
# Access values of keys
# print(student_1['stream'])
# print(student_1['completed modules'][2])

# Exercise
# student_2 = {
#     'name': 'Iron Man',
#     'stream': 'Saving the world',
#     'grade': 10,
#     'completed modules': ['Weaponry', 'Warfare', 'Justice', 'Advanced Fighting', 'Being Awesome']
# }
# student_2['completed modules'] += ['Armour', 'Guns']
# print(student_2)
# print(student_2['completed modules'][2])
# print(student_2['completed modules'].count('Warfare'))
# weapons = 'Missles'
#
# student_2['completed modules'].append(weapons)
# print(student_2['completed modules'][-1])

# Dictionary Update operator
# d = {1: "one", 2: "three"}
# d1 = {2: "two"}
#
# # updates the value of key 2
# d.update(d1)
# print(d)
#
# d1 = {3: "three"}
#
# # adds element with key 3
# d.update(d1)
# print(d)


# Q1: Write a program that display your enterend name
name = input('Enter your name: ')
print(f"Good Afternoon {name}") # f-string is used to insert the value of the variable name inside the string
# Q2: Write a program that display user name and date in the string
sentance = '''Dera <Name> you are selected in the Microsoft on <Date>'''
print(sentance.replace('<Name>', "Manan").replace('<Date>', "2025-06-18")) # replace() function is used to replace the value of th
# Q3: Find the double space in a string
string = "Hello  World"
print(string.find('  ')) # find() function is used to find the index of the first
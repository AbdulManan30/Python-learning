# # Problem 1
# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
# Twinkle, twinkle, little star,
# How I wonder what you are!''')

# # Problem 2
# print(5*1)
# print(5*2)
# print(5*3)
# print(5*4)
# print(5*5)
# print(5*6)
# print(5*7)
# print(5*8)
# print(5*9)
# print(5*10)

# # Problem 3
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

# Problem 4
import os
directoryPath = "/home/abdul-manan/Desktop"
contents = os.listdir(directoryPath)
for item in contents:
    print(item)
    
    
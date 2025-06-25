f = open('learning.txt')
print(f.read())
f.close()
# The same code can be written using with statement like this:
with open('learning.txt') as file:
    print(file.read())
    
# You don't have to close this if you use with statement
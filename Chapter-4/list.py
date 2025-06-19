frinds = ['Manan', 283, 38.4, True]
frinds[2] = 1000.45 # Strings are immutable and list are mutable
# print(frinds)
# Slicing of List
print(frinds[0:3]) # output will be ['Manan', 283, 38.4]

# list and string have a major difference that string saved in Stack memory and list saved in Heap memory.
# Stack memory is a memory that give us a copy of original Primitive Data like String and int, and Heap is also a memory that give us the refernce of original Non-primitive Data like list and object

# Some important List methods
listOfItem = [4,5,6,3,6,4321,4567,1,2,3,4]
listOfItem.append('Kuki') # it will append 'kuki' in the last of the list
listOfItem.remove(4) # it will remove first element from the list
listOfItem.reverse() # it will reverse the whole list
listOfItem.clear() # it will clear all values from the list
print(listOfItem)


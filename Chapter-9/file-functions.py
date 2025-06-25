# file = open('learning.txt')
# readlines mode

# lines = file.readlines()
# print(lines)
# for item in lines:
#     print(item.strip())
    
# readline mode

# line1 = file.readline()
# print(line1)
# line2 = file.readline()
# print(line2)
# line3 = file.readline()
# print(line3)

# append mode
file = open('learning.txt', 'a')
file.write('\nI am a new line')
file.close()
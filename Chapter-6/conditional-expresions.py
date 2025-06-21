
# userEnteredNo = int(input('Please enter an number: '))
userEnteredAge = int(input('Please enter your age: '))
# if we want an centain condion to execute the code then we use if, else, elif
# if userEnteredNo%2 == 0:
#     print('The number is even')
# else:
#     print('The number is odd')

if (userEnteredAge > 10 and userEnteredAge<18):
    print('You can not drive because you are ander 18')
elif (userEnteredAge < 0):
    print('You are entering an invalid age')
elif (userEnteredAge > 70):
    print('You can not drive because you are 70 plus')
else:
    print('Congrates!! you are able to drive')

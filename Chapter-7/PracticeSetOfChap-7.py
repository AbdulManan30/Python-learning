# # Q1
# i = input("Please enter the number that you want table: ")
# for x in range(1, 11):
#     print(f"{i} * {x} = {int(i) * x}")

# # Q2
# l = ['Manan', 'Salman', 'Sapna', 'Noman']
# for z in l:
#     if(z.startswith('S')):
#         print(f'Hello {z}')

# Q3 Attempt Q1 using while loop
# i = input("Please enter the number that you want table: ")
# y = 1
# while(y<=10):
#     print(f'{i} x {y} = {int(i)*y}')
#     y+=1

#  Q4
# u = int(input("Please enter your number: "))
# sum = 0
# i = 1
# while(i<=u):
#     sum +=i
#     i+=1
# print(sum)

# Q5
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''
# for f in range(1, 6):
#     for j in range(1, 6):
#         print("*", end=" ")
        
#     print()
    
# Q6
'''
*
* *
* * *
* * * *
* * * * *
'''
# row = int(input('Enter pattern number: '))
# for i in range(1, row+1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()
    
'''
 * * * * *
 * * * *
 * * *
 * *
 *
'''
# for g in range(rows, 0, -1):
#     for h in range(g):
#         print('*', end=" ")
#     print()

# Q
g = int(input('Enter table number: '))
for f in range(10, 0, -1):
    print(f'{g} * {f} = {g*f}') 
    
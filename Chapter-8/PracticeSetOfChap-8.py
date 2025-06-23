# Q1
# a = 1
# b = 2
# c = 3


# def gretestNumber(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
# result = gretestNumber(a, b, c)
# print(f'Gretest number is {result}')

# Q2
# def End():
#     print("Manan", end=" ")
#     print("Kuki", end=" ")
    
# End()

# Q3
# number = int(input("Enter Your number: "))
# def sum(n):
#     if(n==1):
#         return 1
#     a = sum(n-1) + n
#     return a
# print(sum(number))

# Q4
'''
***
**
*
'''
rows = int(input("Enter your number: "))
def patternPrinter(n):
    if(n==0):
        return
    print("*" * n)
    patternPrinter(n-1)
    
patternPrinter(rows)

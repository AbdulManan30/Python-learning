# Q1
"""
try:
    with(
    open('text.txt') as f1,
    open('text2.txt') as f2,
    open('text3.txt') as f3
):
        print(f1, f2, f3)

except:
    print('No such file or directory: text.txt')

print("Thank You")
"""
# Q2
"""
lis = [1, 2, 3, 4, 5, 6, 7, 8]
for i, item in enumerate(lis):
    if i == 2 or i == 4 or i == 6:
        print(item)
    if i == 6:
        break

"""
# Q3
"""
i = int(input("Enter your table number: "))
table = [i*x for x in range(1,11)]
print(table)
"""
# Q4
"""
a = int(input("Enter your 1st number: "))
b = int(input("Enter your 2nd number: "))
if b == 0:
    raise ZeroDivisionError
else:
    print(a / b)

"""

# Q5
i = int(input("Enter your table number that you want: "))
table = [i * x for x in range(1, 11)]
with open("table.txt", "a") as f:
    f.write(f"Table of {i}: {table}\n")

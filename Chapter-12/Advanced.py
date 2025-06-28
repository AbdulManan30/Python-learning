# Walrus operator
if (n := [1, 2, 3, 4, 5]) == [1, 2, 4, 3, 4, 5]:  # it also define The list
    print("Yes both are same")
# print(n)

# Types
name: str = "Manan"  # it make code more reabadle for coders
age: int = 20


def sum(a: int, b: int) -> int:
    return a + b


sum(5, 6)


# Typing Module
from typing import List, Union, Tuple, Dict

# List
my_list: List[int] = [1, 2, 3, 4, 5, "Manan"]
# Tuple
my_tuple: Tuple[int, str] = (1, "Manan")
# Dict
my_dict: Dict[str, int] = {"Manan": 20, "Rohan": 30}
# Union
my_union: Union[int, str] = (1, "Mnan")


# Match Case
def https_status(St):
    match St:
        case 200:
            return "Ok"
        case 201:
            return "Created"
        case 400:
            return "Bad Request"
        case _:
            return "Not Found"


# print(https_status(201))

# Merging Dictionaries

# There are two ways to merge dictionaries in python
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# dict3 = {**dict1, **dict2}
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = dict1 | dict2
# print(dict3)

# With statement with two values
# with(
#     open("file1.txt", "r") as file1,
#     open("file2.txt", "w") as file2
# ):
#     print(file1)

# Try and Exception
# try:
#     i = int(input("Enter your number: "))
#     print(i)
# except Exception as e:
#     print(e)

# except ValueError as e:
#     print(e)

# except ZeroDivisionError as e:
#     print(e)
# except:
#     print("Please enter a valid number")

# print("Thank you") # It will print because our code is not crashed if we don't use try except it will crashed


# Raise Error
# a = int(input("Enter your 1st number: "))
# b = int(input("Enter your 2nd number: "))
# if b == 0:
#     raise ZeroDivisionError("You can't divide by zero") # Raise will crashe the code
# else:
#     print(a / b)

# Try, except, else and finally

# try:
#     a = int(input("Enter a number: "))
#     print(a)
# except:
#     print("Please enter a valid number")
# else:
#     print("done") # It will only execute when try is successful


# Finally we use in a function that return some value and with the help of finally we can write code after return statement
def main():
    try:
        a = int(input("Enter a number: "))
        return a
    except:
        return "Please enter a valid number"
    finally:
        print("done")  # It will also execute after the return statement


# print(main())

# enumerate
lis = [1, 233, 4676, 78, 9898, 8]
for index, item in enumerate(lis):
    print(f"The index of {item} = {index}")

# List Comrehension
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squaredList = [i * i for i in lis]
print(squaredList)

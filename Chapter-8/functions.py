"""
A function in Python is a reusable block of code that performs a specific task.
Functions help organize code, make it more readable, and avoid repetition.
You define a function using the def keyword, followed by the function name and parentheses which may include parameters.
The function body contains the code to execute, and you can optionally return a value using the return statement.
"""

# # Example: 1
# def avg():
#     # This code calculate the average of numbers enterd by user
#     a = int(input('Eeter your number: '))
#     b = int(input('Eeter your number: '))
#     c =  int(input('Eeter your number: '))
#     print(f'Average of these number is {(a+b+c)/3}')
# avg() # function calling

# # Example: 2 with a argument

# def greet(name):
#     # name is a argument in this function
#     """This function greets the person passed as a parameter."""
#     print(f"Hello, {name}!")

# greet("Manan") # Manan is a parametter in this code

# # Example: 3 with return statement

# def returnFunc(name):
#     # return means: Give this value back to the place where the function was called
#     return (f"Hello, {name}!")
# result = returnFunc("Noman Aijaz")
# print(result)

# Example: 4 with defult value

# def default(name, ending = "Thank you"):
#     # ending is a defult value in this function.
#     return (f"Hello, {name}! {ending}")

# result2 = default("Noman Aijaz")
# result3 = default("Noman Aijaz", "Thanks")
# print(result2)
# print(result3)

# Example: 5 with Recursion

"""What is Recursion in Python?
Recursion is a technique in which a function calls itself to solve a problem.

In Python (and many other languages), recursion is used when a problem can be broken down into smaller versions of itself.

Simple Definition:
Recursion is when a function calls itself until it reaches a base condition.

Key Parts of Recursion:
Recursive call – when the function calls itself

Base case – the stopping condition (to prevent infinite loop)

Example: Factorial using Recursion"""


def factorial(n):
    if n == 1:  # base case
        return 1
    return n * factorial(n - 1)  # recursive call


print(factorial(5))

"""
Output like this
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1
= 120
"""

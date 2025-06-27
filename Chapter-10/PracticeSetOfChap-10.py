# Q1 Create a class that store data of programmers who worked on microsoft
"""
class Programmers:
    def __init__(self, name, age, company, position):
        self.name = name
        self.age = age
        self.company = company
        self.position = position


p = Programmers("Manan", 18, "Microsoft", "Intern")
print(p.name, p.age, p.company, p.position)

"""


# Q2 Create a class of a calculator that can give us square, and cube
"""
class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The Square of {self.num} = {self.num ** 2}")

    def cube(self):
        print(f"The Cube of {self.num} = {self.num ** 3}")

    def square_root(self):
        print(f"The Square Root of {self.num} = {self.num ** 1/2}")

    def cube_root(self):
        print(f"The Cube Root of {self.num} = {self.num ** (1/3)}")

# Example usage
x = Calculator(8)
x.square()
x.cube()
x.square_root()
x.cube_root()
"""
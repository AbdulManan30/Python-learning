"""
🧬 What is Inheritance in Python?
Inheritance is a feature in Python (and most object-oriented languages) that lets you create a new class (child class) from an existing class (parent class).
It helps in code reusability, extensibility, and organization.

🔷 Why Use Inheritance?
Reuse existing code

Add or override features of the parent class

Implement polymorphism (same function behaves differently)


"""


# Basic Syntax
class Parent:
    def greet(self):
        print("Hello from Parent!")


class Child(Parent):
    pass


c = Child()
c.greet()  # Output: Hello from Parent!


#  Overriding Parent Methods
class Parent:
    def greet(self):
        print("Hello from Parent!")


class Child(Parent):
    def greet(self):
        print("Hello from Child!")


c = Child()
c.greet()  # Output: Hello from Child!


# super() Function
# Used to call the parent class methods inside the child class.
class Parent:
    def show(self):
        print("Parent Show")


class Child(Parent):
    def show(self):
        super().show()
        print("Child Show")


c = Child()
c.show()
# Output:
# Parent Show
# Child Show


# Types of Inheritance
# 1, Single Inheritance
class A:
    pass


class B(A):
    pass


# 2, Multilevel Inheritance
class A:
    pass


class B(A):
    pass


class C(B):
    pass


# 3, Multiple Inheritance


class A:
    pass


class B:
    pass


class C(A, B):
    pass


# 4, Hierarchical Inheritance
class A:
    pass


class B(A):
    pass


class C(A):
    pass


# Example (Real-life)
class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")


d = Dog()
c = Cat()
d.sound()  # Bark
c.sound()  # Meow

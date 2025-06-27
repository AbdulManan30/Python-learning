class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        

manan = Employee("Abdul Manan", 17, 80000)
print(manan.name, manan.age, manan.salary)  # Output: Abdul Manan 17 80000
class Employee:
    def __init__(self):
        self.name = "Manan"  # This is an Class Attribute
        self.language = "Py"
        self.salary = 120000

    def getUserInfo(self):
        print(f"The Language is {self.language} and name is {self.name} ")

    @staticmethod
    def getinfo():  # if we don't want to receive self then we use @staticmethod
        print("Good Morning")


data = Employee()
data.caste = "Pirzado"  # This is an Object Attribute
data.getinfo()
data.getUserInfo()
print(data.caste)

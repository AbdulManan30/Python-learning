class Employee:
    a = 1
    @classmethod
    def show(self):
        print(f"Hello a value is {self.a}")

x = Employee()
x.a = 77
x.show()
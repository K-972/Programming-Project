class Person():

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def UpdateAge(self):
        self.age = input("Enter new age: ")

    def InputValues(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")

    def SayHello(self):
        print(f"Hello {self.name}.")

class employee(Person):

    def __init__(self, name, age, position) -> None:
        super().__init__(name, age)
        self.position = position

    def SayHello(self):

        print(f"Hello {self.name} you are a {self.position}.")




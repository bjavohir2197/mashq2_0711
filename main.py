class Animal:
    def __init__(self):
        print("Animal yaratildi")


class Dog(Animal):
    def __init__(self):
        super().__init__()  
        print("Dog yaratildi")

it = Dog()

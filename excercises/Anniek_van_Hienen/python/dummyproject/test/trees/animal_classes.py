class Animal:
    # this is a class
    def __init__(self):
        pass
    def make_sound(self):
        print("I make a sound!")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Dog(Animal):
    def make_sound(self):
        print("Woof")

class Chicken(Animal):
    def make_sound(self):
        print("Tock tock")

    def lay_egg(self):
        print("I made an egg!")


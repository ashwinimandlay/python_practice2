# WAP define a type named person having name attribute
# and talk method

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"hi i am {self.name}")
    # self.name gives the name attribute of the current
    # person object


john = Person("john smith")
john.talk()
print(john.name)

bob = Person("bob smith")
bob.talk()
# each object is a different instance of a person class

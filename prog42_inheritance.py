# inheritance
# for reusing codes
# if we define a class of dogs with method walk and then
# define a class of cat with same method that is inefficient
# instead we define class mammal and let dog and cat inherit it
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass
    # python doesn't like blank class so we use pass


class Cat(Mammal):
    def meow(self):
        print("Meow")


# always define objects to call classes
dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.walk()
cat1.meow()

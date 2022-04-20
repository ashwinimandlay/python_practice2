# constructors in classes
# initializing attributes in the class itself
class Point:
    def __init__(self, x, y):
        # self is reference to the current object
        # in this case with respect to point1
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)
# this is same as point1.x =10 , point1.y = 20
print(point1.x)


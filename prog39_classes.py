# classes is template/ blueprint of objects
# used to define new types and these types can have
# dot methods that we define

# we use pascam naming convention i.e first letter of
# every word of class is capital (unlike function or variable)
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")
    # both draw and move are now dot method of point
    # such as message.append which is already in python


# now we can define new objects in a class
# objects are the actual instances of class
point1 = Point()
point1.draw()
# we can also define attributes, that are like variables
# to our objects
# we can also use constructor to initialize attributes of obj
point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point()
# print(point2.x) this statement doesn't have x attribute

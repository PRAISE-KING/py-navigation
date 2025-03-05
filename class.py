

# we use class to define new types of classes e.g Point
# these types can have methods that are defined in the body of a class e.g def draw()
# the types are always capitalised e.g Point or PraiseKing

# attributes - instance of an object , are like variables belonging to a particular object e.g Point(20),,20 is an attribute
# object - instance of a class ,are called as functions e.g Point()
# objects can be stored in a variable e.g point1 = Point()
# methods - defined inside a class e.g def draw()

class Pointt:
    def draw(self):
        print("I'm drawing")

    def move(self):
        print("I'm moving")

point1 = Pointt()
point1.x = 10
point1.draw()
print(point1.x)

point2 = Pointt()
point2.x = 11
print(point2.x)

# point1 is completely different object from point2


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CONSTRUCTORS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# is a function that gets called at the time of creating an object...method used to construct or crete an object
# instead of using point.x to create values for x we'll use a constructor

class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y


    def draw(self):
        print("I'm drawing")

    def move(self):
        print("I'm moving")


point3 = Point(10 , 23)
print(point3.x)
print(point3.y)

# we can modify or changde the values of x and why using the do function

point3.y = 33
point3.x = 16
print(point3.x)
print(point3.y)


# ......................exercise........................
class Person:
    def __init__(self , name):
        self.name = name
    def talk(self):
        print(f'hey {self.name} is talking')

person = Person('Praiseking')
person.talk()

person1 = Person('Ochieng')
person1.talk()

# example 3
class Paint:
    def __init__(self , office , bedroom):
        self.office = office
        self.bedroom = bedroom

    def painting(self):
        print(f"You'll paint {self.office} Offices")

    def sleep(self):
        input(f"Where is {self.bedroom}'s bedroom ?")

painter1 = Paint('The Royale' , 'Praiseking')
painter1.painting()
painter1.sleep()
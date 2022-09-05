# "In multiple inheritance, a class is derived from more than one class i.e. multiple base classes. 
# The child class, in this case, has features of both the parent classes."

# As the name implies, python's multiple inheritance is when a class inherits from more than one class. This concept is very similar to multilevel inheritance, 
# which also is our next topic of this course. It is also nearly the same as a single-level inheritance because it contains all of the same functionality, 
# except for the number of base classes. 

# While using the concept of multiple inheritance, the order of placing the base classes is very important. Let us clear the concept using an example. 
# Suppose we have a child class named Child, and it has two base classes, named Base1 and Base2.

# Example:

class Base1:
      def func1(self):
            print("this is Base1 class")
class Base2:
      def func2(self):
            print("this is Base2 class")

class Child(Base1 , Base2):
      def func3(self):
            print("this is Base3 class")

obj = Child()

obj.func1()
obj.func2()
obj.func3()

# Output:

# this is Base1 class

# this is Base2 class

# this is Base3 class

# Now, when we are looking for some attribute, let it be a constructor. Then the program will search the current class i.e., 
# the Child1 class first. If it does not find it in the Child1, it will look in the base class that is present at the leftmost side, 
# which is Base1. After that, the program will start moving from left to right in a sequential manner, hence searching the Base2 class at the end. 
# We should always give attention to the ordering of the base classes because it helps us a lot when multiple classes 
# contain the same methods and also in method overriding. 

# Method Overriding:
# Override means having two methods that have the same name. They may perform same tasks or different tasks. 
# In python, when the same method defined in the parent class is also defined in the child class, 
# the process is known as Method overriding. This is also true when multiple classes have the same method and are linked together somehow.  

# There are few rules for Method overriding that should be followed:

# The name of the child method should be the same as parents.
# Inheritance should be there, and we need to derive a child class from a parent class
# Both of their parameters should be the same. 

# In this case, the child method will run, and the reason for which, we have discussed in the paragraph above, related to ordering. 
# Multiple inheritance is based on the same concept on which the single inheritance is based on i.e., DRY (do not repeat yourself). 
# Multiple inheritance makes it easier to inherit methods and attributes from base classes that implement the functionality. 
# When done right, we can reuse the code without having to copy-and-paste a similar code to implement interfaces.   







class Employee:
    no_of_leaves = 8
    var = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game =game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

class CoolProgramer(Player, Employee):  # yaha parent classes ka sequence matter karta he
                                        # yaha pe multiple inheritance banaya he 

    language = "C++"
    def printlanguage(self): # apna constructor banaya
        print(self.language)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Player("Shubham", ["Cricket"])

karan = CoolProgramer("Karan", ["Cricket"]) # karan can use both classes # agar hame 3 argumenst use karne honge to hame Employee class pahle likhana padega
# rohit = CoolProgramer("Rohit", 545454, ["Football"]) # this will throw error because in parent class sequence we write player first and then Employee so player has printdaetails only two arguments

# agar hame parent class ka koi constructor or function use karna hoga to ...hame sequence ka dhyan rakhana padeega...jo class first write kiya hoga uska constructor or class method or anything hi use hoga...
# aur uske no of arguments bhi match hone chahiye nahi to error dega 

det = karan.printdetails()
karan.printlanguage()

# d = rohit.printdetails()
print(det)

print(karan.var) # ye player ka var = 9 print karega ...because player first likha he ...agar Employee first hota to var = 8 ata



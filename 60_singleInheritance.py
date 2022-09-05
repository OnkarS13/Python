# “Inheritance is the ability to define a new class(child class) that is a modified version of an existing class(parent class)”

# Syntax:
# class Parent_class_Name:
# #Parent_class code block
# class Child_class_Name(Parent_class_name):
# #Child_class code block

# The above syntax consists of two classes declared. One is the parent class or by other means, the base class, 
# and the other one is the child class which acts as the derived class.

# Two common terms related to inheritance are as follows:
# Parent: The parent class is the one that is giving access to its methods or properties to the child class or derived class.
# Child: Child class is the one that is inheriting methods and properties from the parent class.
# The class that is inheriting, i.e., the child class, can inherit all the functionality of the parent class and add its functionalities also. 
# As we have already discussed that each class can have its constructors and methods, so in case of inheritance the child class can make and 
# use its constructor and also can use the constructor of the parent class. We can simply construct it as we did for the parent class but OOP 
# has provided us with a simple and more useful solution known as Super().

# We will be discussing super() and overriding in our Super() and Overriding In Classes tutorial of the course.

# Single inheritance exists when a class is only derived from a single base class. Or in other words when a child class is using the methods 
# and properties of only a single parent class then single inheritance exists. Single inheritance and Multiple inheritance are very similar concepts, 
# the only major difference is the number of classes. We will see Multiple Inheritance in our next tutorial.

# Different forms of Inheritance:
# Single inheritance: When a child class inherits from only one parent class then it is called single inheritance.
# Multiple inheritance: When a child class inherits from multiple parent classes then it is called multiple inheritance
# Below is an example of single inheritance in Python.

class Parent():
    def first(self):
        print('Parent function')
        
class Child(Parent):
    def second(self):
        print('Child function')

object1 = Child() # object is created of child class

object1.first()
object1.second()
print("------------------------------------------------------------------------------")
# Output: 

# Parent function
# Child function

# Advantages of Inheritance:
# It increases the code’s reusability as we do not have to copy the same code again to our new class.
# It makes the program more efficient.
# We can add more features to our already built class without modifying it or changing its functionality.
# It provides a representation of real-world relationships.
# In this tutorial, we have discussed the Inheritance concept. Inheritance is among the most significant concepts in object-oriented programming technique which provides code reusability, readability and helps in building optimized and efficient code.








class Employee:
    no_of_leaves = 8

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


class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"

# All the functions of Class Employee can be used by Instances of Programmer class

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Programmer("Shubham", 555, "Programmer", ["python"])
karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])

print(karan.no_of_holiday)

print("-----------------------------------------------------")
print("This is by class Employee ")
print(harry.printdetails())
print(rohan.printdetails())

print("-----------------------------------------------------")

print("This is from Employee class----> ", shubham.printdetails())
print("This is from Programmer class-----> ", shubham.printprog())

print("-----------------------------------------------------")

print("This is from Employee class----> ", karan.printdetails())
print("This is from Programmer class-----> ", karan.printprog()) # here karan.printprog() .......() This is important
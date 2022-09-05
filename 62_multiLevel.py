# What is Multilevel Inheritance in Python?
# In multilevel inheritance, a class that is already derived from another class is derived by a third class. 
# So in this way, the third class has all the other two former classes' features and functionalities. The syntax looks something like this:

# class Parent1:
#     pass
# class Derived1(Parent1):
#     pass
# class Derived2(Derived1):
#     pass
# Now let us dive into the priority brought by the ordering of the class. Suppose that we are looking for a constructor or a value for any variable. 
# Our program will first check our current class i.e., Derived2, for it. If nothing is found, 
# then it will move towards Derived1 and in order at last towards Parent1 until it finds the constructor or variable in the way.

# If we have the same method or variable in the base and derived class, then the order we discussed above will be followed, 
# and the method will be overridden. Else, if the child class does not contain the same method, then the derived1 class method 
# will be followed by the sequence defined in the paragraph above.

# For Example:

class level1:
      def first(self):
            print ('code')

class level2(level1): #inherit level1
      def second(self):
             print ('with')

class level3(level2): #inherit level2
      def third(self):
            print ('harry')

obj=level3()
obj.first()
obj.second()
obj.third()

# Rules for Method overriding:-
# There are few rules for Method overriding that should be followed:

# The name of the child method should be the same as parents.
# Inheritance should be there, and we need to derive a child class from a parent class
# Both of their parameters should be the same.

# Multiple inheritance VS. Multilevel inheritance

# Multiple inheritance                                         Multilevel inheritance

# Multiple Inheritance is where a class inherits               In multilevel inheritance, we inherit from a derived class, making that derived class a base class for a new class.
# from more than one base class.

# Sometimes, multiple Inheritance makes the                   Multilevel Inheritance is widely used. It is easier to handle code when using multilevel inheritance.
# system more complex, that’s why it is not widely used.

# Multiple Inheritance has two class levels;                  Multilevel Inheritance has three class levels, which are base class, intermediate class, and derived class.
# these are base class and derived class.

# Advantages of Inheritance :-

# 1. It reduces code redundancy.
# 2. Multilevel inheritance provides code reusability.
# 3. Using multilevel inheritance, code is easy to manage, and it supports code extensibility by overriding the base class functionality within child classes



class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdances(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad() # three instances are created
larry = Son() # three instances are created
harry = Grandson() # three instances are created

# here larry can use its and darry's functions and constructors
# harry can use any functions and any constructors of any class

print("darry basketball -->", darry.basketball)

print("-------------------------------------------------")

print("larry dance -->", larry.dance)
print("larry basketball -->", larry.basketball)
lar = larry.isdance()                                                  # if you want to execute any function then first you have to create a variable and print that variable 
print("larry isdance -->", lar)

print("-------------------------------------------------")

print("harry basketball -->", harry.basketball)
print("harry dance -->", harry.dance)
print("harry guitar -->", harry.guitar)
har = harry.isdance()
print("harry isdance -->", har)
harr = harry.isdances()
print("harry isdances -->", harr)

print("-------------------------------------------------")



# electronic device
# pocket gadget
# phone




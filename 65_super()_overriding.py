# Super() and Overriding In Classes


# As you people might have noticed that we came across super and overriding keywords a lot of time in a few of our previous tutorials but did 
# not get into its detailed working. The reason for that was to give you an idea of concepts leading to the use of super() and overriding first. 
# In this tutorial, we are going to discuss it in detail, using the single inheritance as an example.

# Yet being different concepts, they are often used together. The need for superclass arises when overriding is being done at a certain point in our code. 
# Overriding is an essential part of object-oriented programming since it makes the inheritance utilize its full power. Overriding avoids duplication of code, 
# and at the same time, enhances or customizes the part of it. It is a part of the inheritance mechanism. Let us get a description of overriding first so that 
# we can dive into the concept of super() later. 

# How to override class methods in Python?
# Overriding occurs when a derived class or child class has the same method that has already been defined in the base or parent class. 
# When called, the same methods with the same name and number of parameters, the interpreter checks for the method first in a child class and runs it ignoring 
# the method in the parent class because it is already overridden. In the case of instance variables, the case is a little different. When the method is called, 
# the program will look for any instance variable having the same name as the one that is called in the child, then in the parent, and after that, 
# it comes again into child class if not found.

# Where does super() fit in all this?
# When we want to call an already overridden method, then the use of the super function comes in. It is a built-in function, so no requirement of any module import statement.
# What super does is it allows us to use the method of our superclass, which in the case of inheritance is the parent class. Syntax of using super() is given below:

# class Parent_Class(object):
#       def __init__(self):
#             pass

# class Child_Class(Parent_Class):
#      def __init__(self):
#            super().__init__()
# super() returns a temporary object of the superclass that then allows you to call that superclass’s methods. 
# The primary use case of super() is to extend the functionality of the inherited method.

# We have discussed earlier that in the case of method overriding, the previous method could not be called, but super makes an exception, 
# and thus we can partially or completely use the method of the parent class too. We can even use super() to call only a specific variable we used in our overridden method. 
# Calling the superclass-built methods with super() saves us from rewriting those methods in our subclass and allows us to swap out superclasses with minimal code changes.




class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    # Super class matlab parent ya basic class jo hota he use bolte he

    def __init__(self): # yaha pe mene class A ke contructor ko override kr diya he to ab uska koi vajud hi nahi banta...fir bhi me agar class A ke self.special
                        # ko run karna chahata hu to muze ise super banana padega

        # super().__init__() # agar he super yaha likha to b instance Class B ke variables ko print karega

        self.var1 = "I am inside class B's constructor" # Override matlab same variable banana ....child class me
        self.classvar1 = "Instance var in class B"

        super().__init__() # super Class ke constructor ko call kiya
                            # yaha pe mene super bana diye to, agar mene b instance se ya a instance se bhi override hue huye constructor ko call kiya to vo call hoga par
                            # vo sirf override huye class ke constructors ko print karega

        print(super().classvar1) # ye super class matlab parent class ke classvar1 ko print karega
        print("-------------------------------")


a = A() # two instances are created 
b = B() # two instances are created

# Agar super() kiya to override hua hi function ya constructor run hoga Matlab vo child class ko bhul jayega

print(a.var1)
print(a.classvar1)
print(a.special)

print("----------------------------")

print(b.var1) 
print(b.classvar1)
print(b.special) 

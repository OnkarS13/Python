# Polymorphism In Python

# What Is Polymorphism?
# In the basic English language, Polymorphism means to exist in different states. 
# The same object or thing changing its state from one form to another is known as polymorphic. 
# The same function or method, being used differently in different scenarios, can perfectly describe Polymorphism. 
# It occurs mostly with base and derived classes.  

# Understanding Polymorphism in Python:
# The concept of Polymorphism has very strong ties with the method overriding concept that we will learn in the next tutorial, i.e., 
# tutorial#65 of this course, along with the super() function. In Python, it is mostly related to objects or the values of 
# variables that are assigned in different classes. For example, suppose a method in the child class has the same name as 
# the methods in the parent class, and also they take the same number of variables as parameters. In that case, the child class
# will inherit the methods from the parent class and will override the method too. Meaning that the compiler will execute the method in 
# the child because it will be the first place it looks while searching for the method when called. By overriding a method, we can also 
# add some more functionalities in it, so in a way modifying the method in the child class but letting it remain the same in the parent class.

# For example:

# len("Python") # returns 6 as result
# len([1,2,3,4,5,6,7,8,9]) # returns 9 as result

# Python also implements Polymorphism using methods. The len() method returns the length of an object. 
# In this case, the function len() is polymorphic as it is taking a string as input in the first case, 
# which returns the total length/characters of the string, and in the second case, it is taking list as input.

#  Polymorphism is a very important concept. Although being a theoretical concept, it is of great importance as it teaches us to use one entity, 
#  let it be a method or variable, differently at different places. By applying the concept of Polymorphism, we can save our time and make our 
#  code more efficient and compact by using the DRY (Don't Repeat Yourself) concept, which is the basis of Oop.

# We can apply the concept of Polymorphism to the methods, objects, functions, and inheritance. Even though the syntax and rules differ, 
# but the concept remains the same. 

# Polymorphism in '+' operator:-
# Take a look at the below example:

# print(5+6)
# print("5" + "6")

# In the above example, we have used the '+' arithmetic python operator two times in our programs. 
# This is an example of the implementation of Polymorphism in Python. We can use the same + operator to add two integers, 
# concatenate two strings, or extend two lists. The + arithmetic operator acts differently depending on the type of objects it is operating upon.



print(5+6)
print("5" + "6")

# Abstraction
# Encapsulation
# Inheritance
# Polymorphism

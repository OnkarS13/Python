# When working with objects in Python, we have to work with two types of variables, i.e., instance variables and class variables. 
# But what do these types of variables mean, and how do they work? OOP allows the variables to be used at the class level or the instance level. 
# In this tutorial, we will learn about the two different kinds of variables associated with a class and the difference between them. The variables are:

# Instance variable
# Class variable
# Instance variable:
# "Instance variables are the variables for which the value of the variable is different for every instance."

# We can also say that the value is different for every object that we create. 
# Let us dive into some in-depth explanations. When we create a class, we define a few variables along with it. For example, we have created a class of Students, 
# and we have defined a variable age. All the students cannot have the same age in a class, so we have assigned the variable an average age of 16. 
# Now, whenever we use an object to print the value of age, it will show 16. We can change the value of age, but it will create a new instance variable for 
# the specific object that we are updating it for, hence defining the value to it.

# The code for changing age for a particular object will be something like this:

# Std1.age = 18

# Class variable:
# "Class attributes are owned by the class directly, which means that they are not tied to any object or instance."

#  Same as in the above example, if we want to change the age for every instance from 16 to 17, 
#  then we can do it by using the class variable, which in this case is Student. 

# "It is worth noting that updating the value of the class variable will not change it for the instance variables of the objects, such as in the case above."

# The code for changing age using a class variable will be something like this:

# Students.age = 18


# The following are the notable differences between Class (static) and instance variables.
# Following are the differences between Class and instance variables.


# Instance variables                                                      Class variables

# When an object is created with the use of the new keyword,           When the program starts, static variables are created and destroyed when the program stops.
# instance variables are created. 
# They are destroyed when the object is destroyed.

# Instance variables can be accessed by calling the variable          Static variables can be accessed by calling using a class
# name inside the class. ObjectReference.VariableName.                name. ClassName.VariableName.

# Every instance of the class has its own copy of that variable.      There is only one copy of that variable that is shared with all instances of the class. If changes are made to that variable, all other instances will be affected.
# Changes made to the variable don't affect the 
# other instances of that class.


# The __dict__ attribute
# Every object in Python has an attribute that is denoted by __dict__. It maps the attribute name to its value. 
# This dictionary stores all the attributes defined for the object itself. Following is the syntax of using __dict__:

# object.__dict__

# A quick review:
# Instance variables are created only for a specific object. 
# The object can change, create, or update only its instance variables. While in the case of class variables, 
# the variables and values we create or define are set as default for all the objects. The objects cannot change the class value or 
# variable by updating it using object_name.variableName.However, it can change the values of their particular instance variables. 
# Making use of class and instance variables can ensure that our code adheres to the DRY (don't repeat yourself) principle to reduce repetition within code.

class Employee: # Employye named class is created 
    no_of_leaves = 8    #this is called class variable
                        # here a global variable is created and it is like property of Employee class ....It is applicable for whole class
    pass # It is almost compulsory to write

harry = Employee() # here two objects or instances are created of class Employee
rohan = Employee() # here two objects or instances are created of class Employee

harry.name = "Harry" # here instance varibles are created 
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(Employee.no_of_leaves) # it will print =  8

print(Employee.__dict__) # Here in employee both the harry and rohan are objects of class employee  So it will print them in form of dictionary

Employee.no_of_leaves = 9 # value is updated for global case

print(Employee.__dict__) # it will print updated values

print(Employee.no_of_leaves) # here it will print updated value of no_of_leaves

harry.no_of_leaves = 10 # here I updated the respective objects no_of_leaves value ....it will affect the global value of class Employee
rohan.no_of_leaves = 15 # here I updated the respective objects no_of_leaves value ....it will affect the global value of class Employee 

print("These are the updated values of respective object - harry", harry.no_of_leaves)
print("These are the updated values of respective object - rohan", rohan.no_of_leaves)
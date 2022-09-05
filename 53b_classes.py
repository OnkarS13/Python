# Defining a Class in Python:
# As in function, definitions begin with the keyword def, class begins with a class keyword.

# class MyClass:
#     '''This is a docstring.'''
#     pass
# A class is a blueprint from which objects are created. Creating a new class creates a new type of object, which allows the new instances of that type to be made. Each class instance has attributes attached so that it can maintain its state. Class instances can also have methods that are defined by their class for modifying their state. 

# Let us understand the concept of class through an example. Suppose we have to create a program that requires the data of all the individuals in a school. We will create three different classes, one for students, one for teaching staff, and one for accounting officers and others. The separation of the class is based on attributes because a teacher’s attributes are different from students’, and both have different attributes from the members of account officers. Although many attributes are the same, such as name, age, address, etc. but the teacher also has an attribute salary that the student does not or an attribute, number of classes that the accounts officers do not possess. So, now we have an understanding of how and on what basis we form different classes.  

# Classes are not like functions, so we do not have to use the keyword def to create a class; instead, we use the keyword Class along with the name of the class. Also, we do not call a class as a whole; instead, we use an object to access its different attributes. We can assign new values and can also overwrite the previous values with the help of an object. In short, an object gives us permission to access the whole class. We can access variables in a class, like:

# Object_name.variable_name = “abc”
# Here we are setting a variable equal to abc. By doing this, its previous value will be overwritten.


# Creating Object:
# Creating an object of a class is rather easy and simple. Suppose we have a class named Student. We can create an object of it by these certain lines of code:

# Stu1 = Student()
# Stu2 = Student()
# Here we have created two objects of class Student. We can access every item in the Student class using these objects. There is no restriction on the number of objects a class may have, and also, there is no limit to the number of classes a program may have.

# An object consists of :
#  The State, which is represented by attributes of an object which reflect the properties of an object.
#  Methods of an object represent the object’s behavior and the response of an object with other objects.
#  Identity, which gives a unique name to an object so that one object can interact with other objects.
# Code file as described in the video:



class Student: #Here class is created Student 
    pass # This pass means that it is like void

harry = Student() # harry named object is created
larry = Student() # larry named object is created

harry.name = "Harry" 
harry.std = 12
harry.section = 1

larry.std = 9
larry.subjects = ["hindi", "physics"]

print(harry.section, larry.subjects) # here with the help of objects items are invoked 



  

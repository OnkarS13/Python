# We have been dealing with static methods until now. In Object-Oriented programming, there is a concept of a class method, 
# which we will see today in this lecture. They are very different from static methods as they are limited in their functionality to the built-in class. 
# They can be called by using the class name and also can be accessed by using the object.

# As we have observed in the previous tutorials, we cannot change the value of a variable defined in the class from outside using an object. 
# Instead, if we try that, a new instance variable will be created for the class having the value we assigned. But no change will occur in the 
# original value of the variable.

# We saw the use of the self keyword in the previous tutorial. In this tutorial, we are going to know the working of a new keyword, 
# i.e., cls. Class methods take cls parameter that points to the class and not the object instance when the method is called.

# Syntax:



# class myClass:
#     @classmethod
#     def myfunc (cls, arg1, arg2, ...):
#                           ....


# myfunc defines the function that needs to be converted into a class method

# returns: @classmethod returns a class method for function.

# Because the class method only has access to the cls argument, it cannot modify the object instance state. 
# However, class methods can still modify the class state that applies to all instances of the class. 
# So a class method automatically recognizes a class, so the only parameter that remains to be passed is the function that needs conversion.

# @classmethod Decorator:
#  We have covered decorators in detail in Tutorial 
 #51, so here we are just doing to define the functionality of decorators instead of its working. 
 # A @classmethod Decorator is a built-in function in Python. It can be applied to any method of the class.
 #  We can change the value of variables using this method too.

# A quick overview:
# The Python class method is a way to define a function for the Python class. 
# It receives the class as an implicit first argument. Using @classmethod decorator, creating as many constructors for a class that 
# behaves like a factory constructor is possible. Hopefully, now you can apply this concept to your projects and use it to improve your code's 
# organization and quality.



class Employee:
    no_of_leaves = 8

    

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod # with the help of this classmethod if we want to change any class instance with the help of instance...it is possible
                    # if we change no_of_leaves with the help of  rohan or harry ...it will be changed for every instance and class too

    def change_leaves(cls, new_leaves):     # To is function me cls me harry ka class chala jayega aur new_leaves me 36  chala jayega...matlab value update ho jayega 
                                            # This function is made for changing the value of no_of_leaves
        cls.no_of_leaves = new_leaves       # It is like rohan.no_of_leaves ho jayega....

harry = Employee() # here two instances are created 
rohan = Employee() # here two instances are created 

rohan.change_leaves(36) # agar rohan ke nam se bhi value update kiya to to pure class ke liye update ho jayega....
                        # yahi classmethod ka kam he
print(harry.no_of_leaves)



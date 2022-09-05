# In this tutorial, we will learn how we can convert a class method into an alternating constructor. 
# This tutorial is not about "what," as we have seen in previous tutorials, where we learn about new concepts or functionality. 
# But this one is about" how." We will focus more on implementation as we are already familiar with all the concepts we are going to use. 
# In this tutorial, we are going to learn some new skills or techniques other than a new concept.


# We learned about constructor and its functionality in tutorial #55, 
# where we had to set all the values as parameters to a constructor. Now we will learn how to use a method as a constructor. 
# It has its own advantages. By using a method as a constructor, we would be able to pass the values to it using a string.

# Note that we are talking about a class method, not a static method.

# The parameters that we have to pass to our constructor would be the class i.e., cls and the string containing the parameters. 
# Moving on towards the working, we have to use a function "split()," that will divide the string into parts. 
# And the parts as results will be stored in a list. We can now pass the parameters to the constructor using the index numbers of the 
# list or by the concept of *args (discussed in tutorial#43 ).



# split():
# Let us have a brief overview of the split() function. What split() does is, it takes a separator as a parameter. 
# If we do not provide any, then the default separator is any whitespace it encounters. 
# Else we can provide any separator to it such as full stop, hash, dash, colon, etc. 
# After separating the string into parts, the split() function stores it into a list in a sequence. For example:

text = "Python tutorial for absolute beginners."
t = text.split()
print(t)

# Here, we are not providing it any separator as a parameter, so it will automatically divide, 
# taking whitespace as a separator. 

# The output will be a list, such as:

# ['Python', 'tutorial', 'for', 'absolute', 'beginners.']

print("-----------------------------------------------------------------------------------")

# Example of Class methods - alternative constructor:

class Date:
    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    @classmethod
    def from_d(cls, string):
        return cls(*string.split("-")) # here args and kwargs are used So with the help of from_d function and split function dates are separated 

today = Date.from_d("2002-01-08")

print("Year is", today.year)
print("Month is", today.month)
print("Day is", today.day)

print("-----------------------------------------------------------------------------------")



class Employee:
    no_of_leaves = 10

    def __init__(self, aname, asalary, arole): # Constructor is created
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        params = string.split("-")
        print(params) # it will print in form of list
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-")) # it will work the same


harry = Employee("Harry !", 1000000, "Instructor")
rohan = Employee("Rohan !", 1500000, "Student")

karan = Employee.from_dash("Karan !-45478 - Teacher")

print("Name is ", harry.name, "Salary is ", harry.salary, "Role is ", harry.role)
print("Name is ", rohan.name, "Salary is ", rohan.salary, "Role is ", rohan.role)
print("Name is ", karan.name, "Salary is ", karan.salary, "Role is ", karan.role)
    

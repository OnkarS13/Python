# We are going to name our file argskw here.  

# We have worked with functions lately and also have made our own functions. 
# We have seen that a function can only pass a certain number of arguments. 
# The number of arguments has to be decided while defining the function, and it can not be changed while calling it. 
# In simple terms, the number of arguments passed should be the same as the ones that are defined. 
# If we dislike this restriction and do not want ourselves to be bound by certain limits, then we are lucky to have *args and **kwargs with us.

# Before discussing *args and **kwargs, we should have a basic knowledge about types of arguments. 
# In Python programming, there are two types of arguments that can be passed in a function.

# positional arguments
# keyword arguments
# Positional arguments are the one in which an order has to be followed while passing arguments. 
# We have been dealing with them until now.

# We know how normal functions work with positional arguments, so now we will directly start exploring keyword arguments. 
# But to understand them, we have to know about asterisk or more commonly known in Perl 6 and ruby as a splat operator.

#  Asterisk is used in python as a mathematical symbol for multiplication, but in case of arguments, it refers to unpacking. 
#  The unpacking could be for a list, tuple, or a dictionary. We will discover more about it by defining *args and **kwargs.

# *args:
# args is a short form used for arguments. It is used to unpack an argument. In the case of *args, the argument could be a list or tuple. 
# Suppose that we have to enter the name of students who attended a particular lecture. 
# Each day the number of students is different, so positional arguments would not be helpful because we can not leave an argument empty in that case. 
# So the best way to deal with such programs is to define the function using the class name as formal positional argument and student names with 
# parameter *args. In this way, we can pass student's names using a tuple.

# Note that the name args does not make any difference, we can use any other name, such as *myargs. 
# The only thing that makes a difference is the Asterisk(*).

# **kwargs:
# The full form of **kwargs is keyword arguments. It passes the data to the argument in the form of a dictionary. 
# Let's take the same example we used in the case of *args. The only difference now is that the student's registration, along with the student's name, 
# has to be entered. So what **kwargs does is, it sends argument in the form of key and value pair. So the student's name and their registration both 
# can be sent as a parameter using a single ** kwargs statement.

# Same as we discussed for args*, the name kwargs does not matter. We can write any other name in its place, such as **attendance. 
# The only mandatory thing is the double asterisks we placed before the name.   

# One of the instances where there will be a need for these keyword arguments will be when we are modifying our code, 
# and we have to make a change in the number of parameters or a specific function.




# here function_name named function is created and it has parameters
def function_name(a, b, c, d, e):
    print(a, b, c, d, e)


# function invoked and passed tha values
function_name("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

print("--------------------------------------------------------------------")


def funargs(norm, *argsOnkar, **kwargsOmii):
    # here name of arguments matter nahi karte just, * hoga to args and ** hoga to kwargs hoga...thats it
    # here normal and *argsOnkar named three arguments are created and **kwargs is also created (argument)
    # hame hamesha normal arguments first rakhane he aur *args bad me
    print(norm)
    print(type(argsOnkar))  # here it means name is not important

    # print(args[0]) # it will print 0 th index of that har list

    for item in argsOnkar:  # here it means name is not important
        print(item)

    print("-----------------------------------------------------------------")

    for key, value in kwargsOmii.items():  # you must have to write .items() when you want to print multiple elements and keys
        print(key, value)
        print("Another method for writing this by using f string ")
        print(f"{key} is a {value}\n")


# here list is cretaed and by doing *args i can add infinite no of elements in list har
har = ["Harry", "Rohan", "Skillf", "Hammad", "Shivam", "I am programmer"]
# harr = ("Harry", "Rohan", "Skillf", "Hammad", "Shivam") # here tuple is cretaed   Both will work same

normal = 34  # here I assigned 34 to normal and it got passed to that functions argument

kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor", "The Programmer": "Coordinator",
      "Shivam": "Cook", "Onkar": "Professor"}  # here dictionary is created

# funargs function is invoked and har list is passed to it also kw dictionary is passed to **kwargs function
funargs(normal, *har, **kw)
# funargs(*harr) # funargs function is invoked and har list is passed to it

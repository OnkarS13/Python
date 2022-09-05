# Functions And Docstrings
#  “Functions in Python can be defined as lines of codes that are built to create a specific task and 
#  can be used again and again in a program when called.”

# There are two types of functions in the Python language:
# Built-in functions
# User-defined functions

# We have used a lot of built-in functions in our code till now, these functions include print(), or sum(), etc. 
# So, we have a good idea about how to call a function. Built-in functions are already present in our python program, 
# and we just have to call them whenever we need them to execute. Being familiar with built-in functions we will 
# now look into User-defined function mostly in this tutorial.

# We must know how to define a function in Python. In order to create one ourselves, 
# we have to use the def keyword in order to define a function accompanied by the function's name with a pair of parentheses. 
# The function of parenthesis is to send arguments or parameters to a function. 
# n simple words, parameters can be defined as values that are sent in the parenthesis. 
# For example, if a function is used to add two numbers then both the numbers will be passed as parameters in the parenthesis. 
# After parenthesis, a colon is used to get in the body of the function. Some functions may return a value to the caller, 
# so in order to get the value, a return statement is put at the end of the body of the function that gives the value that has been calculated by the function.

# Calling a function is very simple, we just have to write the name of the function along with the closing parenthesis. 
# If the function requires some arguments then we write those in the parenthesis, but if it does not return anything, then we leave them empty.

# We have discussed a lot about what functions are and how to use them, now let us move to the advantages of using a function:

# If we are working on a big project then we will prefer to make as many functions as possible, so every other member of our team could use that.
# By using functions, we can avoid the repetition of code to an extent. As we have discussed in the previous tutorial i.e. Tutorial #22, more lines of code mean less efficiency. Also repeating the same code at different places will just make the code more crowded than required.
# The reusability of code is ensured by using functions. We can even use a function inside another function or in any part of our code.
# By making a function of code that we are going to use again and again, we can save a lot of time.

# Docstrings
# Docstring is a short form of documentation string. Its purpose is to give the programmer a brief knowledge about the functionality of the function. 
# It must be the first string in a function, and it is also an optional string but always good to have it while working on programs having multiple functions. 
# The syntax for writing a docstring is very simple as it is just a string written in between three double quotes placed three times (""" """) on either side of the string. 
# But it has to be the first line of code in the function’s body. To call a docstring we write the name of the function followed by ._doc_.








a = 4
b = 10
e = sum((a, b)) # built in function # this method also can be used, by using variables
c = sum((4, 10))
print(c)
print(e)

def name(): # here def is like void in cpp, int, or somthing else
    print("Hello you are in function") # everything that you entered, using tab button will be in that function

print(name()) # dont forget to write (), after function name 
name() # By writing only name of function, means that you are calling whole function, and calling print function


# Here function is creatednmaed function1 and it has two parameters. and in this function its working is to add two numbers 
def function1(a, b):
    print("You are in function 1\n", a + b)
function1(5, 10) # here I am calling the function1 and assigning value to it at same  time

def function2(c, d):
    # Here it is called docstring
    #  and we can also print doc string
    """This is a function which will calculate average of two numbers
    this function doesnt work for three numbers"""

    average = (c + d)/2
    # print(average)
    return average
    

#now i am providing values to function2
# function2(12, 45)   # here I am calling the function2 and assigning value to it at same time
# so in short when ever you want to print the value by variable then you have to return that functions working

#if i want to print their value by variable, then
v = function2(12, 45)
print(v)  # it will print none...So, in function2, we have to return the that average, then it will be printed

print(function2.__doc__)  # This will print that doc String which is in """    """
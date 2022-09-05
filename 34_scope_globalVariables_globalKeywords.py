# Scope, Global Variables and Global Keyword
# What is Scope in Python?
# Scope refers to the coding area where a particular Python variable is accessible. 
# Hence one cannot access any particular variable from anywhere from the code. 
# We have studied about variables in previous lectures. Recall that a variable is a label for a location in memory. It holds a value. 
# Not all variables are accessible, and not all variables exist for the same amount of time.

# Where the variables defined determines that is it accessible or not, and how long it will exist.

# Local vs. Global Variables
# Local Variable:-
# A variable that is declared inside a function or loop is called a local variable. In the case of functions, when we define a variable within a function, 
# its scope lies within the function only. It is accessible from the point where it is defined until the end of the function. 
# It will exist for as long as the function is executing. Local variables cannot be accessed outside the function. The parameter names in the function, 
# they behave like a local variable.

# For Example,
# def sum():

#       a=10 #local variable cannot be accessed outside the function
#       b=20
#       sum=a+b
#       print( sum)

# print(a) #this gives an error
# When you try to access variable “a” outside the function, it will give an error. 
# It is accessible within the function only.

# Global Variable:-
# On the other hand, a global variable is easier to understand; it is not declared inside the function and can be accessed anywhere within a program. 
# It can also be defined as a variable defined in the main body of the program. Any function or loop can access it. Its scope is anywhere within the program.

# For Example,
# a=1  #global variable

# def print_Number():

#             a=a+1;
#             print(a)

#  print_number()
# This is because we can only access the global variable, but we cannot modify it from inside of the function.

# What if we want to modify the global variable inside the function?
# For this purpose, we use the global keyword. In Python, the global keyword allows us to modify the global variable. 
# It is used to create a global variable and make changes to the variable in a local scope.

# Rules of global keyword:
# If we assigned a value to a variable within the function body, it would be local unless explicitly declared as global.
# Those variables that are referenced only inside a function are implicitly global.
# There is no need to use the global keyword outside a function.
# What if we have a nested function. How does the scope change?
# When we define a function inside another function, it becomes a nested function. We already know how to access a global variable from a 
# function by using a global keyword. When we declare a local variable in a function, its scope is usually restricted to that function alone. 
# This is because each function and subfunction stores its variables in its separate workspace.

# A nested function also has its own workspace. But it can be accessed to the workspaces of all functions in which it is nested.
# A variable whose value is assigned by the primary function can be read or overwritten by a function nested at any level within the primary.

















l = 10 #global
b = 15 #global
def function1(n):
    global b
    l = 5 # local variables
    m = 8

    #we can update local vairables value in that function
    # we cant update or change the value of global variable
    # l =  l  + 45  # this is for global case not for local 

    #If I want to change the value of global then I have to get accessed of it
    print(b, "This is before updating")
    b = b + 15
    print(b, "This value is updated of b")
    

    print(n, "This is written")
    print(l, m) # this will print (5, 8),  becoz this print is in function1 and it will print its local variables

function1("Onkar ") # here i called the function and passed something to argument n
print(l) # here print(l) will print 10,  becoz it is global 
print(b)





print("-------------------------------")

x = 100 #global variable

def harry(): # harry named default function is created
    x = 20 # local vatiable
    print(x, "harry")
harry() # here I called the harry function
    
def rohan():
    global x # here i called the global variable x and accessed its value
    print("before calling rohan()", x)
    x = 88 # here i updated the value of global varible 

rohan()
print("after calling rohan()", x)

harry()
print(x, "Harry updated value of x") #

print("-------------------------------")


# this is example of nested function


# p = 70
def harry():
    p = 20
    def rohan():
        global p    # this will not update valur of x becuase when ever you try to access global, it directly go outside of all function 
                    # and try to find global variable, here harry() x = 20 is local proprty of harry, so it cant change its value
                    # if any global function is present outside the function, then it will not update its value  and if any global variable id present outside the function
                    # it will update that specific value
        p = 88
    print("before calling rohan()", p)
    rohan()
    print("after calling rohan()", p) # this global p will not affect harry or rohan.

harry() # but here outside the function rohan and harry, it created a global function p itself and made changes 
print(p)


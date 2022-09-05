# Using Python External & Built In Modules
# In Python, a module can be defined as a file containing a runnable python code. The extension used by modules in Python is .py. 
# Hence any simple file containing Python code can be considered as a module if its extension is .py. The file and module names are the same; 
# hence we can call a module only by name without using the extension. Along with this, a module can define functions, classes, and variables.

# There are two types of modules.

# Built-in
# External
# Built-in Modules:
# Built-in modules are already installed in Python by default. We can import a module in Python by using the import statement along with the specific 
# module name. We can also access the built-in module files and can read the Python code present in them. Newly integrated modules are added in 
# Python with each update. 

# Some important modules names are as follows



# Modules Names           Purpose
# calendar                used in case we are working with calendars
# random                  used for generating random numbers within certain defined limits
# enum                    used while working with enumeration class
# html                    for handling and manipulating code in HTML
# math                    for working with math functions such as sin, cos, etc.
# runpy                   runpy is an important module as it locates and runs python modules without importing them first


# External modules:
# External modules have to be downloaded externally; they are not already present like the built-in ones. 
# Installing them is a rather easy task and can be done by using the command “pip install module_name” in the compiler terminal. Being familiar with all 
# the modules seems like a long shot for even the best of programmers because there are so many modules available out there. 
# So, we can search and find modules according to our needs and use them as there is no need to remember all of them when we can simply look for them on 
# the internet when the need occurs.

# Being programmers, module makes our life a lot easy. Unlike programming languages in the past, 
# also known as low-level programming languages, Python provides us with a lot of modules that make our coding much easy because we do not
# have to write all the code ourselves. We can directly access a module for a specific task. For example, to generate a random number within two numbers, 
# known as its limit, we do not have to write a function ourselves with loops and a large number of lines of codes. Instead, we can directly import a module, 
# and this makes our work simple.

# We should not concern ourselves with the code written inside the module; instead, we can search the internet for the functions and properties. 
# If we are not satisfied with the available module's work or could not find a module that could help us in the required manner, 
# we can create our own module by making a file with .py extension. The module file will be like any other file you see in Python, 
# the difference will just arise in the extension.  





import random
random_number = random.randint(0, 10) # it will print random number from 0 to 10
print(random_number)

random3 = random.random() # it will print random number from 0 to 1
random1 = random.random() * 100 # it will print random number from 0 to 100
print(random3)
print(random1)

lst = ["Star Plus", "DD1", "Aaj Tak", "CodeWithHarry"] # it will choose any random word from that list lst
cho = random.choice(lst) # that random choice will be assigned to cho 
print(cho)
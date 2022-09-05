# Operators In Python

# Today's tutorial is more about theoretical learning than coding because we must have basic 
# knowledge about what we are actually implementing in our code because if our basis is strong 
# then only we can make an efficient program of a larger scale.

# “Operators in Python can be defined as symbols that assist us to perform certain operations. 
# The operations can be between variable and variable, variable and value, value and value”

# Operators that Python Language supports are:

# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity Operators
# Membership Operators
# Bitwise Operators


# We must remember most of them from our basic mathematics that we studied in school. 
# May be except the last one, that might be new for some of us. 
# To understand bitwise fully, we must have the basic knowledge of the conversion of decimal into binary. 
# For example, the binary for the first five number is:

# 0001
# 0010
# 0011
# 0100
# 0101


# And so on.

# Now I will give you a theoretical understanding of each of these operators. 
# There is no theory related difference in them and the one we studied during school time.
# The only difference you will see will be in the syntax i.e. how to write them for perfect execution.

# Arithmetic Operators:
# Basic mathematical operations such as addition, multiplication, subtraction, division, etc. 
# are performed with the help of arithmetic Operations. 
# It contains nearly all operations that we can perform with the help of a calculator. 
# Symbols for such operators include *, /, %, -, //, etc.    

# Assignment Operators:
# The assignment operator is used to assign values to a variable. 
# In some cases, we have to assign a variable’s value to another variable, in such cases the value of the right operand is assigned to the left operand. 
# One of the basic signs from which we can recognize an assignment operator is that it must have an equal-to(=) sign. 
# Some commonly used assignment operators include +=, -=, /=, etc.

# Comparison Operators:
# They are also known as relational operators. They compare the values on either side of the operator and decide the relation among them. 
# Commonly used comparison operators include ==, >, < , >=,etc.

# Logical Operators:
# Logical operators perform logical AND, OR and NOT, operations. 
# They are usually used in conditional statements to join multiple conditions. 
# AND, OR and NOT keywords are used to perform logical operations.

# Identity Operations:
# Identity operator checks if two operands share the same identity or not, which means that they share 
# the same location in memory or different. “is” and “is not” are the keywords used for identity operands.

# Membership Operands:
#  Membership operand checks if the value or variable is a part of a sequence or not. 
#  The sequence could be string, list, tuple, etc. “in” and “not in” are keywords used for membership operands.

# Bitwise Operand:
# Bitwise operands are used to perform bit by bit operation on binary numbers. 
# First, we have to change the format of the number from decimal to binary and then compare them using AND, OR, XOR, NOT, etc.



# Arithmetic Operators
print("5 + 6 is ", 5+6)
print("5 - 6 is ", 5-6)
print("5 * 6 is ", 5*6)
print("5 / 6 is ", 5/6)
print("5 ** 3 is ", 5**3)
print("5 % 5 is ", 5%5)
print("15 // 6 is ", 15//6)

# Assignment Operators
print("Assignment Operators")
x = 5
print(x)
x %=7 
x -=7 
x +=7 
x *=7 
# x = x%7
print(x)

# Comparison Operators
i = 5
print(i == 8)
print(i != 8)

# Logical Operators
a = True
b = False
print( a and b)
print( a or b)
print( a is b)
print( a is not b)

# Identity Operators
# print(5 is not 5)

# Membership Operators
list = [3, 3,2, 2,39, 33, 35,32]
# print(324 not in list)

# Bitwise Operators
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

print(0 & 2)
print(0 | 3)


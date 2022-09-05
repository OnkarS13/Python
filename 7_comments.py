# Comments, Escape Sequences & Print Statement

# Comments are used to write something which the programmer does not want to execute. Comments can be written to mark the author's name, date when the program is written, adding notes for your future self, etc.

# 1. Comments are used to make the code more understandable for the programmer.
# 2. The Interpreter does not execute comments.

# There are two types of comments in Python Language -:

# Single Line Comment
# Multi-Line Comment
# Single Line Comment: Single Line comments are the comments which are written in a single line, i.e., they occupy the space of a single line.

# 1. We use # (hash/pound to write single-line comments).
# 2. E.g., the below program depicts the usage of comments.

# Multi-Line Comment: 

# Multi-Line comments are the comments which are created by using multiple lines,
#  i.e., they occupy more than one line in a program.

# We use ' ' '….. Comment ….' ' ' for writing multi-line comments in Python (Use lines enclosed with three quotes for 
# writing multi-line comments). An example of a multi-line comment is shown below:

import os
#This is a comment
print("Main code started")

#Now I will write my code here:
print(os.listdir())  # this will give list of folders or files present in python folder (specific file), this is default sysntax


# this is multi line comment
 
"""This is a comment
Author: Harry
Date: 27 November 2020
Multi-line comment ends here
"""
print("Main code started")

#Now I will write my code here:
print(os.listdir())


# Python Print() Statement:

# print() is a function in Python that allows us to display whatever is written inside it. 
# In case an operation is supplied to print, the value of the expression after the evaluation is
#  printed in the terminal. For example,


# print statement for printing strings
print("Harry is a programmer", end =" **") # this end= "**" will be added at last of the line
print( )
# Print statement with a literal
print(1+87)

#This will print "Harry is a programmer**88" on the screen 

""" Escape Sequences :
1. An Escape Sequence character in Python is a sequence of characters that represents a single character.
2. It doesn't represent itself when used inside string literal or character.
3. It is composed of two or more characters starting with backslash \ but acts as a single character. Example \n depicts a new line character.
"""
"""

\n 	Inserts a new line in the text at the point
\\	Inserts a backslash character in the text at the point
\"	Inserts a double quote character in the text at that point

\'	Inserts a single quote character in the text at that point
\t	Inserts a tab in the text at that point

\f	Inserts a form feed ln the text at that point
\r	Inserts a carriage return in the text at that point

\b	Inserts a backspace in the text at that point

"""


#Please dont remove this line
"""
This is a
Multiline Comment
"""
"""
This is a comment
"""
# print("Subscribe CodeWithHarry now","Bhai video bhi like kar dena")
# print("next line")
# print("C:\'narry")
print("Harry is \n good boy \t1") #comment after statement       # here /t will add new tab where it is written


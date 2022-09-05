# Short Hand If Else Notation In Python

# Before going through the if-else short-hand statement, we must be familiar with the basic definition, 
# so that we can know what the short-hand statement actually is. 
# In basic English, shorthand can be said as “a basic way of writing using abbreviations or symbols”. 
# For example, we do not use the full name, Kentucky Fried Chicken, instead we use its abbreviation that is KFC. 
# Writing in such a compact manner is known as shorthand. 
# Now let us move towards the definition of shorthand with respect to the Python language.

# “An executable statement, written in so compact manner that it comprises of only a single line of code is known as shorthand statement.”

# Python supports many sorts of shorthand statements and with the help of these statements, 
# we can write our code in a more compact sort or form using less space. 
# We learned the original form of “if and else” statement in tutorial 13 of our playlist, we can also write it in a shorthand form of code.

# Now let us come to the question that why we should use shorthand if-else statement instead of the original one. 
# First of all, you have to do less typing while using the shorthand form. 
# If you are making a project that requires thousands of lines of code then, it is very hectic if you are writing something 
# in four or five lines that could easily be written in a single line. 
# This advantage would not be too convincing for a lot of viewers now and they would not like to adopt the shorthand method 
# instead of the one they are using currently. 
# In this case, this tutorial is still very important for them because if you are a coder then reading other people’s code is a must. 
# Even though you are clearing your concepts by going through some code on Stack Overflow or making a group project with other programmers, 
# you will surely encounter shorthand code at any time, so it is best to have a piece of prior knowledge about it.

#  The second advantage of using the shorthand way of programming is that the compiler handles it in an efficient way. 
#  It does not matter for the short program even though if they are a couple of thousand lines long but when working on a huge project, 
#  like Amazon (12 Million lines of code) or Facebook (62 Million lines of code) or Google (2 Billion lines of code), 
#  then it is very important to save as many lines of code as we can by writing it in a compact form.

# There is also a disadvantage of using shorthand, that it is not easily readable. 
# When we are working on a group project, we always try to choose the approach that is the easiest to understand, 
# and writing a compact code always bring difficulties when we share our code with someone. 
# Even though whichever approach we follow, we should always have knowledge about all possible approaches, because everyone is not 
# using the same approach.








# New Syntax
# If-expression if(Condition) else else-expression

#Old Syntax
# if condition:
#        if-expression
# else:
#    else-expression


# c = int(input("Enter c \n")) # this is also a syntax of getting info from user

a = int(input("enter a\n"))
b = int(input("enter b\n"))

# if a>b: print("A B se bada hai bhai")
print("B A se bada hai bhai") if  b > a else print("A B se bada he")
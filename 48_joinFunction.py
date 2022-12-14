# We are all familiar with the word join and it's meaning i.e., to combine. Join has nearly the same meaning in Python, 
# as it is used to join the elements of a list, tuple, set, etc. In this article, we will learn about the join() method and how to use it. 
# In Python, join() is a function that is used with iterables like list, dictionaries, and string.
# Examples are also mentioned below so you may learn how to use join() function. If you do not know what iterables are, 
# then check our tutorials on Python Lists And List Functions, Dictionary & It's Functions and String Slicing And Other Functions to 
# get the basic idea about iterables.

# What is the join method in Python?
# "Join is a function in Python, that returns a string by joining the elements of an iterable, using a string or character of our choice."

# In the case of join function, the iterable can be a list, dictionary, set, tuple, or even a string itself. 
# The string that separates the iterations could be anything. It could just be a comma or a full-length string. 
# We can even use a blank space or newline character (/n ) instead of a string.

# The syntax of the join() method is:
# string.join(iterable)
# the string is the name of string in which joined elements of iterable will be stored.

# Note: If the iterable contains any non-string values, join() will raise a TypeError exception.

# The implementation over the list iterable example is explained below. Here we join the elements of a list using a delimiter. 
# A delimiter can be any character or nothing.

# For Example:

#join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))
# Output:
# 1, 2, 3, 4

# With the join function, we can join two strings together, changing it into a larger string. 
# Along with the iterable, we also have to use a string between each iterable and a string on its own is also iterable; thus, 
# two strings can also be joined by using the join function.
# It's is a lot easier and more compact than using a loop.
# We use a variable for iteration along with a string or fstring to print all the elements onto the screen.

# How will the join function work in case of a "dictionary"? Are there any limitations to join() function?
# The join function has certain limitations. 
# We must have a question in our mind that how join function will work in case of a "dictionary" where there are values along with the keys. 
# In the case of the dictionary, the join function will only return the key part, separated by the string in between, leaving the value side behind.

# For Example:
myDictionary = {"name": "Jack", "country": "America"}
separator = "_separator_"
print(separator.join(myDictionary))

# Output:
# name_separator_country

# As we are on the subject, let us discuss another limitation associated with the join method. 
# In situations where the iterable consists of a multi-data type, such as a list or tuple consisting of all integer variables and one single, 
# double variable, the join function will not work. 
# Instead, it will display an error. 
# For join to function properly, all the variables should have the same sort of data type, either it is an integer, string, or any other.

# For Example:
inputlist = {"Test1":13,"Test2":24,"Test3":100,"Test":4}
sep = '_'
out = sep.join(inputlist)
print(out)
# Output:
# Traceback (most recent call last): File "./prog.py", line 3, in TypeError: sequence item 1: expected str instance, int fou







lis = ["john", "cena", "Randy", "orton", "Sheamus", "Khali", "Jindar mahal"]

for item in lis:
    print(item, "and", end = " ")

#for joining the statements use join function
a = ", ".join(lis) # it joins every element in that function with user's desired string or anything like , 
print(a, "Other wwe superstars")

print("Other wee superstars")
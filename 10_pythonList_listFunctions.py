# Python Lists And List Functions

# Python lists are containers used to store a list of values of any data type.
# In simple words, we can say that a list is a collection of elements from any
# data type. E.g.
list1 = ['harry', 'ram', 'Aakash', 'shyam', 5, 4.85]

# The above list contains strings, an integer, and even an element of type float.
# A list can contain any kind of data, i.e., it’s not mandatory to form a list of only one data type.
# The list can contain any kind of data in it.

# Do you remember we saw indexing in strings? List elements can also be accessed by using Indices,
# i.e., the first element of the list has 0 index and the second element has one as its index, and so on.

# Note: If you put an index that isn’t in the list, you will get an error.
# i.e., if a list named list1 contains four elements, list1[4] will throw an error because the list index starts
# from 0 and goes up to (index-1) or 3.
# Have a look at the examples below:\

# Lists in Python

[]                                             # list with no member, empty list
[1, 2, 3]                                    # list of integers
# list of numbers (integers and floating point)
[1, 2.5, 3.7, 9]
['a', 'b', 'c']                               # list of characters
['a', 1, 'b', 3.5, 'zero']                # list of mixed value types
['One', 'Two', 'Three']               # list of strings


# *******************************List Methods :*******************************

# Here is the list of list methods in Python.
# These methods can be used in any python list to produce the desired output.

# List Methods :
l1 = [1, 8, 4, 3, 15, 20, 25, 89, 65]  # l1 is a list
print(l1)

l1.sort()
print(l1)  # l1 after sorting
l1.reverse()
print(l1)  # l1 after reversing all elements

print("----------------------------------------------------------------------------------------")

# ************************************List Slicing :************************************

# List slices, like string slices, return a part of a list extracted out of it. Let me explain; you can use indices to get elements and create list slices as per the following format :

# seq = list1[start_index:stop_index]
# Just like we saw in strings, slicing will go from a start index to stop_index-1. The seq list, a slice of list1, contains elements from the specified start_index to specified (stop_index – 1).


# ***********************************List Methods:***********************************

# There are a lot of list methods that make our life easy while using lists in python.
# Let's have a look at a few of them below:
# List Methods :-

list2 = [1, 2, 3, 6, 8, 5, 4]  # list1 is a list

list2.append(7)    # This will add 7 in the last of list
print(list2)
list2.insert(3, 8)    # This will add 8 at 3 index in list
print(list2)
list2.remove(1)  # This will remove 1 from the list
print(list2)
list2.pop(2)  # This will delete and return index 2 value.
print(list2)

print("----------------------------------------------------------------------------------------")

# ****************************Tuples in Python:****************************

# A tuple is an immutable data type in Python.
# A tuple in python is a collection of elements enclosed in () (parentheses).
# Tuple, once defined, can’t be changed, i.e., its elements or values can’t be altered or manipulated.

# Tuples in Python :
a = ()    # It's an example of empty tuple
x = (1,)   # Tuple with single value i.e. 1
tup1 = (1, 2, 3, 4, 5)
tup1 = ('harry', 5, 'demo', 5.8)

# Note: To create a tuple of one element, it is necessary to put a comma  ‘,’ after that one element like this
# tup=(1,) because if we have only 1 element inside the parenthesis, the python interpreter will interpret it as a
# single entity which is why it’s important to use a ‘,’ after the element while creating tuples of a single element.

print("----------------------------------------------------------------------------------------")

# *********************Swapping of two numbers*********************

# Python provides a very handy way of swapping two numbers like below:

# Swapping of two numbers :

a = 10
b = 15
print(a, b)  # It will give output as: 10 15
a, b = b, a
print(a, b)  # It will give output as: 15 10

print("----------------------------------------------------------------------------------------")

# this is the method for writting the list...strings in double quotes and numbers directly
grocery = ["Harpic", "vim bar", "deodrant", "Bhindi", "Lollypop", 56]
# glocery named list is created
print(grocery)  # it will print whole list
# it will print specific desired name according to tye number
print(grocery[3])

print("----------------------------------------------------------------------------------------")

numbers = [2, 7, 9, 11, 3, 6, 8, 104]
# numbers named list is created
print(numbers)  # it will print whole list

# SLICING THE LIST

print(numbers[:5])  # it will print whole list
print(numbers[:])  # it will print whole list
print(numbers[::])  # it will print whole list
print(numbers[1:4])
print("Reverse slicing with negative")
# first it will reverse the list like
# 104  8  6  3  11  9  7  2
print(numbers[::-3])  # it will print whole list
numbers.remove(9)  # it will remove 9
print(len(numbers))  # will give how many numbers
print(max(numbers))  # will give maximum number
numbers.pop()  # it will remove the element whivh is written in index
numbers.sort()  # will sort elements in ascending order
#numbers = []
numbers.reverse()
numbers.append(1)  # will add element at end
numbers.append(72)
numbers.append(5)
numbers.insert(2, 67)
numbers[2] = 300  # it will change that second with 300

# extend() adds all elements of a list to another list
# pop() returns and removes an element at the given index
# clear() removes all items from the list
# index() returns the index of the first matched item
# copy() returns a shallow copy of the list

print(numbers)
3, 11, 9, 7, 2
print(numbers)
numbers[1] = 98
print(numbers)

print("----------------------------------------------------------------------------------------")

# TUPLING

# Mutable - can change
# Immutable - cannot change
tp = (1,)  # you need this extra comma for single element
# tp[1] = 8 # this will give error because tuple values cant be changed, these are immutable
print(tp)

print("----------------------------------------------------------------------------------------")

# SWAPPING PROCESS

a = 1
b = 8
print(a, b)
print("After swapping")
a, b = b, a  # this is easy

# This is old method

# temp = a
# a = b
# b = temp
print(a, b)

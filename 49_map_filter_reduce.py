# Why are lambdas relevant to map(), filter() and reduce()?
# These three methods expect a function object as the first argument. This function object can be a normal or predefined function. Most of the time, functions passed to map(), filter(), and reduce() are the ones we only use once, so there's often no point in defining a named function(def function).To avoid defining a new function, we write an anonymous function/lambda function that we will only use once and never again.

# map():
# "A map function executes certain instructions or functionality provided to it on every item of an iterable."

# The iterable could be a list, tuple, set, etc. It is worth noting that the output in the case of the map is also an iterable i.e., a list. It is a built-in function, so no import statement required.

# SYNTAX:
# map(function, iterable) 
# A map function takes two parameters:

# First one is the function through which we want to pass the items/values of the iterable
# The second one is the iterable itself
# Example:

items = [1, 2, 3, 4, 5]
a=list(map((lambda x: x **3), items))

print(a)

#Output: [1, 8, 27, 64, 125]
# The map()function passes each element in the list to a lambda function and returns the mapped object.

# filter():-
# "A filter function in Python tests a specific user-defined condition for a function and returns an iterable for the elements and values that satisfy the condition or, 
# in other words, return true."

# It is also a built-in function, so no need for an import statement. All the actions we perform using the filter can also be performed by using a for 
# loop for iteration and if-else statements to check the conditions. 
# We can also use a Boolean that could take note of true or false, but that would make the process very lengthy and complex. So, to simplify the code, 
# we can use the filter function.

# SYNTAX:
# filter(function, iterable)
# It also takes two parameters:

# First one is the function for which the condition should satisfy
# The second one is the iterable
# Example:
a = [1,2,3,4,5,6]
b = [2,5,0,7,3]
c = list(filter(lambda x: x in a, b))
print(c) # prints out [2, 5, 3]
# reduce():
# "Reduce functions apply a function to every item of an iterable and gives back a single value as a resultant".

# Unlike the previous two functions (Filter and Map), we have to import the reduce function from functools module using the statement:

# from functools import reduce

# We can also import the whole functools module by simply writing

# Import functools

# But in the case of bigger projects, it is not good practice to import a whole module because of time restraint.

# SYNTAX:
# reduce(function, iterable)
# Example:

from functools import reduce
a=reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
print(a) 
#Output: 24
#  Like the previous two, it also takes two-parameter. First one is the function and the second one is the iterable

# Its working is very interesting as it takes the first two elements of the iterable and performs the function on them and converts them into a single element. 
# It proceeds further, taking another element and performing the function of that one and the new element. 
# For example, if we have four digits and the function wants to multiply them, then we can first multiply the first two and then multiply the third one in 
# their resultant and then the forth and so on. The reduce is in the functools in Python 3.0. It is more complex. It accepts an iterator to process, 
# but it is not an iterator itself. It returns a single result.





# ******************************************  MAP ***************************************************

print("\n***************************************** MAP ***************************************************")
numbers = ["3", "45", "96"] # these are in form of string so for doing operations with numbers we have to typecast it.

#so we can typecast it with help of for loop

#This is not correct method to do that 

# for i in range(len(numbers)): # if we are using range it demands only integers...
#     numbers[i] = int(numbers[i])

print(map(int, numbers))
numbers = list(map(int, numbers))   # so here map made all elements of numbers integer
                                    # map returns objects

numbers[2] = numbers[2] + 2
print(numbers[2]) # It will add 2 with 96

def sq(a):
    return a*a

num = [2,3,4,5,7,9,2,3,4]
square = list(map(sq, num))
print(square)

# If any function is not defined then we can do this

num = [2,3,4,5,7,9,2,3,4]
square = list(map(lambda x: x*x, num))
print("This squaring is done by lambda function", square)

print("****************************************************************************************************************")

def squa(a):
    return a * a

def cube (a):
    return a * a * a

func = [squa, cube] # List is created of function names

for i in range(5):
    val = list(map(lambda x:x(i), func)) # ye jo lambda he vo func ke dono sqaure and cube pe apply hoga to vo ek bar square and ek bar cube return karega
    print(val)


#  ****************************************** FILTER *******************************************************

print("\n****************************** FILTER *******************************************************")

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_greater_5(num): # ek function banaya jo ki ek number agar 5 se bada hoga to hi value return karega
    return num > 5

#creating a list

gr_than_5 = list(filter(is_greater_5, list_1))
gr_than_5_map = list(map(is_greater_5, list_1))

print(gr_than_5)
print(gr_than_5_map)

#************************************************** REDUCE ************************************************************

print("\n*********************************************** REDUCE ******************************************************")

from functools import reduce

list1 = [1, 2, 3, 4] #If we want to add those all

#This is old method

# num = 0
# for i in list1:
#     num = num + i
# print("Addition is",num)

addi = reduce(lambda x, y : x + y, list1)
mul = reduce(lambda x, y : x * y, list1)

print("This addition is by reduce", addi)
print("This multiplication is by reduce", mul)
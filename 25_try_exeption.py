# Try Except Exception Handling In Python
# Before discussing exceptional handling, let us discuss, what an exception is actually.
# “Exception can be said as an error, that causes a program to crash. Unlike syntax error, it is syntactically correct and occurs mostly due to our negligence”
# For example, assigning a string value to an int data type variable or dividing a number by zero or also when a name of a variable or a function is not found, 
# an exception occurs. Python has built-in support for dealing with many sorts of exceptions automatically, but we can also define our own.

# The solution to exception related problems is simple. We just have to alter the normal flow of the program by a bit of code known as an exception handler. 
# This code will save the state of the program up to the point where the exception occurred and will continue the normal flow from the 
# code written outside the area of occurrence of an exception. We can also print the exception by converting it into a string. 
# This way program does not terminate but executes completely except for the area where the exception occurred.

# Now as we have covered the basics, let us move towards an in-depth understanding of exception handling. 
# Try and except blocks are used in Python to handle the exception. If you are familiar with any other programming language, 
# the except block is the same as the catch block. In the try block, we write the code about which we have doubt that exception could occur in it, 
# and in except block we just write the code that we want to execute in case the exception error occurs. In such cases where no exception occurs, 
# the except block will not execute. In simple words, in the try block, we write the code where chances of exception are high, 
# and in except block, we handle the error, maybe through printing a warning or just skipping the exception part completely 
# by completely ignoring it as a part of the program.

# We can also use an else keyword to print something if no exception occurs. For example. In case of an exception, 
# the except block is printing the error, likewise, if the exception does not occur, we could print a statement that 
# no error occurred, using an else keyword.

# There are also many sorts of predefines exceptions that we could find in Python such as EOF or End of File Error 
# (occurs when the end of a file is reached but the operation is not completed) or ZeroDivisionError (occurs when the number is divided by zero). 
# We can code such expect blocks that catch only specific sort of exception and ignore the rest. 
# For this purpose, we have to specify the error name after the keyword except, before putting the colon.


# Advantages of using try and catch

# Without a try block if an exception occurs the program will surely crash.
# If we have some part of code that is not much important but can cause an exception, 
# then we must write it down in the try block so it does not cause the whole program to crash.





print("Enter num 1")
num1 = input()
print("Enter num 2")
num2 = input()

# yaha pe try matlab, iss try me jo bhi function or print ho, vo sahi se run hua to bhi acha he aur nahi bhi hua run hua aur error aa raha to bhi programm age badhega 
# program rokega nahi. Agar error nahi aya to bhi code run hoga ur error aya to bhi age code jayega.
#try matlab vo sirf try karta he ... isme koi bhi error aya to sirf error show hoga and program age badhega exeption ki taraf jo ki bahoot jada important rahega ki jo 
# print or execute hona hi he

try:
    print("The sum of these two numbers is",
          int(num1)+int(num2))

# Execption matlab try me kuch bhi ho, exeption me jo hoga vo run hoga hi....Its like try and error   ...and move forward

except Exception as e:  # This is a confirmed syntax 
    print(e)

print("This line is very important")  # Thus will be printed at any condition


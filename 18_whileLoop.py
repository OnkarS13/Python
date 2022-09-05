# While Loops In Python

# In the previous tutorial, we discussed about loops in general, what they are and their benefits, why we should use them, 
# along with syntax, and the working of the “for” loop. 
# If you haven’t gone through that tutorial till now, I will recommend you to go through that first, 
# so it will be easier for you to learn the concept of while loop, once you have the concept, what loops generally are.

# Now, as we know now what loops are and why they are used, in this section, I will go directly towards the working and syntax 
# of while loop along with its comparison with for loop and where to use it.

# “A while loop in python runs a bunch of code or statements again and again until the given condition is true when the condition becomes false, 
# the loop terminates its repetition.”

# The syntax for a while loop is simple and very much like for loop. 
# We have to use the keyword “while”, along with it, we have to put a condition in parenthesis, and after that, a colon is placed. 
# pThe condition could be either true or false. Until the condition is true, the loop will keep on executing again and again. 
# If we use a certain condition in our while loop that never becomes false, the program will continue running endlessly until we stop it by force. 
# So, this kind of mistake in our syntax is known as logical/human error.

# To terminate an infinite loop, you can press Ctrl+C on your system.

# Syntax of while loop:

# while codition_is_true:
#     Code inside the loop body

# For vs. While:

# A “for” statement loop runs until the iteration through, set, lists, tuple, etc., or a generator function is completed. 
# In the case of a while loop, the statement simply loops until the condition we have provided becomes false. 
# We generally use for loops for areas where we are already familiar with the number of iterations and use while loop where the number of iterations are unknown. 
# ecause while the loop is solely based on the state of its condition.

# Let us understand the concept of the while loop and why we use it in areas where the number of iterations are not defined, 
# or we do not have any idea how many iterations would take place with the help of an example. 
# Suppose that we have created an application for an ATM from where a customer can only withdraw money up to 5000 rupees. 
# Now our condition in the while loop would be to iterate unless the input is between 1 to 5000. 
# So, the condition will be true unless the user inputs a number between 1 to 5000, 
# so the loop will iterate depending upon the time until the user submits the wrong input. 
# The example is a bit rough, but I hope it helps you clear your concepts.

# For a While loop to run endlessly, we can pass true or 1 as a condition. 1 is also used in place of writing true as a whole. 
# So, in this case, the condition will never become false, so the program will run endlessly. 
# But these kinds of programs do not output anything because they can never complete their execution.







#SYNTAX

# while codition_is_true:
#     Code inside the loop body

i = 0
while ( i < 45):
    i = i + 1 # this will print from 1 to 45
    print (i)

i = 0
while ( i < 45):
    print (i)
    i = i + 1 # this will print from 0 to 44
# Using With Block To Open Python Files
# There is more than one way to open and close a file. The one we have studied till now is using the open() and close() function. 
# In today's tutorial, we will go through another yet better and straightforward approach of opening and closing files.
# We will see how we can use, with block to open and close a file, including syntax and benefits. 
# We will be using f as our file’s object.

# Opening and closing of files are necessary and crucial steps in file handling. 
# We cannot read, write, or perform any task on a file without opening it first. 
# Everyone is familiar with it because it is the first step in file handling. 
# But what most of us are not familiar with is how vital closing a file is. If we do not close our file after we are done using it, 
# then the file object will keep on consuming processor memory, and also, there will be more chances of exceptions as the file is still open hence, 
# more chances of bugs.

# To save ourselves from such situations, we could use a with block to open files.


# Its syntax is simple:

# With open(“file_name.txt”) as f:


# f being the object of the file. The important thing to note is, there is no close() function required. After running the code in the block, 
# the file will automatically be closed.  

#  Now at this level, closing a file does not seem like a big issue, but when we are working on more significant projects with a higher number 
#  of files then there are instances where we tend to forget that we have closed our file. In such situations, chances of bugs occurrence increase, 
#  and we can not access a file elsewhere until it is closed properly. Also, the program will require more processing power. 
#  So, even if we are not dealing with a more significant project now, still closing a file is a good practice because, as a programmer, 
#  I can tell you that the practices you adopt now will soon become habits, and they will be difficult to let go.

# What opening a file with "With block" actually does is to create a context manager that automatically closes a file after processing it. 
# Another benefit of using a “With block” is that we can open multiple files in a single block by separating them using a comma. 
# All the files could have different modes of opening. For example, we can access one file for reading and another one for writing purposes. 
# Both files should have different objects referring to them.

# The syntax would be:

# With open(“file1txt”) as f, open(“file2.txt”) as g
# Both files will be simultaneously closed together.

# Let us once again briefly go over the advantages of With block:
# Multiple files can be opened.
# The files that are opened together can have different modes
# Automatically closes file
# Saves processing power by opening and closing file only when running code inside the block
# Creates a context manager, so lesser chances of an exception occurring







with open("29_onkar.txt") as onkarF: # here this line means that 29_onkar.txt file is opening with the variable onkarF 
    # print(onkarF.read(8)) # it will read first 8 characters and it will print those here
    
    # another method
    
    m = onkarF.read(8) # here onkarF is assigned to m and m is printed
    print(m)

print("-------------")

file = open("29_onkar.txt")
cont = file.read(10)
print(cont)

# if we used both the methods in same program, they will work

# Open(), Read() & Readline() For Reading File
# As we now have an idea of what files(text or binary) are and their access modes, we are now ready to dive into the discussion of file handling methods. 
# When we want to read or write a file (say on our hard drive), we must first open the file. 
# When we open a file, we are asking the operating system to find the file by name, making sure the file exists.

# How to open a file?
# Python has a built-in open() function to open a file.

# The syntax of the function is:

# open("filename" ,"mode")

# To open a file, we must specify two things,

# Name of the file and its extension
# Access mode where we can specify in which mode file has to be opened, it could either be read (r), write (w) or append(a), etc. 
# For more information regarding access modes, refer to the previous tutorial.

# For Example, 
# open("filename" ,"mode")

# The file “myfile.txt” will open in "rt" mode as it is the default mode. But the best practice is to follow the syntax to avoid errors.

# The open function returns a file object. We store this file object into a variable which is generally called as a file pointer/file handler. 
# Here is a code snippet to open the file using file handing in Python,

# f=open("myfile.txt," "w")

# You can use this file pointer to further add modifications in the file. An error could also be raised if the operation fails while opening the file. 
# It could be due to various reasons like trying to access a file that is already closed or trying to read a file open in write mode.

# How to read a file?
# To read a file in Python, there are various methods available,
# We can read a whole file line by line using a for loop in combination with an iterator. This will be a fast and efficient way of reading data.
# When opening a file for reading, Python needs to know exactly how the file should be opened. Two access modes are available reading (r), and reading in binary mode (rb). 
# They have to be specified during opening a file with the built-in open() method.

# open("filename" ,"mode")

# You can use the readline() method to read individual lines of a file. By calling readline() a second time, you will get the next line.
# readlines() method reads until the end the file ends and returns a list of lines of the entire file. It does not read more than one line.    

# f=open("myfile.txt","r");
# f.readlines() #Returns a list object

# Note: The default mode to read data is text mode. If you want to read data in binary format, use ''rb".

# Is it necessary to close a file?

# The answer is yes, it is always the best practice to close a file after you are done performing operations on it. 
# However, Python runs a garbage collector to clean up the unused objects, but as good programmers, we must not rely on it to close the file. 
# Python has a build-in close() function to close a file i.e;

# f.close()






# read and text mode are default.
# open("filename", "mode")

file_Onkar = open("27_myfile.txt")

content = file_Onkar.read(5)  # yaha pe read (5) matlab ye sirf first 5 letters print karega aur bakike letters next wala f.read() karega # here f is assigned to content which have work of read the file 
print("1", content) # and here content is being print

print()

#if you want to write the lines using for loop,then you dont have to write the above lines, this is effient way
for line in file_Onkar:
    print(line, end= " ") # ab yaha pe hi sab lines read ho chuki he to ab niche ke functions ko print karne ke liye kuch nahi bacha to kuch print nahi hoga

print()

print(file_Onkar.readline())  # by this way also,  we can write the lines ....line by line
print(file_Onkar.readline())
print(file_Onkar.readline())

print()

print(file_Onkar.readlines()) # by this readlines, we can write the lines in form of list

print()

content = file_Onkar.read()  # here f is assigned to content which have work of read the file 
print("2", content) # and here content is being print

file_Onkar.close() # you must have to close the fioe after opening it It is a good practice




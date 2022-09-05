# *********************String Slicing And Other Functions In Python*********************

# The string is a data type in Python. 
# Strings in Python programming language are arrays of bytes representing a sequence of characters. 
# In simple terms, Strings are the combination or collection of characters enclosed in quotes. 
# Strings are one of the most used data types in any programming language because most of the real-world data 
# such as name, address, or any sequence which contains alphanumeric characters are mostly of type ‘String’.

# Primarily, you will find three types of strings in Python :

# Single Quote String – (‘Single Quote String’)
# Double Quote String – (“Double Quote String”)
# Triple Quote String – (‘’’ Triple Quote String ‘’’)
# Let us now look into some functions you will use to manipulate or perform operations on strings.

# len() Function : This len() function returns the total no. of characters in a string. 
# E.g., for string a="abc", len(a) will return three as the output as it is a string 
# variable containing 3 characters
x = "String Demo"
# This string variable x contains a string containing 11 characters (including spaces). 
# Since the index in a string starts from 0 to length-1, this string can be looked at as:

# String Slicing :

# 1. As we know, the meaning of the word ‘slice’ is ‘a part of.’ 
# I am sure you have sliced paneer cubes at home!

# 2. Just like paneer slice refers to the part of the paneer cube; 
# In Python, the term ‘string slice’ refers to a part of the string, 
# where strings are sliced using a range of indices.

# 3. To do string slicing, we just need to put the name of the string followed by [n:m]. 
# It means ‘n’ denotes the index from which slicing should start, 
# and ‘m’ denotes the index at which slicing should terminate or complete. 
# Let's look into an example!


#           0    1    2    3    4    5    6    

#   word    a    m    a    z    i    n    g    

#          -7   -6   -5   -4   -3   -2   -1
 
# word[0 : 7]   will give    'amazing'    (the letters starting from index 0 going up till 7 - 1 ie., 6: from indices 0 to 6, both inclusive)
# word[0 : 3]    will give   'ama'        (letters from index 0 to 3 - 1 ic., 0 to 2)
# word[2: 5]    will give    'azi'        (letters from index 2 to 4 (¿e., 5 - 1) )
# word[-7 : -3]  will give   'amaz'       (letters from indices -7, -6, -5, -4 excluding index -3)
# word[-5 : -1]  will give   'azin'       (letters from indices -5, 4, -3, -2 excluding -1)
 
# In Python, string slicing s[n:m] for a string s is done as characters of s from n to m-1. 
# It means characters are taken from the first index to the second index-1.
# E.g., abc="Demo" then abc[0:3] will give ‘Dem’ and will not give ‘Demo’ coz 
# index number of ‘D’ is 0, ‘e’ is 1, ‘m’ is 2, and ‘o’ is 3. So it will give a range from n to m-1, 
# i.e., 0 to 3-1=2. That’s why we got the output ‘Dem’.


# word[7]     will give 'amazing'   (missing index before colon is taken as 0(zero))
# word[:5]    will give 'amazi'     (-do-)
# word[ 3: ]  will give 'zing'      (missing index after colon is taken as 7 (the lengih of the string) ) 
# word [5:]   will give 'ng'        ( -do-)

# In string slicing, we sometimes need to give a skip value 
# i.e. string[n:m:skip_value]. This simply takes every skip_valueth character. 
# By default, the skip value is 1 but if we want to choose alternate characters
# f a string then we can give it as 2. Have a look at the example below:

# >>> word [1:6:2]     'mzn'        It will take every 2nd character starting from index = 1 rill index < 6.
# >>> word [-7:-3:3]   'az'         It will take every 3rd character starting from index = -7 1o index < -3.
# >>> word [: : -2]    'giaa'       Every 2nd character taken backwards,
# >>> word [: :-1]     'gnizama'    Ever character taken backwards.


# Let's end this tutorial by looking into some of the most used string functions :

# string.endswith(): This function allows the user to check whether a given string ends with a passed argument or not. It returns True or False.
# string.count(): This function counts the total no. of occurrences of any character in the string. It takes the character whose occurrence you want to find as an argument.
# string.capitalize(): This function capitalizes the first character of any string. It doesn’t take any argument.
# string.upper(): It returns the copy of the string converted to the uppercase.
# string.lower(): It returns the copy of the string converted to lower case.
# string.find(): This function finds any given character or word in the entire string. It returns the index of the first character from that word.
# string.replace(“old_word”, “new_word”): This function replaces the old word or character with a new word or character from the entire string.




# REFFER STRING FUNCTIONS IN PYTHON ON GOOGLE


mystr = "Harry is a good boy"
print(mystr[6]) # it will print that character present at that number 
print(len(mystr)) # it will print legth of that line
print(mystr[0 : 9]) # it will print character starting from including  0 and excluding 9
print(mystr[0 : 70]) # it will print whole line upto 70 characters
print(mystr[0 : 19 : 3]) # first it will print 0 to 4 and 3 means it will print every 3 character from starting 
print(mystr[ : ])  # whole line will be printed
print(mystr[ : : ])  # whole line will be printed
print(mystr[0:19:1])  # These are default values of above line
print( )

# NEGATIVE SYSTEM

# "H  a  r  r  y   i  s   a   g  o  o  d   b  o  y"
# -19 -18 -17 -16 -15                -4 -3  -2   -1   like this

print(mystr[-10:]) # it will print from reverse side, -10 to -1 word will be printed

print(mystr.isalnum())  #false mean that there are spaces between the line if, those spaces are removed it will be true

print(mystr.endswith("boy")) # it will be true bcoz line ends with boy 
print(mystr.endswith("bdoy")) # it will be false bcoz line does not ends with bdoy   
print(mystr.count("o"))  # it will count, how many times for o is printed
print(mystr.capitalize()) # it will capitalize the first letter of line
print(mystr.replace("is", "are")) # this is used for replacing words
print(mystr.find("is")) # it will give that from is is starting
print(mystr.lower()) # line will be converted to lower caese
print(mystr.upper()) # line will be converted to upper caese

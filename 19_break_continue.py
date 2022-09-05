# Break & Continue Statements In Python
# “Break and continue statements are used to alter the flow or normal
# working of a loop, that could be either a “for loop” or “while loop”.

# If you are not familiar with the concept of loops, I recommend you go through
# Tutorial numbers 16 and 17 of Python Tutorials For Absolute Beginners In Hindi Playlist.


j = 0
while(j < 45):
                                # this end means that after every i, end " ", isme jo bhi likhega vo uske bad print hoga
    print(j + 1, end=", ")
    j = j + 1

print()

i = 0
while(True):  # condition true kiya to loop infinite pe chalega
    if i+1 < 5:
        i = i + 1
        continue

    print(i+1, end=" ")

    if(i == 44):
        break  # this will break the loop when reached to 44
    i = i + 1

print()

while(True):
    # print("Enter a number")
    # inp = int(input()) # here type casting is done...string to integer

    inp = int(input("Enter a Number\n"))

    if inp > 100:
        print("Congrats you have entered a number greater than 100 \n")
        break
    else:
        print("Try again !")
        continue

print()

i = 0
while(True):
    # here f string is used for repeating the lines and {i} this syntax is also compulsory
    print(f"The value of i is : {i}")
    i = i + 1  # here increment is done
    if(i > 10):
        print("Breaking the loop. ")
        break


print()

i = 0
while(True):
    i = i + 1  # increamenting by one and so on

    if(i == 5):
        continue  # this will skip 5 and move forword
    elif(i > 10):
        break
    print(f"The value of i is : {i}")

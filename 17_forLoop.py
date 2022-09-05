# **************SYNTAX*******************
# FOR LISTS

# for_vaiable names_ in _list name
# print(variable names separated by commas)

# FOR DICTIONARY

# for_variable names_in_dictionary name_.items():
# print(variable names separated by commas)


dict1 = {"Best Python Course": "CodeWithHarry",
         "Best C Languge Course": "CodeWithHarry",
         "Harry Sir": "Tom Cruise Of Programming"}

# dictionary are always in {} these braces
# hame dictionary me agar for loop use karna padega to .items(): lagana hi padega

for x, y in dict1.items():  # yaha pe dict1 ke bad .items(): lagana hi padega
    print(x, y)  # this will in the form of string like single line

print()

for x in dict1.items():  # yaha pe dict1 ke bad .items(): lagana hi padega
    print(x)   # this will in the form of list separated by comma

print()

list1 = [["Harry", 1], ["Larry", 2],
         ["Carry", 6], ["Marie", 250]]

dict2 = dict(list1)  # haya pe list ko type casting karke dictionary banaya he

for item in dict2:
    print(item)

print()

for item, item2 in dict2.items():  # agar hame ek se jada items print karwane ho to   dictionary_name.items()  ye likhana padega
    print(item, item2)

for item, lollypop in dict2.items():

    print(item, "and lolly is ", lollypop)

print()

items = [int, float, "HaERRY", 5, 3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item >= 6:
        print(item)

print()

num = 100
balance_amount = int(input("Enter you balance:- "))

for i in range(num):
    # here in range means that you are providing a condition ...like i will be printed less than 100
    item = input("Enter item name or Enter '0' for exit:- ")
    if item == "0":
        break

n = 20
number_of_guesses = 1

print("You have to guess a number and you will get 9 chances !")
while(number_of_guesses <= 9):
    guess_num = int(input("Guess the number:- "))
    if guess_num < 20:
        print("Please enter bigger number !")
    elif guess_num > 20:
        print("Please enter smaller number !")
    else:
        print("\n You won !")
        print(number_of_guesses, "no. of guesses you took to finish !")
        break
    print(9 - number_of_guesses, "no. of guesses are remaining !")
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses > 9):
    print("You lost the game !")

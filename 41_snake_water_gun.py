#snake water gun

import random

lst = ['s', 'w', 'g']
print("You are playing snake water gun game ! starting your game !")

computer = 0
user = 0
n = 0
chance = 10

print(" \t \t \t \t Snake Water Gun Game \n \n")
print("s for snake \nw for water \ng for gun")
while(n <= chance):
    print("Please enter your choice among :- 's', 'w', 'g'")
    player = input()
    cho = random.choice(lst)
    
    
    
    if cho == 's' and player == 'w':
        computer = computer + 1
        print(f"You choosed {player} and computer choosed {cho}")
        print("Computer wins 1 point !")
        print("Snake will drink water, so computer have won this round! amd 1 point to computer")
        
    elif cho == 'w' and player == 's':
        user = user + 1
        print(f"You choosed {player} and computer choosed {cho}")   
        print("You wins 1 point !")
        print("Snake will drink water, so you have won this round! amd 1 point to player")
        
    elif cho == 'g' and player == 'w':
        user = user + 1
        print(f"You choosed {player} and computer choosed {cho}")
        print("You wins 1 point !")
        print("The gun will drown in water, so you have won this round! and 1 point to player")
        
    elif cho == 'w' and player == 'g':
        computer = computer + 1
        print(f"You choosed {player} and computer choosed {cho}")
        print("Computer wins 1 point !")
        print("The gun will drown in water, so computer have won this round! and 1 point to computer")
        
    elif cho == 's' and player == 'g':
        user = user + 1
        print(f"You choosed {player} and computer choosed {cho}")
        print("You wins 1 point !")
        print("The gun will kill snake, so you have won this round! and 1 point to player")
        
    elif cho == 'g' and player == 's':
        computer = computer + 1
        print(f"You choosed {player} and computer choosed {cho}")
        print("Computer wins 1 point !")
        print("The gun will kill snake, so computer have won this round! and 1 point to computer")

    elif cho == player:
        print("Its a tie ! you both choosed same")

    else:
        print("You have choosed wrong input !")

    n = n + 1
    print(f"{chance - n} is left out of {chance}") # here f string is used

print("Game Over !")

if computer == user:
    print("Its a Tie !")

elif computer > user:
    print("Computer wins and you loose !")

else:
    print("You win and computer loose !")

print(f"Your points are {user} and computer's points are {computer}")




        
         
    


































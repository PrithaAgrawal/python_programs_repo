
import random

user_points=0
computer_points=0
options=["rock","paper","sissor"]

while True :
    user=input("type rock/paper/sissor if wanna play or else type q to quit: ").lower()
    if user == "q":
        break

    if user not in options:
        continue
    
    #here in options, rock is 0, paper is 1, sissor is 2 so, 1st and last option is written below
    random_options= random.randint(0,2)
    computer_choice= options[random_options]
    
    print("computer's pick is:",computer_choice)

    if user.lower() == "rock" and computer_choice=="paper":
        print("you lose :(")
        computer_points += 1 

    elif user.lower() == "sissor" and computer_choice == "rock":
        print("You lose :(")
        computer_points += 1

    elif user.lower() == "paper" and computer_choice == "sissor":
        print("You lose :(")
        computer_points += 1

    else:
        print("You win :)")
        user_points +=1

print("Your score is:",user_points)  
print("Computer's score is",computer_points)
print("THANK YOU FOR PLAYING :)")

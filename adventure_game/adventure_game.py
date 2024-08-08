print ("WELCOME TO THE ADVENTURE!!!")
user_name = input("Please enter your name: ")

vehicle=input("Please choose your vehicle DIRT BIKE or BATTLESHIP: ")

if vehicle == "dirt bike":
    dirt_bike= input("You are stuck in a forest and skinwalker is chasing you, you have 2 choices:" 
                     " 1.turn left"
                     " 2.turn  right"
                     " (Choose between left/right): ")
    if dirt_bike == "left":
        waterfall=input("You got a speed boost!!There is waterfall in front of you. you have two options:"
                        " 1. drop your bike and swim"
                        " 2. try to cross it with your bike."
                        " (Choose from swim/cross):")
        if waterfall == "swim":
            danger1=input("You crossed the river succesfully.now in front of there's a cave. There are two options:"
                          " 1.explore the cave"
                          " 2. back off"
                          " (Choose between in/out):")
            if danger1 == "in":
                print("The skinwalker fell into the ravine.You saw the tresure in front of you.")
                print("CONGRATULATIONS ;) YOU WON!!")
            elif danger1 == "out":
                print("You tried to back off. The skinwalker caught you and ripped your flesh off.")
                print("YOU ARE DEAD!! YOU LOST")
            else:
                print("please type correct value.")
        elif waterfall == "cross":
            print("You tried to cross the river but your bike slipped and you fell into the ravine. You lost")
        else:
            print("Please type a correct value")
    elif dirt_bike == "right":
        print("You choose right, and there was a ravine and you fell in it. You lost.")
    else :
        print("Please type a correct value.")
elif vehicle == "battleship":
    battleship= input("you own a battleship and a scylla is approching you. You have two options"
                      " 1.attack the scylla "
                      " 2.run away"
                      " (Choose between attack/run): ")
    if battleship == "attack":
        danzor1=input("It was a weak scylla it died in no time. Now you see a huge wave approaching.You have two options:" 
                      " 1.drop the ship and swim through the wave"
                      " 2.face the wave with the ship" 
                      " (Choose between drop/fight): ")
        if danzor1 == "fight":
            danzor2 =input("You fought with great courage and overcame the huge wave.Now you see two ways in front of you "
                           " (Choose from left/right): ")
            if danzor2 == "left":
                print("There was a huge crocodile waiting for you to be its meal.You died.You lost")
            elif danzor2 == "right":
                print("You found your way to the island and found the tresure.")
                print("CONGRATULATIONS ;) YOU WON!!")
            else :
                print("Please type a correct value.")
        elif danzor1 == "drop":
            print("You dropped the ship,the wave was too big for you to handle.You got washed away.You lost")
        else :
            print("Please type a correct value.")
    elif battleship == "run":
        print("You tried to run away but the scylla catched you and tore you apart. YOU ARE DEAD.")
    else :
        print("please type a correct value.")
else:
    print("please type a correct value.GOODBYE")

print("GAME OVER. Thank you for playing :)")

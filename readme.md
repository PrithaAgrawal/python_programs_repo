# My Python Programs

This repository contains a collection of Python programs I created to practice and learn Python programming. Each program is organized into its own folder.

## List of Programs

1. **adventure_game.py**: A text-based interactive fiction game where players make choices that shape the story's outcome.
2. **binary_search.py**: A Python implementation of the binary search algorithm for efficiently finding elements in a sorted list.
3. **calculator.py**: A basic calculator that performs arithmetic operations like addition, subtraction, multiplication, and division.
4. **die_game.py**: A simple dice-rolling game that generates random numbers between 1 and 6.
5. **madlibs_generator.py**: A fun word game where user inputs are used to generate a humorous story.
6. **no_guesser.py**: A number guessing game where the player tries to guess a randomly generated number with hints.
7. **password_manager.py**: A tool to securely store, retrieve, and manage passwords.
8. **password_strength_tester.py**: A program that evaluates and scores the strength of a given password.
9. **passwords.txt**: A text file used to store passwords managed by the password manager.
10. **quiz_game.py**: A multiple-choice quiz game that tests the user's knowledge on various topics.
11. **rock_paper_scissors.py**: A command-line version of the classic Rock, Paper, Scissors game.
12. **story.txt**: A text file containing a story or narrative, potentially used in madlib_generator.py.
13. **tic_tac_toe.py**: A Python implementation of the Tic-Tac-Toe game for two players.
14. **time_math_challenge.py**: A math quiz game where players solve arithmetic problems under time pressure.

## Folder Structure

- `adventure_game/`
  - `adventure_game.py`:
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

**- `binary_search.py/`**
   -  `binary_search.py`:
   
def binary_search(a_list, an_item):
    first = 0 
    last = len(a_list) - 1

    while first <= last:
        mid_point = (first + last) // 2
        if a_list[mid_point] == an_item :
            return True
        else:
            if an_item < a_list[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point +1
    return False

def binary_searching(a_list, first, last, an_item):
    if len(a_list) == 0:
        return False
    else:
        mid_point = (first + last) // 2
        if a_list[mid_point] == an_item :
            return True
        else:
            if an_item < a_list[mid_point]:
                last = mid_point - 1
                return binary_searching(a_list, first, last, an_item)
            else:
                first = mid_point +1
                return binary_searching(a_list, first, last, an_item)
            
if __name__ =='__main__':
    user_input = input("Enter a sorted list of numbers separated by spaces: ")
    a_list = list(map(int, user_input.split()))
    an_item = int(input("Enter the number to search for: "))
    print('Binary Search Recursive:',binary_searching(a_list, 0, len(a_list) -1, an_item))

**- `calculator.py/`**
   - `calculator.py`:
   import os

def addition():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Addition')

    continue_calc = 'y'

    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))
    ans = num_1 + num_2
    values_entered = 2
    print(f'current result =  {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input("Enter more (y/n): "))
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter from \'y\' or \'n\'.')
            continue_calc = (input('Enter more (y/n):'))

        if continue_calc.lower() == 'n':
            break
        num = float(input("Enter another number: "))
        ans += num
        print(f'current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def substraction():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Substraction')

    continue_calc = 'y'

    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))
    ans = num_1 - num_2
    values_entered = 2
    print(f'Current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input("Enter more (y/n): "))
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter from \'y\' or \'n\'.')
            continue_calc = (input('Enter more (y/n): '))
        if continue_calc.lower() == 'n':
            break
        num = float(input("Enter another number: "))
        ans -= num
        print(f'current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def multiplication():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Multiplication')

    continue_calc = 'y'
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter the seond number: "))
    ans = num_1 * num_2
    values_entered = 2
    print(f'Current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input("Enter more (y/n): "))
        while continue_calc.lower() not in ['y', 'n']:
            print("Please enter from \'y\' or \'n\'.")
            continue_calc = (input('Enter more (y/n): '))
        if continue_calc.lower() == 'n':
            break
        num = float(input("Enter another number: "))
        ans *= num
        print(f'current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def division():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('division')

    continue_calc = 'y'

    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter the seond number: "))
    while num_2 == 0.0:
       print('Please enter a second number > 0')
       num_2 = float(input('Enter another number: '))

    ans = num_1 / num_2
    values_entered = 2
    print(f'Current result: {ans}' )
       
    while continue_calc.lower() == 'y':
        continue_calc = (input("Enter more (y/n): "))
        while continue_calc.lower() not in ['y', 'n']:
            print("Please enter from \'y\' or \'n\'.")
            continue_calc = (input('Enter more (y/n): '))
        if continue_calc.lower() == 'n':
            break
        num = float(input("Enter another number: "))
        while num == 0.0:
            print('Please enter a number > 0')
            num = float(input('Enter another number: '))
        ans /= num
        print(f'current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def calculator():
    quit = False
    while not quit:
        result = []
        print('Simple calculator in python !!!')
        print("Enter \'a\' for addition.")
        print("Enter \'s\' for substraction.")
        print("Enter \'m\' for multiplication.")
        print("Enter \'d\' for division.")
        print("Enter \'q\' for quit.")

        choice = input('Selection: ')

        if choice == 'q':
            quit = True
            continue

        if choice == 'a':
            result = addition()
            print('Ans = ', result[0], ' total inputs: ', result[1])
        elif choice == 's':
            result = substraction()
            print('Ans = ', result[0], ' total inputs: ', result[1])
        elif choice == 'm':
            result = multiplication()
            print('Ans = ', result[0], ' total inputs: ', result[1])
        elif choice == 'd':
            result = division()
            print('Ans = ', result[0], ' total inputs: ', result[1])
        else:
            print("Sorry invalid entry :(")

if __name__ == '__main__':
    calculator()

**- `die_game.py/`**
   - `die_game.py`:
   import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players (2-4)")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("players must be between 2-4 ")
    else:
        print("invalid try again")
    
max_score = 50 
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx +1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score=0
        
        while True:
            should_roll = input("Would you like to roll(y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled 1 ! Turn done")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a ", value, "!")

            print("Your current score is:", current_score)
            
        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx +1," Is the winner with a score of:",max_score)

**- `madlibs_generator.py/`**
   - `madlibs_generator.py`:
    with open("story.txt","r") as f:
    story = f.read()

words = set()
starting_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        starting_word = i 

    if char == target_end and starting_word != -1:
        word = story[starting_word: i + 1]
        words.add(word)
        starting_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for" + word + ":")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)

**- `no_guesser.py/`**
   -`no_guesser.py`:
  import random

top_of_range = input("Type the range of number starting from 0 : ")
random_number= random.randint(-1, 11)

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number next time!!")
else:
    print("please type in a digit next time.")
    quit()

random_number = random.randint(0,top_of_range)
guesses=0

while True:
    guesses += 1
    user_guess = input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type in a digit next time.")
        continue

    if user_guess == random_number:
        print("you got it!!")
        break
    else:
        if user_guess > random_number:
            print("you were above the number!")
        else:
            print("You were below the number.")

print("you got it in",guesses, "guesses")

**- `password_manager.py/`**
   -`password_manager.py`:
  from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|"+ fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

- `password_stregnth_tester.py/`
  - `password_stregnth_tester.py`:
    import string
import getpass

def password_stregnth_checker():
    password = getpass.getpass("Enter your password: ")
    stregnth = 0 
    lower_count = 0
    upper_count = 0
    space_count = 0 
    special_char_count = 0 
    num_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char in string.whitespace:
            space_count += 1
        else:
            special_char_count += 1
    
    if lower_count >= 1:
        stregnth += 1
    if upper_count >= 1:
        stregnth += 1
    if space_count >= 1:
        stregnth += 1
    if special_char_count >= 1:
        stregnth += 1
    if num_count >= 1:
        stregnth += 1 
    
    if stregnth == 1:
        print("That is a verry poor password."+"Can be easily hacked.")
    elif stregnth == 2:
        print("Weak password")
    elif stregnth == 3:
        print("Poor password. Can be improved.")
    elif stregnth == 4:
        print("Pretty strong password. The harder the better")
    else :
        print ("That's a hell of a password. Hackers are crying in corner ;)")
    

    print (f'Your password score is:',stregnth,'/5')

def check_pwd2(another_pwd=False):
    valid = False
    if another_pwd:
        choice = input("Do you want to check another password? (y/n)")
        if choice == "y":
            return True
        elif choice == "n":
            print("Exiting......")
            return False
        else:
            print("Invalid Input")
        
if __name__ == '__main__':
    print("===== Welcome to the Password Stregnth Checker =====")        
    check_pwd = check_pwd2
    while check_pwd:
        password_stregnth_checker()
        check_pw = check_pwd(True)

**- `quiz_game.py/`**
   - `quiz_game.py`:
    print("Welcome to my quiz!!")

play = input("Do you wanna play? ")

if play.lower()!= "yes":
    quit()
else:
    print("Okay! let's play :)")
score=0
answer1 = input("What does the acronym SQL stand for? ")
if answer1.lower() == "structured query language":
    print('Correct!!')
    score+=1
else:
    print("Incorrect :(")

answer2 = input("What is the term for a network security system that monitors and controls incoming and outgoing network traffic? ")
if answer2.lower() == "firewall":
    print('Correct!!')
    score+=1
else:
    print("Incorrect :(")

answer3 = input("What does HTML stand for? ")
if answer3.lower() == "hypertext markup language":
    print('Correct!!')
    score+=1
else:
    print("Incorrect :(")

answer4 = input("What does RAM atands for? ")
if answer4.lower() == "random access memory":
    print('Correct!!')
    score+=1
else:
    print("Incorrect :(")

answer5 = input("What does PSU stands for? ")
if answer5.lower() == "power supply":
    print('Correct!!')
    score+=1
else:
    print("Incorrect :(")

answer6 = input("Which programming language is known for its use of indentation to define code blocks? ")
if answer6.lower() == "python":
    print('Correct!!')
    score+=1
else:
    print("Incorrect :(")

answer7 = input(" Which company developed the Windows operating system? ")
if answer7.lower() == "microsoft":
    print('Correct!!')
    score+=1
else:
    print("Incorrect :(")

answer8 = input("What does HTTP stand for?")
if answer8.lower() == "hypertext transfer protocol":
    print('Correct!!')
    score+=1
else:
    print("Incorrect :(")

answer9 = input(" What is the name of the global system of interconnected computer networks? ")
if answer9.lower() == "internet":
    print('Correct!!')
    score+=1
else:
    print("Incorrect :(")

answer10 = input("What does CPU stand for? ")
if answer10.lower() == "central processing unit":
    print('Correct!!')
    score+=1
else:
    print("Incorrect :(")

print("You got " + str(score) + " questions correct!!")

**- `rock_paper_sissor.py/`**
   - `rock_paper_sissor.py`:
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

**- `story.txt/`**
   - `story.txt`:
    
Today, my best friend and I went to the zoo.
We saw a(n) <adjective> <animal> jumping up and down in its tree. 
He <verb (past tense)> <adverb> through the large tunnel that led to its <adjective> <habitat>.
I was so <emotion> because I’ve never seen anything like it before.
The zookeeper told us that its favorite food is <food>, but I didn’t have any <food> with me.
I gave it a(n) <noun> to eat instead.
Next, we went to the petting zoo where we saw a(n) <adjective> <animal>. 
It looked like it needed <noun>. I had fun <verb ending in -ing> with it. 
We decided to buy some <plural noun> and head to our favorite part of the zoo. 
The highlight of the day was when a <adjective> <animal> <verb (past tense)> right in front of us!

**- `tic_tac_toe.py/`**
   - `tic_toe_toe.py`:
    
import random

class TicTacToe:
    
    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)
    
    def get_random_first_player(self):
        return random.randint(0,1)
    
    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def has_player_won(self, player):
        n = len(self.board)
        board_values = set()

        # Check rows
        for i in range(n):
            for j in range(n):
                board_values.add(self.board[i][j])
            if board_values == {player}:
                return True
            else:
                board_values.clear()
        
        # Check columns
        for i in range(n):
            for j in range(n):
                board_values.add(self.board[i][j])
            if board_values == {player}:
                return True
            else:
                board_values.clear()
            
            board_values.add(self.board[0][2])
            board_values.add(self.board[1][1])
            board_values.add(self.board[2][0])
            if board_values == {player}:
                return True
            else:
                return False
            
    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True
    
    def swap_player_turn(self,player):
        return 'X' if player == 'O' else 'O'
    
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=' ')
            print()
    
    def start(self):
        self.create_board()
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            try:
                self.show_board()
                print(f'\nPlayer {player} turn')

                row, col = list( map(int, input('Enter row & column numbers to fix spot: ').split()))
                print()
                if col is None:
                    raise ValueError('not enough values to unpack (expected 2, got 1)')
                self.fix_spot(row -1, col -1, player)
                game_over = self.has_player_won(player)
                if game_over:
                    print('fPlayer {player} wins the game!')
                    continue

                game_over = self.is_board_filled()
                if game_over:
                    print('Match Draw! ')
                    continue

                player = self.swap_player_turn(player)
            
            except ValueError as err:
                print(err)

        print()
        self.show_board()

if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()

    
**- `time_math_challange.py/`**
   - `time_math_challange.py`:
    import random
import time
operators = ["+","-","*"]
min_opr = 3
max_opr = 12
total_problems = 10

def generate_problem():
    left = random.randint(min_opr,max_opr)
    right = random.randint(min_opr,max_opr)
    operator = random.choice(operators)

    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression)
    print(expression)
    return expression, answer

expression, answer = generate_problem()
print(expression, answer)

wrong = 0 
input("Press enter to start")
print("--------------------")

start_time = time.time()
for i in range(total_problems):
    expression, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i +1) + ": " + expression + "=")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time
print("----------------------")
print("Nice Work! You finished in", total_time, "Seconds!")

    
Feel free to explore the folders and try out the programs!

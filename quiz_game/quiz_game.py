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

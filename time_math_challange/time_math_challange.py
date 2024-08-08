
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

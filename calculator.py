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
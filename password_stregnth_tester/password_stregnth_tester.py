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

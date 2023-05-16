from account import Account
import os
import time

def clear_screen(your_time):
    time.sleep(your_time)
    os.system("cls")
    time.sleep(your_time)

def login(email, original_password):
    print(Account.data_base)
    #for key, value in Account.data_base.items():

def sign_up():
    pass

def login_board():
    email = input("Enter Your Email: ")
    password = input("Enter Your Password: ")
    login(email, password)

def register_board():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    pass1 = input("Enter Password: ")
    pass2 = input("Confirm Password: ")
    phone = input("Enter Phone Number: ")
    user = Account(first_name, last_name, email, age, gender, pass1, pass2, phone)
    user.create_account()

def menu():
    print("""
    1) Login
    2) Create Account

    Press and Enter Any Value .....
    """)

    try:
        user_input = int(input('Enter Number: '))
        if user_input == 1:
            login_board()
        elif user_input == 2:
            register_board()
        else:
            print("Shey you are blind ni?")
            exit()
    except Exception as e: 
        print(f"Wrong Input!, {e}")
        menu()

if __name__=='__main__': 
    print("Welcome To Major Bank")
    menu()



            
import query_handler
from menus import *
from store import store
from connect import *
from validation.signup_validation import valid_user
from validation.login_validation import valid_entry
from query_handler import *

store = store()
db = get_db()
cursor = db.cursor()
store.db = db
store.cursor = cursor

def user_dash_board():
    print("success")
    pass


def signup():
    username = input('please enter a username:\n>')
    password = input('choose a password:\n>')
    first_name = input('enter your firstname:\n>')
    last_name = input('enter your lastname:\n>')
    phone_number = input('enter your phone number:\n>')
    email = input('enter your email:\n>')
    security_question_answer = input('what is your favorite color? (as the security question)\n>')

    user = {
        "username": username,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "email": email,
        "security_question_answer": security_question_answer.lower()
    }

    user_validity = valid_user(user, cursor)
    if user_validity:
        query_handler.sign_up(user)
        user_dash_board()
    else:
        print(user_validity)
        print(store.signup_error_message)

        signup()

    pass


def login():
    username = input('please enter your username: ')
    password = input('please enter your password: ')
    user = {
        "username": username,
        "password": password
    }
    user_validity = valid_entry(user, cursor)
    if user_validity:
        query_handler.log_in(user)
        user_dash_board()
    else:
        print(user_validity)
        print(store.login_error_message)

        login()


if __name__ == "__main__":
    welcome_text()
    while True:
        enter_menu()
        user_choice = input()
        if user_choice == '1':
            signup()
        elif user_choice == '2':
            login()
        elif user_choice == '3':
            break
        else:
            print("you may have entered some wrong values")

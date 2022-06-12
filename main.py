import menus
from menus import *
from store import store
from connect import *
from validation.signup_validation import valid_user
from validation.login_validation import valid_entry
from validation.index_validation import index_is_valid
from query_handler.sign_up import sign_up
from query_handler.log_in import log_in
from query_handler.log_out import log_out
from query_handler.logged_in_user import *
from query_handler.search import search
from cli_assets.cli_colors import CliColors
from query_handler.friend_request_utils import *

store = store()
db = get_db()
cursor = db.cursor()
store.db = db
store.cursor = cursor


def user_dash_board(user):
    while True:
        print('\n\n' + CliColors.WARNING + '______' + '{}'.format(user["username"]) + '______' + CliColors.ENDC)
        print(CliColors.OKGREEN + '****' + 'Dash Board' + '****' + CliColors.ENDC)
        menus.dash_board_menu()
        user_input = input("choose an option\n>").rstrip()
        if user_input == '1':
            pass
        elif user_input == '2':
            pass
        elif user_input == '3':
            search_handler(user)
            pass
        elif user_input == '4':
            requests(user)
        elif user_input == '5':
            pass
        elif user_input == '6':
            log_out(user)
            break
        elif user_input == '7':
            pass
        else:
            print("you may have entered a wrong value")


def search_handler(user):
    user_search_str = input("enter the username to be searched\n>")
    result_array = search(user_search_str)
    print_search_result(result_array, user)
    friend_request_handler(result_array, user)


def print_search_result(result_array, user):
    if len(result_array) == 0:
        print("no such user found")
        return
    print("search results:")
    for i, t in enumerate(result_array):
        if t[0] == user["username"]:
            print(CliColors.WARNING + '' + '{i} ) {id} (YOU)'.format(i=i + 1, id=t[0]) + CliColors.ENDC)
        else:
            print('{i} ) {id}'.format(i=i + 1, id=t[0]))


def friend_request_handler(result_array, user):
    friend_req_target = input('which one do you wish to send a friend_request to?\n>')

    # if not friend_req_target.isdigit():
    #     print(CliColors.FAIL + 'please enter a number' + CliColors.ENDC)
    #     friend_request_handler(result_array, user)
    #
    # friend_req_target = int(friend_req_target)
    # friend_req_target = friend_req_target - 1
    #
    # if friend_req_target < 0 or friend_req_target > len(result_array):
    #     print(CliColors.FAIL + 'index out of border....' + CliColors.ENDC)
    #     friend_request_handler(result_array, user)

    if not index_is_valid(friend_req_target, len(result_array)):
        friend_request_handler(result_array, user)
        return
    friend_req_target = int(friend_req_target)
    friend_req_target -= 1

    if result_array[friend_req_target][0] == user["username"]:
        print(CliColors.FAIL + 'You cant send a request to yourself... try again' + CliColors.ENDC)
        return

    dest_ID = result_array[friend_req_target][0]

    if is_friend(user["username"], dest_ID):
        print('You are already a friend of {}'.format(dest_ID))
        return
    if request_exists(user["username"], dest_ID):
        print('A request had already been sent to {}'.format(dest_ID))
        return
    if reverse_request(user["username"], dest_ID):
        print('A request had already been sent from {} to you. You can go and accept it'.format(dest_ID))
        return
    send_request(user["username"], dest_ID)


def requests(user):
    user_choice = input('1) sent requests\n2) received requests\n>')
    username = user["username"]
    if user_choice == '1':
        user_sent_requests(username)
    elif user_choice == '2':
        user_received_requests(username)
    else:
        print('you may have entered wrong value')


def user_sent_requests(username):
    result_array = sent_requests(username)
    print_requests(result_array)


def user_received_requests(username):
    result_array = received_requests(username)
    print_requests(result_array)
    print(""""HELP NOTE:\n
    you can accept a  request using keyword `acc` along with the index you want to accept\n
    reject a request using keyword `rej`along with the index you want to reject\n
    or close the section using keyword `ext`""")
    user_input = input('enter your choice (dont forget to use spaces ;))')
    input_splited = user_input.split(' ')
    command = input_splited[0]
    if command == 'acc':
        update_request_situation(username, input_splited[1], result_array, RequestLevels.ACCEPTED)
    elif command == 'rej':
        update_request_situation(username, input_splited[1], result_array, RequestLevels.REJECTED)
    elif command == 'ext':
        return
    else:
        print('you may have entered wrong entry')
        return


def update_request_situation(username, index, result, sit):
    if not index_is_valid(index, len(result)):
        user_received_requests(username)
        return
    index -= 1
    request_sender_ID = result[index][0]
    update_request(request_sender_ID, username, sit)



def print_requests(result_array):
    if len(result_array) == 0:
        print('no request found!...')
        return
    print(CliColors.OKBLUE + '   User_ID\t\tSituation' + CliColors.ENDC)
    for ind, row in enumerate(result_array):
        print('{}) {}\t\t{}'.format(ind + 1, row[0], row[1]))


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
        sign_up(user)
        user_dash_board(user)
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
        log_in(user)
        user_dash_board(user)
    else:
        print(user_validity)
        print(store.login_error_message)

        login()


if __name__ == "__main__":
    welcome_text()
    count, user = check_login()
    # print(count)
    if count:
        user_dash_board(user)
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

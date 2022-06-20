import menus
from menus import *
from store import store
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
from query_handler.friends_utils import *
from query_handler.blocks_utils import *
from validation.friend_req_validation import valid_friend_request
from validation.block_req_validation import valid_block_request
from query_handler.db_users import *
from query_handler.messages_utils import *

store = store()


def user_dash_board(user):
    while True:
        print('\n\n' + CliColors.WARNING + '______' + '{}'.format(user["username"]) + '______' + CliColors.ENDC)
        print(CliColors.OKGREEN + '****' + 'Dash Board' + '****' + CliColors.ENDC)
        menus.dash_board_menu()
        user_input = input("choose an option\n>").rstrip()
        if user_input == '1':
            pass
        elif user_input == '2':
            display_friends(user)
            chat_with_friend(user)
        elif user_input == '3':
            search_handler(user)
            pass
        elif user_input == '4':
            requests(user)
        elif user_input == '5':
            blocked_users(user)
        elif user_input == '6':
            log_out(user)
            break
        elif user_input == '7':
            pass
        else:
            print("you may have entered a wrong value")


def chat_with_friend(user):
    # display_friends(user)
    friends = get_friends(user["username"])
    if len(friends) == 0:
        return
    menus.start_chat_help_menu()
    user_choice = input('enter your choice\n>')
    data_list = user_choice.split(' ')
    cmd = data_list[0]
    if not cmd == 'chat':
        return
    if not len(data_list) > 1:
        return
    if index_is_valid(data_list[1], len(friends)):
        chat_contact = friends[int(data_list[1]) - 1][0]
        chatroom(user["username"], chat_contact)


def chatroom(src, dst):
    menus.chat_help_menu()
    while True:
        display_messages(src, dst)
        if message_prompt(src, dst) == 0:
            return


def display_messages(src, dst):
    src = get_user(src)
    dst = get_user(dst)
    messages = get_messages(src, dst)
    if len(messages) == 0:
        print('No messages found')
        return
    for index, message in enumerate(messages):
        user_is_sender = message[3] == src["username"]
        print('*' * 32)
        print('{})'.format(index))
        if user_is_sender:
            print(CliColors.OKGREEN + 'YOU: ' + CliColors.ENDC, end='')
        else:
            print(message[3] + ': ', end='')
        print(message[5])
        if user_is_sender:
            end = '\t'
        else:
            end = '\n'
        print('\n{}'.format(message[6]), end=end)
        if user_is_sender:
            if message[7] == 0:
                print('not seen')
            else:
                print('seen')
        print('*' * 32)


def get_messages(src, dst):
    chat_messages = get_chat(src, dst)
    return chat_messages


def message_prompt(src, dst):
    src = get_user(src)
    dst = get_user(dst)
    chat_input = input('{}: '.format(src["username"]))
    chat_data = chat_input.split(' ')
    command = chat_data[0]
    print(command)
    if command != 'msg' and command != 'like':
        return 0
    if not len(chat_data) > 1:
        print('not enough entries')
        return 0
    if command == 'like':
        """TODO: get index, validate it, add to liked messages"""
        pass
    if command == 'msg':
        if len(chat_data[1]) > 300:
            print('message content should not be over 300 characters')
            return 0
        msg_content = ' '.join([str(item) for item in chat_data[1:]])
        send_message(src, dst, msg_content)

def blocked_users(user):
    username = user["username"]
    blocks = get_blocked_users(username)
    if len(blocks) == 0:
        print('YOU have no blocked user')
        return
    print('    ID\t\t Blocked_Date')
    for ind, row in enumerate(blocks):
        print('{}) {}\t{}'.format(ind + 1, row[0], row[1]))


def display_friends(user):
    username = user["username"]
    friends = get_friends(username)
    if len(friends) == 0:
        print('YOU have no friends You are alone Get a life loser...')
    for ind, row in enumerate(friends):
        print('{}) {}'.format(ind + 1, row[0]))


def search_handler(user):
    user_search_str = input("enter the username to be searched\n>")
    result_array = search(user_search_str)
    print_search_result(result_array, user)
    menus.search_help_menu()
    user_input = input('enter your choice here:\n>')
    data_list = user_input.split(' ')
    cmd = data_list[0]
    if cmd == 'frnd':
        friend_request_handler(result_array, user, data_list[1])
    elif cmd == 'blck':
        block_user_handler(result_array, user, data_list[1])
    else:
        return


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


def block_user_handler(result_array, user, index):
    if not index_is_valid(index, len(result_array)):
        block_user_handler(result_array, user, index)
        return
    index = int(index) - 1

    block_target = result_array[index][0]

    if valid_block_request(result_array, user, index):
        block_user(user["username"], block_target)


def friend_request_handler(result_array, user, friend_req_target):
    if not index_is_valid(friend_req_target, len(result_array)):
        friend_request_handler(result_array, user, friend_req_target)
        return
    friend_req_target = int(friend_req_target)
    friend_req_target -= 1

    dest_ID = result_array[friend_req_target][0]
    if valid_friend_request(result_array, user, friend_req_target):
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
    menus.request_help_menu()
    user_input = input('enter your choice (dont forget to use spaces ;))\n>')
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
    index = int(index)
    index -= 1
    if not result[index][1] == RequestLevels.PENDING:
        print("you already have decided about this request and can't change it")
        return
    request_sender_ID = result[index][0]

    update_request(request_sender_ID, username, sit)

    if sit == RequestLevels.ACCEPTED:
        add_friends(username, request_sender_ID)


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

    user_validity = valid_user(user)
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

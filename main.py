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
from query_handler.like_handler import *
from chat_commands import ChatCommands
from validation import send_message_validation
from query_handler.delete_account_utils import *
from query_handler.user_limitation_utils import *
from query_handler.password_retreival_failure import *

store = store()


def user_dash_board(user):
    while True:
        print('\n\n' + CliColors.WARNING + '______' + '{}'.format(user["username"]) + '______' + CliColors.ENDC)
        print(CliColors.OKGREEN + '****' + 'Dash Board' + '****' + CliColors.ENDC)
        menus.dash_board_menu()
        user_input = input("choose an option\n>").rstrip()
        if user_input == '1':
            chats_handler(user)
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
            delete_account_ability(user)
        else:
            print("you may have entered a wrong value")


def delete_account_ability(user):
    last_chance = input('Are you really sure to delete your account?\n1) Yes\n2)NO\n>')
    if not int(last_chance) == 1:
        return
    remove_user(user["username"])


def chats_handler(user):
    chat_list = show_chat_list(user)
    print(chat_list)
    user_input = input(
        CliColors.OKGREEN + 'To enter a chatroom enter the selected of index\nTo close enter anything else\n>' + CliColors.ENDC)
    if not index_is_valid(user_input, len(chat_list)):
        return
    chatroom(get_user(user["username"]), get_user_by_token(chat_list[int(user_input) - 1][1]))


def show_chat_list(user):
    chat_list = get_contacts(user)
    if len(chat_list) == 0:
        print('no chats found...')
        return
    for index, contact_user in enumerate(chat_list):
        if contact_user[0] is None:
            print('{ind}) Deleted Account'.format(ind=index + 1))
        else:
            print('{ind}) {user}'.format(ind=index + 1, user=contact_user[0]))

    return chat_list


def chat_with_friend(user):
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
        src = get_user(user["username"])
        dst = get_user(chat_contact)
        chatroom(src, dst)


def chatroom(src, dst):
    menus.chat_help_menu()
    while True:
        make_seen(src, dst)
        messages = display_messages(src, dst)
        command = message_prompt(src, messages)
        if command["command"] == ChatCommands.CLOSE:
            return
        elif command["command"] == ChatCommands.LIKE:
            like_message(src["username"], command["message"])
        elif command["command"] == ChatCommands.SEND:
            if send_message_validation.message_is_valid(src, dst, command["message"]):
                send_message(src, dst, command["message"])


def make_seen(src, dst):
    make_seen_message(src, dst)


def display_messages(src, dst):
    messages = get_messages(src, dst)
    if len(messages) == 0:
        print('No messages found')
        return
    for index, message in enumerate(messages):
        user_is_sender = message[3] == src["username"]
        print(CliColors.WARNING + '*' * 32 + CliColors.ENDC)
        print('{})'.format(index + 1))
        if user_is_sender:
            print(CliColors.OKGREEN + 'YOU: ' + CliColors.ENDC, end='')
        else:
            if not message[3] is None:
                print(message[3] + ': ', end='')
            else:
                print('Deleted Account : ', end='')
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
        likes = get_liked_by(message[0])
        if not len(likes) == 0:
            liked_users = ','.join(str(i[0]) for i in likes)
            print('liked by: {}{}{}'.format(CliColors.FAIL, liked_users, CliColors.ENDC))
        print(CliColors.OKBLUE + '*' * 32 + CliColors.ENDC)

    return messages


def get_messages(src, dst):
    chat_messages = get_chat(src, dst)
    return chat_messages


def message_prompt(src, messages):
    chat_input = input('{}: '.format(src["username"]))
    chat_data = chat_input.split(' ')
    command = chat_data[0]
    if command != 'msg' and command != 'like':
        return {"command": ChatCommands.CLOSE}
    if not len(chat_data) > 1:
        print('not enough entries')
        return {"command": ChatCommands.CLOSE}
    if command == 'like':
        """TODO: get index, validate it, add to liked messages"""
        if not index_is_valid(chat_data[1], len(messages)):
            return {"command": ChatCommands.CLOSE}
        liked_index = int(chat_data[1]) - 1
        liked_message = messages[liked_index][0]
        return {"command": ChatCommands.LIKE,
                "message": liked_message
                }

    if command == 'msg':
        msg_content = ' '.join([str(item) for item in chat_data[1:]])
        return {"command": ChatCommands.SEND,
                "message": msg_content
                }


def display_blocked_users(user):
    username = user["username"]
    blocks = get_blocked_users(username)
    if len(blocks) == 0:
        print('YOU have no blocked user')
        return blocks
    print('    ID\t\t Blocked_Date')
    for ind, row in enumerate(blocks):
        print('{}) {}\t{}'.format(ind + 1, row[0], row[1]))

    return blocks


def blocked_users(user):
    blocks = display_blocked_users(user)
    if len(blocks) == 0:
        return
    user_inp = input(
        CliColors.OKGREEN + 'If you wish to unblock any user enter the index of the user\nOtherwise enter anything but an index\n>' + CliColors.ENDC)
    if index_is_valid(user_inp, len(blocks)):
        index_to_remove = int(user_inp) - 1
        remove_blocked(user["username"], blocks[index_to_remove][0])


def display_friends(user):
    print(CliColors.FAIL + 'Friends' + CliColors.ENDC)
    username = user["username"]
    friends = get_friends(username)
    if len(friends) == 0:
        print('YOU have no friends\nYou are alone\nGet a life loser...')
    for ind, row in enumerate(friends):
        print('{}) {}'.format(ind + 1, row[0]))


def search_handler(user):
    user_search_str = input("enter the username to be searched\n>")
    result_array = search(user_search_str)
    if print_search_result(result_array, user) == 0:
        return
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
        return 0
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

    if is_login_suspend(user):
        print('You are suspended until {}'.format(get_login_suspend_time(user)))
        return

    user_validity = valid_entry(user)
    if user_validity["validity"]:
        log_in(user)
        user_dash_board(user)

    else:
        print(user_validity["message"])
        if user_validity["error"] == 'WrongPass':
            wrong_password_handler(user)

        login()


def wrong_password_handler(user):
    insert_false_try(user)


def forget_password_handler():
    user_username = input('please enter your your username\n>')
    user = {"username": user_username}
    if is_pass_ret_suspend(user):
        print('You are suspended to retrieve and change password until {}'.format(get_pass_ret_suspend_time(user)))
        return
    if not user_exists(user_username):
        print('This user doesnt even exist in app database')
        return
    user_fav_color = get_fav_color(user_username)
    fav_color = input('What is your favorite color?\n>')
    if fav_color.lower() == user_fav_color:
        new_pass = input('Please enter new password\n>')
        change_password(user_username, new_pass)
    else:
        print(CliColors.FAIL+'Incorrect Try again'+CliColors.ENDC)
        insert_false_color(user)
        return


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
            forget_password_handler()
        elif user_choice == '4':
            break
        else:
            print("you may have entered some wrong values")

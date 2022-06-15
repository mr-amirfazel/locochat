from cli_assets.cli_colors import CliColors
from query_handler.blocks_utils import *
from query_handler.friend_request_utils import *


def valid_friend_request(result_array, user, friend_req_target):
    if result_array[friend_req_target][0] == user["username"]:
        print(CliColors.FAIL + 'You cant send a request to yourself... try again' + CliColors.ENDC)
        return False

    dest_ID = result_array[friend_req_target][0]
    if has_blocked(user["username"], dest_ID):
        print('you have blocked {} you have to unblock this user first'.format(dest_ID))
        return False
    if has_blocked(dest_ID, user["username"]):
        print('Since you have been blocked by {}, you cant send a friendship request to this user'.format(dest_ID))
        return False
    if is_friend(user["username"], dest_ID):
        print('You are already a friend of {}'.format(dest_ID))
        return False
    if request_exists(user["username"], dest_ID):
        print('A request had already been sent to {}'.format(dest_ID))
        return False
    if reverse_request(user["username"], dest_ID):
        print('A request had already been sent from {} to you. You can go and accept it'.format(dest_ID))
        return False
    return True

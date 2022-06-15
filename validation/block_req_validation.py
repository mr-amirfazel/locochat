from cli_assets.cli_colors import CliColors
from query_handler.blocks_utils import has_blocked
from query_handler.friend_request_utils import is_friend
from query_handler.friends_utils import *


def valid_block_request(result_array, user, index):
    if result_array[index][0] == user["username"]:
        print(CliColors.FAIL + 'You cant block yourself... try again' + CliColors.ENDC)
        return False

    block_target = result_array[index][0]

    """This checks if user had locked the target in the past or not"""
    if has_blocked(user["username"], block_target):
        print('you already have blocked user with username: {}'.format(block_target))
        return False

    if is_friend(user["username"], block_target):
        remove_friends(user["username"], block_target)

    return True

from cli_assets.cli_colors import CliColors
from query_handler.blocks_utils import has_blocked
from query_handler.friend_request_utils import is_friend


def message_is_valid(src, dst, message_content):
    if has_blocked(src["username"], dst["username"]):
        print(CliColors.FAIL + 'you have blocked this user, you cant send message ' + CliColors.ENDC)
        return False
    if has_blocked(dst["username"], src["username"]):
        print(CliColors.FAIL + 'this user has blocked you, you cant send message to this user' + CliColors.ENDC)
        return False
    if not is_friend(src["username"], dst["username"]):
        print(
            CliColors.FAIL + 'You are not a friend of {} anymore. try sending a new friend request to this user'.format(
                dst["username"] + CliColors.ENDC))
        return False
    if len(message_content.rstrip()) == 0:
        print(CliColors.FAIL+'You cant enter empty string'+CliColors.ENDC)
        return False
    if len(message_content) > 300:
        print('message content should not be over 300 characters')
        return False
    return True

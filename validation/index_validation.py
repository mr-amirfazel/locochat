from cli_assets.cli_colors import CliColors


def index_is_valid(index, length):
    return index_is_digit(index) and index_in_border(index, length)


def index_is_digit(index):
    if not index.isdigit():
        print('index is not even a digit')
    return index.isdigit()


def index_in_border(index, length):
    index = int(index)
    index -= 1

    if index < 0 or index >= length:
        print(CliColors.FAIL + 'index out of border....' + CliColors.ENDC)
        return False
    return True



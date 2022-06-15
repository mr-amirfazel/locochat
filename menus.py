from cli_assets.cli_colors import CliColors

welcome = "cli_assets/welcome.txt"
enter = "cli_assets/enterMenu.txt"
dash_board = "cli_assets/dash_board.txt"
search_help = "cli_assets/search_help_menu.txt"
request_help = "cli_assets/request_help_menu.txt"


def printer(file_name, color=''):
    with open(file_name) as file:
        for line in file:
            print(color+line.rstrip()+CliColors.ENDC)


def welcome_text():
    printer(welcome, CliColors.FAIL)


def enter_menu():
    printer(enter)


def dash_board_menu():
    printer(dash_board)


def search_help_menu():
    printer(search_help, CliColors.OKGREEN)


def request_help_menu():
    printer(request_help, CliColors.OKGREEN)

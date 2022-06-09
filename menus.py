welcome = "cli_assets/welcome.txt"
enter = "cli_assets/enterMenu.txt"
dash_board = "cli_assets/dash_board.txt"


def printer(file_name):
    with open(file_name) as file:
        for line in file:
            print(line.rstrip())


def welcome_text():
    printer(welcome)


def enter_menu():
    printer(enter)


def dash_board_menu():
    printer(dash_board)

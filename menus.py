welcome = "cli_assets/welcome.txt"
enter = "cli_assets/enterMenu.txt"


def printer(file_name):
    with open(file_name) as file:
        for line in file:
            print(line.rstrip())


def welcome_text():
    printer(welcome)

def enter_menu():
    printer(enter)
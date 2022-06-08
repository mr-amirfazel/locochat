from store import store

store = store()


def valid_user(user, cursor):
    store.signup_error_message = ''
    name_is_valid = valid_name(user)
    ID_is_valid = valid_ID(user, cursor)
    mail_is_valid = valid_mail(user, cursor)
    phone_is_valid = valid_phone_number(user, cursor)
    password_is_valid = valid_password(user)
    answer_is_valid = valid_question_answer(user)
    print(name_is_valid, ID_is_valid, mail_is_valid, phone_is_valid, password_is_valid, answer_is_valid)

    return name_is_valid and mail_is_valid and ID_is_valid and phone_is_valid and password_is_valid and answer_is_valid


def valid_name(user):
    first_name = user["first_name"]
    last_name = user["last_name"]
    print("valid name")
    if first_name.rstrip() == '' or last_name.rstrip() == '':
        store.signup_error_message = store.signup_error_message + "name or lastname Shouldn't be empty\n"
        return False
    return True


def valid_password(user):
    print("valid pass")
    password = user["password"]
    if password.rstrip() == '':
        store.signup_error_message = store.signup_error_message + "password Shouldn't be empty\n"
        return False
    if password.isdigit():
        print(password.isdigit())
        store.signup_error_message = store.signup_error_message + 'Password should have at least one alphabetical\n'
        return False
    if not any(char.isdigit() for char in password):
        store.signup_error_message = store.signup_error_message + 'Password should have at least one numeral\n'
        return False

    return True


def valid_phone_number(user, cursor):
    print("valid phone")
    return valid_phone_digit(user) and valid_phone_len(user) and not phone_number_exists(user, cursor)


def valid_phone_len(user):
    if len(user['phone_number']) == 11:
        return True
    store.signup_error_message = store.signup_error_message + "phone number must  contain 11 digits\n"
    return False


def valid_phone_digit(user):
    if user['phone_number'].isdigit():
        return True
    store.signup_error_message = store.signup_error_message + "phone number must only contain digits\n"
    return False


def phone_number_exists(user, cursor):
    number = user['phone_number']
    query = """
    select phone_number
    from users
    where phone_number = {phone_number}
    """.format(phone_number=number)
    cursor.execute(query)
    if cursor.rowcount != 0:
        store.signup_error_message = store.signup_error_message + 'there is an account with this phone number\n'
        return True
    return False


def valid_mail(user, cursor):
    print("valid mail")
    print("mail exists: ", email_exists(user, cursor))
    return valid_email_combination(user) and not email_exists(user, cursor)


def valid_email_combination(user):
    if '@' in user['email']:
        return True
    store.signup_error_message = store.signup_error_message + "email must contain @\n"
    return False


def email_exists(user, cursor):
    email = user['email']
    query = """
    select email
    from users
    """

    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        if email in row:
            return True
    return False


def valid_ID(user, cursor):
    print("valid id")
    print("ID exists ", user_exists(user, cursor))
    return valid_ID_combination(user) and not user_exists(user, cursor)


def valid_ID_combination(user):
    user_ID = user['username']
    if user_ID.rstrip() == '':
        store.signup_error_message = store.signup_error_message + "username Shouldn't be empty\n"
        return False
    if not any(char.isdigit() for char in user_ID):
        store.signup_error_message = store.signup_error_message + 'username should have at least one numeral\n'
        return False
    return True


def user_exists(user, cursor):
    username = user['username']
    username = str(username)
    query = """
    select userID
    from users
    """
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        if username in row:
            return True
    return False


def valid_question_answer(user):
    if user["security_question_answer"].rstrip() == '':
        store.signup_error_message = store.signup_error_message + 'answer to security question should not be EMPTY! \n'
        return False
    return True

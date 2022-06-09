from store import store
import hashlib

store = store()


def valid_entry(user, cursor):
    store.login_error_message = ''
    return user_existence(user, cursor) and password_match(user, cursor)


def user_existence(user, cursor):
    if user_exists(user, cursor):
        return True
    else:
        store.login_error_message = store.login_error_message + 'User does not exist in database\n'
        return False


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


def password_match(user, cursor):
    username = user['username']
    password = user['password']

    sql = """
    select userID, password_hashed
    from users 
    """
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        if row[0] == username and row[1] == hashlib.sha256(password.encode('utf-8')).hexdigest():
            return True
    store.login_error_message = store.login_error_message + 'password doesnt match'
    return False

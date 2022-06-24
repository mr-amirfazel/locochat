from store import store
import hashlib
from connect import *

db = get_db()
cursor = db.cursor()

store = store()


def valid_entry(user):
    store.login_error_message = ''
    return user_existence(user) and password_match(user)


def user_existence(user):
    if user_exists(user):
        return True
    else:
        store.login_error_message = store.login_error_message + 'User does not exist in database\n'
        return False


def user_exists(user):
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


def password_match(user):
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

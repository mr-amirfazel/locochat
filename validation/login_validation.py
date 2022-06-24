from store import store
import hashlib
from connect import *

db = get_db()
cursor = db.cursor()

store = store()


def valid_entry(user):
    if not user_existence(user):
        return {
            "validity": False,
            "error": 'UserNotExist',
            "message": 'this username does not exist in database'
        }
    if not password_match(user):
        return {
            "validity": False,
            "error": 'WrongPass',
            "message": 'password is incorrect'
        }
    return {"validity": True}


def user_existence(user):
    if user_exists(user):
        return True
    else:
        return False


def user_exists(user):
    username = user['username']
    username = str(username)
    query = """
    select userID
    from users
    """
    result = []
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        db.commit()
    except Exception as inst:
        print(inst)
        db.rollback()

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
    result = []
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        db.commit()

    except Exception as inst:
        print(inst)
        db.rollback()

    for row in result:
        if row[0] == username and row[1] == hashlib.sha256(password.encode('utf-8')).hexdigest():
            return True
    return False

import secrets
from hashlib import sha256
from connect import *
import time
import datetime

db = get_db()
cursor = db.cursor()


# from store import store

# store = store()
# db = store.db
# cursor = store.cursor


def sign_up(user):
    token = secrets.token_hex(25)
    sql = """
            insert into `users`
            (token, userID, first_name, last_name, phone_number, email, password_hashed, security_question_answer)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s)
            """
    val = (token, user['username'], user["first_name"], user["last_name"], user["phone_number"], user["email"],
           sha256(user["password"].encode('utf-8')).hexdigest(), user["security_question_answer"])

    try:
        cursor.execute(sql, val)
        db.commit()
        print("added to db")

    except Exception as inst:
        print("not added")
        print(inst)
        db.rollback()

    log_in(user)


def log_in(user):
    ts = time.time()
    login_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    login_id = user["username"] + login_date
    sql = """
    insert into `logins`
    (login_ID, entered_user_ID, login_date, logout_date, login_situation)
    VALUES
    (%s, %s, %s, %s, %s)
    """
    val = (login_id, user["username"], login_date, None, True)

    try:
        cursor.execute(sql, val)
        db.commit()
        print("added to logins")

    except Exception as inst:
        print("not added to logins")
        print(inst)
        db.rollback()



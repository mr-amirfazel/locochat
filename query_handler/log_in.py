import secrets
from hashlib import sha256
from connect import *
import time
import datetime

db = get_db()
cursor = db.cursor()


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

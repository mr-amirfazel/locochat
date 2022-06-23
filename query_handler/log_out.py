from connect import *
import time
import datetime
from logger import log
from table_titles import TableTitles

db = get_db()
cursor = db.cursor()


def log_out(user):
    ts = time.time()
    log_out_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    sql = """
    UPDATE logins 
    SET login_situation = %s, logout_date = %s 
    WHERE entered_user_ID = %s
    """
    val = ("0", log_out_date, user["username"])

    try:
        cursor.execute(sql, val)
        db.commit()
        print("logged out")

    except Exception as inst:
        print("error in logging out")
        print(inst)
        db.rollback()

    log(TableTitles.LOGINS, 'user: {} logged out of the app'.format(user))


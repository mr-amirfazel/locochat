from connect import *
from query_handler.logger import log
from query_handler.table_titles import TableTitles as t
import time
import datetime

db = get_db()
cursor = db.cursor()


def init_false_try_login(user):

    sql = """
    insert into  `login_failure`
    (ID)
    values
    (%s)
    """
    val = (user['username'], )

    try:
        cursor.execute(sql, val)
        db.commit()

    except Exception as inst:
        print(inst)
        db.rollback()


def insert_false_try(user):
    fail_count = get_number_of_false_entries(user)
    if fail_count < 4:
        sql = """
        update `login_failure`
        set failure_count = %s
        where ID = %s
        """
        val = (fail_count + 1, user["username"])
        execute_query(sql, val)
        log(t.LOGIN_FAIL, '{} entered wrong password'.format(user["username"]))
    elif fail_count == 4:
        ts = time.time()
        sus_begin = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        ftr = datetime.datetime.fromtimestamp(ts) + datetime.timedelta(days=5)
        sus_end = ftr.strftime('%Y-%m-%d %H:%M:%S')
        sql = """
                update `login_failure`
                set failure_count = %s, suspend_begin= %s, suspend_end=%s
                where ID = %s
                """
        val = (fail_count + 1, sus_begin, sus_end, user["username"])
        execute_query(sql, val)
        log(t.LOGIN_FAIL, '{} entered wrong password and got suspended untill {}'.format(user["username"], sus_end))
    elif fail_count == 5:
        sql = """
                        update `login_failure`
                        set failure_count = %s, suspend_begin= %s, suspend_end=%s
                        where ID = %s
                        """
        val = (1, None, None, user["username"])
        execute_query(sql, val)
        log(t.LOGIN_FAIL, '{} entered wrong password'.format(user["username"]))


def execute_query(sql, val):
    try:
        cursor.execute(sql, val)
        db.commit()

    except Exception as inst:
        print(inst)
        db.rollback()


def get_number_of_false_entries(user):
    sql = """
    select failure_count
    from `login_failure`
    where ID = %s
    """
    val = (user["username"],)

    try:
        cursor.execute(sql, val)
        res = cursor.fetchall()
        db.commit()
        return int(res[0][0])

    except Exception as inst:
        print(inst)
        db.rollback()


def is_login_suspend(user):
    ts = time.time()
    now = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    sql = """
    select failure_count, suspend_end
    from `login_failure`
    where ID = %s
    """
    val = (user["username"], )

    try:
        cursor.execute(sql, val)
        res = cursor.fetchall()
        db.commit()

        return int(res[0][0]) == 5 and now < str(res[0][1])

    except Exception as inst:
        print(inst)
        db.rollback()


def get_login_suspend_time(user):
    sql = """
    select suspend_end
    from `login_failure`
    where ID = %s
    """
    val = (user["username"], )

    try:
        cursor.execute(sql, val)
        res = cursor.fetchall()
        db.commit()
        return res[0][0]

    except Exception as inst:
        print(inst)
        db.rollback()

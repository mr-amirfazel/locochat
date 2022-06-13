from connect import *
import time
import datetime


db = get_db()
cursor = db.cursor()


def has_blocked(src, dst):
    sql = """
    select count(blocker_ID)
    from `blocked`
    where blocker_ID = %s and blocked_ID = %s
    """

    val = (src, dst)
    try:
        cursor.execute(sql, val)
        res = cursor.fetchall()[0][0]
        db.commit()
        return res > 0

    except Exception as inst:
        print(inst)
        db.rollback()


def block_user(src, dst):
    ts = time.time()
    blocked_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    sql = """
    insert into `blocked`
        (blocker_ID, blocked_ID, blocked_at)
     values
        (%s, %s, %s)
    """

    val = (src, dst, blocked_date)
    try:
        cursor.execute(sql, val)
        db.commit()
        print('successfully blocked user.')

    except Exception as inst:
        print('2')
        print(inst)
        db.rollback()


def remove_blocked(src, dst):
    pass

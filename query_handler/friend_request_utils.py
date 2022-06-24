from query_handler.request_levels import RequestLevels
from connect import *
from query_handler.logger import log
from query_handler.table_titles import TableTitles

db = get_db()
cursor = db.cursor()


def is_friend(src, dst):
    sql = """
    select count(userID)
    from `friends`
    where userID = %s and friendID =%s
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


def request_exists(src, dst):
    sql = """
       select request_situation
       from `friendrequests`
       where sender_ID = %s and reciever_ID =%s
       """
    val = (src, dst)

    try:
        cursor.execute(sql, val)
        res = cursor.fetchall()[0][0]
        db.commit()
        if res == RequestLevels.PENDING:
            return True
        return False

    except Exception as inst:
        print(inst)
        db.rollback()


def send_request(src, dst):
    sql = """
    insert into `friendrequests`
    (sender_ID, reciever_ID, request_situation)
    VALUES
    (%s, %s, %s)
    """
    val = (src, dst, RequestLevels.PENDING)

    try:
        cursor.execute(sql, val)
        db.commit()
        print("Request was sent successfully")

    except Exception as inst:
        print(inst)
        db.rollback()

    log(TableTitles.FRIENDREQUESTS, '{} sent a friendship request to {}'.format(src, dst))


def reverse_request(src, dst):
    sql = """
           select request_situation
           from `friendrequests`
           where sender_ID = %s and reciever_ID =%s
           """
    val = (dst, src)

    try:
        cursor.execute(sql, val)
        res = cursor.fetchall()[0][0]
        db.commit()
        if res == RequestLevels.PENDING:
            return True
        return False

    except Exception as inst:
        print(inst)
        db.rollback()


def received_requests(username):
    sql = """
               select sender_ID, request_situation
               from `friendrequests`
               where  reciever_ID =%s
               """
    val = (username,)

    try:
        cursor.execute(sql, val)
        res = cursor.fetchall()
        db.commit()
        return res

    except Exception as inst:
        print(inst)
        db.rollback()

    log(TableTitles.FRIENDREQUESTS, 'User {} checked for received friendship requests'.format(username))


def sent_requests(username):
    sql = """
                   select reciever_ID, request_situation
                   from `friendrequests`
                   where  sender_ID =%s
                   """
    val = (username,)

    try:
        cursor.execute(sql, val)
        res = cursor.fetchall()
        print(res)
        db.commit()
        return res

    except Exception as inst:
        print(inst)
        db.rollback()

    log(TableTitles.FRIENDREQUESTS, 'User {} checked for send friendship requests'.format(username))


def update_request(src, dst, situation):
    sql = """
    UPDATE friendrequests 
    SET request_situation = %s 
    WHERE sender_ID = %s and reciever_ID = %s
    """
    val = (situation, src, dst)

    try:
        cursor.execute(sql, val)
        db.commit()

    except Exception as inst:
        print(inst)
        db.rollback()

    log(TableTitles.FRIENDREQUESTS, "user {} changed user {}'s request situation to {}".format(src, dst, situation))

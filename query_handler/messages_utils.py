from connect import *
import secrets
import time
import datetime

db = get_db()
cursor = db.cursor()


def get_chat(src, dst):
    src_token = src["token"]
    dst_token = dst["token"]
    sql = """
    select *
    from `messages`
    where 
    sender_token = %s and receiver_token = %s
    or 
    sender_token = %s and receiver_token = %s
    order by message_time asc
    """
    val = (src_token, dst_token, dst_token, src_token)

    try:
        cursor.execute(sql, val)
        res = cursor.fetchall()
        db.commit()
        return res

    except Exception as inst:
        print(inst)
        db.rollback()


def send_message(src, dst, message_content):
    """TODO: adds messages to the messages table in database"""
    ts = time.time()
    msg_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    msg_id = secrets.token_hex(10)
    sql = """
    insert into `messages`
    (message_ID, sender_token, receiver_token, sender_user_ID, receiver_user_ID, message_content, message_time, seen)
    values 
    (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    val = (msg_id, src["token"], dst["token"], src["username"], dst["username"], message_content, msg_date, 0)

    try:
        cursor.execute(sql, val)
        db.commit()

    except Exception as inst:
        print(inst)
        db.rollback()


def like_message(src, message_id):
    pass

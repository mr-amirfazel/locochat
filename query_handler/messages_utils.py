from connect import *

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


def send_message(src, dst):
    """TODO: adds messages to the messages table in database"""
    pass


def like_message(src, message_id):
    pass

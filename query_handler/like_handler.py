from connect import *
from query_handler.logger import log
from query_handler.table_titles import TableTitles

db = get_db()
cursor = db.cursor()


def like_message(src, message_id):
    sql = """
     insert into `likes`
    (message_ID, liker_ID)
    values 
    (%s, %s) 
    """
    val = (message_id, src)

    try:
        cursor.execute(sql, val)
        db.commit()

    except Exception as inst:
        print(inst)
        db.rollback()


    log(TableTitles.LIKES, 'user: {} liked a message with ID of {}'.format(src, message_id))

def get_liked_by(message_id):
    sql = """
    select liker_ID
    from `likes`
    where message_ID = %s
    """
    val = (message_id, )

    try:
        cursor.execute(sql, val)
        result = cursor.fetchall()
        db.commit()
        return result

    except Exception as inst:
        print(inst)
        db.rollback()



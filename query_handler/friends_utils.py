from connect import *

db = get_db()
cursor = db.cursor()


def add_friends(username, friend_ID):
    sql = """
       insert into `friends`
       (userID, friendID)
       VALUES
       (%s, %s)
       """
    val = (username, friend_ID)
    reverse_val = (friend_ID, username)

    try:
        cursor.execute(sql, val)
        cursor.execute(sql, reverse_val)
        db.commit()

    except Exception as inst:
        print(inst)
        db.rollback()


def get_friends(username):
    sql = """
    select friendID
    from `friends`
    where userID = %s
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


def remove_friends(src, dst):
    sql = """
    delete 
    from friends
    where userID =%s and friendID = %s
    """
    val = (src, dst)
    reverse_val = (dst, src)
    try:
        cursor.execute(sql, val)
        cursor.execute(sql, reverse_val)
        db.commit()

    except Exception as inst:
        print(inst)
        db.rollback()
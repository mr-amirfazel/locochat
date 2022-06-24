from connect import *
from hashlib import sha256

db = get_db()
cursor = db.cursor()


def get_user(username):
    sql = """
    select token
    from `users`
    where userID = %s
    """
    val = (username,)

    try:
        cursor.execute(sql, val)
        res = cursor.fetchall()
        user = {
            "token": res[0][0],
            "username": username
        }
        db.commit()
        return user

    except Exception as inst:
        print(inst)
        db.rollback()


def get_user_by_token(token):
    sql = """
        select userID
        from `users`
        where token = %s
        """
    val = (token,)

    try:
        cursor.execute(sql, val)
        res = cursor.fetchall()
        if len(res) == 0:
            username = None
        else:
            username = res[0][0]
        user = {
            "token": token,
            "username": username
        }
        db.commit()
        return user

    except Exception as inst:
        print(inst)
        db.rollback()


def user_exists(username):
    sql = """
    select count(userID)
    from `users`
    where userID = %s
    """
    val = (username,)

    try:
        cursor.execute(sql, val)
        res = cursor.fetchall()
        db.commit()
        return res[0][0] > 0

    except Exception as inst:
        print(inst)
        db.rollback()


def get_fav_color(username):
    sql = """
        select security_question_answer
        from `users`
        where userID = %s
        """
    val = (username,)

    try:
        cursor.execute(sql, val)
        res = cursor.fetchall()
        db.commit()
        return res[0][0]

    except Exception as inst:
        print(inst)
        db.rollback()


def change_password(username, new_pass):
    sql = """
    update `users`
    set password_hashed = %s
    where userID = %s
    """
    val = (sha256(new_pass.encode('utf-8')).hexdigest(), username)

    try:
        cursor.execute(sql, val)
        db.commit()

    except Exception as inst:
        print(inst)
        db.rollback()

from connect import *

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
        user = {
            "token": token,
            "username": res[0][0]
        }
        db.commit()
        return user

    except Exception as inst:
        print(inst)
        db.rollback()

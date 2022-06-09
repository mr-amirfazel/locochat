from connect import *

db = get_db()
cursor = db.cursor()


def check_login():
    sql = """
        select count(entered_user_ID), entered_user_ID
        from `logins`
        where login_situation = '1'
        """

    try:
        cursor.execute(sql)
        res = cursor.fetchall()
        count = res[0][0]
        username = res[0][1]
        user = {"username": username}
        db.commit()
        return count, user

    except Exception as inst:
        print(inst)
        db.rollback()

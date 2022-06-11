from connect import *


db = get_db()
cursor = db.cursor()


def search(searched_user):

    sql = """
    select userID 
    from `users`
    where userID LIKE %s
    """
    args = ['%' + searched_user + '%']

    try:
        cursor.execute(sql, args)
        result_array = cursor.fetchall()

        db.commit()
        return result_array

    except Exception as inst:
        print("error")
        print(inst)
        db.rollback()


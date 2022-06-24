from connect import *
from query_handler.logger import log
from query_handler.table_titles import TableTitles as t

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

    log(t.USERS, 'search for a user with ID like {} was made'.format(searched_user))
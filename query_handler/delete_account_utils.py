from connect import *
from query_handler.logger import log
from query_handler.table_titles import TableTitles as t

db = get_db()
cursor = db.cursor()


def remove_user(username):

    sql2 = """
    DELETE FROM `locochat`.`users` WHERE (`userID` = %s);
    """

    val = (username,)

    try:
        cursor.execute(sql2, val)
        db.commit()
        print('user deleted account successfully')

    except Exception as inst:
        print(inst)
        db.rollback()

    log(t.USERS, 'user with id of {} deleted account'.format(username))

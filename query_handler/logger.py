from connect import *
import time
import datetime

db = get_db()
cursor = db.cursor()


def log(table_name, desc):
    ts = time.time()
    log_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    sql = """
        insert into `logs`
        (event_table, description, event_time)
        VALUES
        (%s, %s, %s)
        """
    val = (table_name, desc, log_date)

    try:
        cursor.execute(sql, val)
        db.commit()

    except Exception as inst:
        print(inst)
        db.rollback()

import secrets
from hashlib import sha256
from connect import *
from query_handler.log_in import log_in

db = get_db()
cursor = db.cursor()


def sign_up(user):
    token = secrets.token_hex(25)
    sql = """
            insert into `users`
            (token, userID, first_name, last_name, phone_number, email, password_hashed, security_question_answer)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s)
            """
    val = (token, user['username'], user["first_name"], user["last_name"], user["phone_number"], user["email"],
           sha256(user["password"].encode('utf-8')).hexdigest(), user["security_question_answer"])

    try:
        cursor.execute(sql, val)
        db.commit()
        print("added to db")

    except Exception as inst:
        print("not added")
        print(inst)
        db.rollback()

    log_in(user)

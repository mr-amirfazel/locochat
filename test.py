from connect import get_db
from store import store
#
# shared = store()
# shared.count = 1
#
# shared2 = store()
# # shared2.count = 23
# # # print(shared.count)
# # with open("cli_assets/welcome.txt") as file:
# #     for line in file:
# #         print(line.rstrip())
# #
# test = "9931Abc#099"
# res = test.isdigit()
# print(res)
# import re
#
# name = 2
# def age():
#     return name+3
# print(age())
# print(shared2.error_message)
import mysql.connector as connector

NAME = "locochat"


def get_db():
    db = connector.connect(
        host="localhost",
        user="root",
        passwd="DbMYSQL2003",
        database=NAME
    )
    return db


db = get_db()
cursor = db.cursor()
# username = "amirfazel22"
# usernames = []
# usernames.append(username)
#
# query = " select userID from users"
# userIDs = ("amirfaze21","amirfazel22","amirfazel23")
# print(username in userIDs)
#
# cursor.execute(query)
# print(cursor.rowcount == 0)
# res = cursor.fetchall()
# print(type(res))
# for row in res:
#     print(row)
import secrets
# t = secrets.token_hex(25)
# print(t)
# t = secrets.token_hex(25)
# print(len(t))
from hashlib import sha256

user = {
    "username": input('username: '),
    "password": input('password: '),
    "first_name": input('first_name: '),
    "last_name": input('last_name: '),
    "phone_number": input('phone_number: '),
    "email": input('email: '),
    "security_question_answer": input('fav color: ')
}
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

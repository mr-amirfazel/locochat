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
username = "amirfazel22"
usernames = []
usernames.append(username)

query = " select userID from users"
userIDs = ("amirfaze21","amirfazel22","amirfazel23")
print(username in userIDs)

cursor.execute(query)
print(cursor.rowcount == 0)
res = cursor.fetchall()
print(type(res))
for row in res:
    print(row)
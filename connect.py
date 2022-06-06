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

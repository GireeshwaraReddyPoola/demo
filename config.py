import mysql.connector
def connect():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="aimlb2",
        database="aimlb2"

    )
    return mydb
print(connect())
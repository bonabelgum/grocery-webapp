import pymysql

def get_sql_connection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="wala",
        database="grocery_store"
    )
    return connection

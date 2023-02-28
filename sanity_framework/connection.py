import cx_Oracle

try:
    def get_connection():
        connection = cx_Oracle.connect(user="", password='',dsn="",encoding="UTF-8")
        return Connection
except :
    print(e)
else:
    print("connection Successfull")


def output_type_handler(cursor, default_type):
    if default_type == cx_Oracle.DB_TYPE_CLOB:
        return cursor.var(cx_Oracle.DB_TYPE_LONG, arraysize=cursor.arraysize)
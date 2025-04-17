import  mysql.connector as mysql

def conectar_db():
    return mysql.connect(
        user="root",
        password="xxxxxxxxxxxx",
        host="localhost",
        database="transportemercancias"
    )

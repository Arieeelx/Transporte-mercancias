import  mysql.connector as mysql

def conectar_db():
    return mysql.connect(
        user="root",
        password="zzzzzzzzzzz",
        host="localhost",
        database="transportemercancias"
    )

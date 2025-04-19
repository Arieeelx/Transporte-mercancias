import mysql.connector as mysql

def conectar_db():
    return mysql.connect(
        user="root",
        password="Javiteamo11.",
        host="localhost",
        database="transportemercancias"
    )

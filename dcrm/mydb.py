import mysql.connector

database=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Balaban123',
)

cursorobject=database.cursor()

cursorobject.execute("CREATE DATABASE elderco")

print("all done ")
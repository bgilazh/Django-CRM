import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'nurikshurik1'
)

cursorObject = dataBase.cursor()

#create db
cursorObject.execute("CREATE DATABASE elderco")

print("All Done")
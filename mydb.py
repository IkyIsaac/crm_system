import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='picfare'
)

cursorObject=dataBase.cursor()

cursorObject.execute('CREATE DATABASE ridstech')

print('All Done!')
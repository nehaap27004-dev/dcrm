import mysql.connector
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",                                    
    password="password123",
    )
cursortObject = dataBase.cursor()
#create a database
cursortObject.execute("CREATE DATABASE elderco")
print("All Done!")  
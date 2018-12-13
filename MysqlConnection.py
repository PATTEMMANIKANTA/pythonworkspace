from mysql import *
import mysql.connector

mydb = mysql.connector.connect(host= "10.1.20.75", user= "GxQATMS", password="GxQATMS", database="gxqa")

mycursor = mydb.cursor()
mycursor.execute("select * from user_details")
results = mycursor.fetchall()
for i in results:
    print(i)

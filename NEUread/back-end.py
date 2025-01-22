import mysql.connector
db = mysql.connector.connect(
    host="DESKTOP-6NMMH13",
    user="database",
    passwd = "12STEM7-B*",
    database = "schemaneuread"
)

mycursor = db.cursor()

mycursor.execute("USE sakila")
mycursor.execute("SHOW columns from actor")
print(mycursor.fetchall())
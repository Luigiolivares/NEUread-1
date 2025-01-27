import mysql.connector
db = mysql.connector.connect(
    host="DESKTOP-6NMMH13",
    user="database",
    passwd = "12STEM7-B*",
    database = "neuread"
)

mycursor = db.cursor()

mycursor.execute("USE neuread")
def getUserInfo(RFID, purpose):
    if purpose == "Info":
        mycursor.execute(f"SELECT * FROM users WHERE RFID = {RFID};")
        userInfo = mycursor.fetchall()
        mycursor.execute(f"SELECT * FROM borrowed_books WHERE RFID = {RFID};")
        userBorrowedBooks = mycursor.fetchall()
        return userInfo, userBorrowedBooks
    
    elif purpose == "history":
        mycursor.execute(f"SELECT * FROM borrow_history WHERE RFID = {RFID};")
        return mycursor.fetchall()
def searchBook(title):
    mycursor.execute("SELECT * FROM books WHERE Title LIKE %s", (f"%{title}%",))
    return mycursor.fetchall()

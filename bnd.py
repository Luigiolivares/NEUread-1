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
def searchBooks(column, ID):
    mycursor.execute(f"SELECT * FROM books WHERE {column} LIKE %s", (f"%{ID}%",))
    return mycursor.fetchall()
def showGenreBooks(genre, nthFrom, nthTo):
    mycursor.execute("SELECT * FROM books WHERE Genre = %s LIMIT %s OFFSET %s", (genre, nthTo, nthFrom))
    return mycursor.fetchall()
def showBorrowHistory(RFID, nthTo, nthFrom):
    mycursor.execute("SELECT * FROM borrowed_books WHERE RFID = %s LIMIT %s OFFSET %s", (RFID, nthTo, nthFrom))
    return mycursor.fetchall()
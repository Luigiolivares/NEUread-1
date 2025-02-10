import mysql.connector
db = mysql.connector.connect(
    host="DESKTOP-6NMMH13",
    user="database",
    passwd = "12STEM7-B*",
    database = "neuread"
)

mycursor = db.cursor()

mycursor.execute("USE neuread")
def getUserInfo(RFID):
    mycursor.execute(f"SELECT * FROM users WHERE RFID = {RFID};")
    userInfo = mycursor.fetchall()
    mycursor.execute(f"SELECT * FROM borrowed_books WHERE RFID = {RFID} AND `Date_returned` IS NULL;")
    userBorrowedBooks = mycursor.fetchall()
    return userInfo, userBorrowedBooks
def searchBooks(column, ID, nthTo, nthFrom):
    mycursor.execute(f"SELECT * FROM books WHERE {column} LIKE %s LIMIT %s OFFSET %s", (f"%{ID}%", nthTo, nthFrom))
    return mycursor.fetchall()
def showGenreBooks(genre, nthFrom, nthTo):
    mycursor.execute("SELECT * FROM books WHERE Genre = %s LIMIT %s OFFSET %s", (genre, nthTo, nthFrom))
    return mycursor.fetchall()
def showBorrowHistory(RFID, nthTo, nthFrom):
    mycursor.execute("SELECT * FROM borrowed_books WHERE RFID = %s AND `Date_returned` IS NOT NULL LIMIT %s OFFSET %s", (RFID, nthTo, nthFrom))
    return mycursor.fetchall()
def showGenres(nthTo, nthFrom):
    mycursor.execute("SELECT DISTINCT `Genre` FROM books LIMIT %s OFFSET %s", (nthTo, nthFrom))
    return mycursor.fetchall()
#print (showBorrowHistory(75240, 2, 0))
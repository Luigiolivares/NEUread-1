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

def searchBookID(bookID):
    mycursor.execute(f"SELECT Title, Author, Description, Availability, Book_Cover, Genre, Year_Publication, Book_Address FROM books WHERE Book_ID = {bookID};")
    return mycursor.fetchall()

def showGenreBooks(genre, nthFrom, nthTo):
    mycursor.execute("SELECT Book_ID, Book_Cover, Title  FROM books WHERE Genre = %s LIMIT %s OFFSET %s", (genre, nthTo, nthFrom))
    return mycursor.fetchall()

def showBorrowHistory(RFID, nthTo, nthFrom):
    mycursor.execute(
        "SELECT Book_ID, Date_Borrowed, Date_returned FROM borrowed_books WHERE RFID = %s AND `Date_returned` IS NOT NULL LIMIT %s OFFSET %s", 
        (RFID, nthTo, nthFrom)
    )
    
    items = mycursor.fetchall()  # Fetch borrowing history
    
    allBooks = []
    for book_id, date_borrowed, date_returned in items:
        mycursor.execute("SELECT Title, Author, Book_Cover, Availability, Year_Publication, Book_Address FROM books WHERE book_ID = %s", (book_id,))
        book_info = mycursor.fetchone()  # Fetch one book's info
        
        if book_info:  # If book info is found, combine data
            title, author, book_cover = book_info
            allBooks.append([book_cover, title, author, date_borrowed, date_returned])
    return allBooks

def showGenres(nthTo, nthFrom):
    mycursor.execute("SELECT DISTINCT `Genre` FROM books LIMIT %s OFFSET %s", (nthTo, nthFrom))
    return mycursor.fetchall()

def adminCheck(RFID):
    mycursor.execute("SELECT AName FROM admins WHERE ARFID = %s", (RFID,))
    return mycursor.fetchall()
def addBorrowBook(RFID, Book_ID, Date_Borrowed, Deadline, Date_returned):
    mycursor.execute("INSERT INTO borrowed_books (RFID, Book_ID, Date_Borrowed, Deadline, Date_returned) VALUES (%s, %s, %s, %s, %s)", (RFID, Book_ID, Date_Borrowed, Deadline, Date_returned))
    db.commit()
def showWhoToEmail():
    listGmail = []
    
    # Fetch overdue borrowed books
    mycursor.execute("SELECT * FROM borrowed_books WHERE date_returned IS NULL AND DATE(Deadline) <= DATE_SUB(CURDATE(), INTERVAL 3 DAY);")
    borrow_IDs = mycursor.fetchall()

    for row in borrow_IDs: 
        rfid = row[1]  # Assuming RFID is in the second column

        # Secure query to fetch email
        mycursor.execute("SELECT DISTINCT Email FROM users WHERE RFID = %s;", (rfid,))
        result = mycursor.fetchone()  # Get the single email result
        
        if result:  # Ensure result is not None
            listGmail.append(result[0])  # Append the email to the list

    print(listGmail)
    return listGmail
#print (showBorrowHistory(75240, 2, 0))
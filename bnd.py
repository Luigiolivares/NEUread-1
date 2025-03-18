import mysql.connector
from sendEmail import *
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "june12006",
    database = "neuread"
)

mycursor = db.cursor()

mycursor.execute("USE neuread")
def getUserInfo(RFID):
    # Secure query to fetch user info
    mycursor.execute("SELECT * FROM users WHERE RFID = %s;", (RFID,))
    userInfo = mycursor.fetchall()

    # Secure query to fetch borrowed books
    mycursor.execute(
        "SELECT Book_ID, Date_Borrowed, Deadline FROM borrowed_books WHERE RFID = %s AND Date_returned IS NULL;",
        (RFID,),
    )
    userBorrowedBooks = mycursor.fetchall()

    books = []
    for i in userBorrowedBooks:  # Loop through each borrowed book
        mycursor.execute("SELECT Title, Author, Book_Cover FROM books WHERE Book_ID = %s;", (i[0],))  # ✅ Use i[0] instead of userBorrowedBooks[0][0]
        book = mycursor.fetchone()  # ✅ Use fetchone() instead of fetchall()
        books.append(book)

    return userInfo, userBorrowedBooks, books

def searchBooks(column, ID, nthTo, nthFrom):
    mycursor.execute(f"SELECT Book_ID, Book_Cover, Title FROM books WHERE {column} LIKE %s LIMIT %s OFFSET %s", (f"%{ID}%", nthTo, nthFrom))
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
    mycursor.execute("SELECT Email FROM users WHERE RFID = %s", (RFID,))
    result = mycursor.fetchone()
    if result and result[0] == "Admin":
        return True
    else: 
        return False
def addBorrowBook(RFID, Book_ID, Date_Borrowed, Deadline, Date_returned):
    mycursor.execute("INSERT INTO borrowed_books (RFID, Book_ID, Date_Borrowed, Deadline, Date_returned) VALUES (%s, %s, %s, %s, %s)", (RFID, Book_ID, Date_Borrowed, Deadline, Date_returned))
    mycursor.execute(
        "UPDATE books SET availability = 0 WHERE Book_ID = %s",
        (Book_ID,)
    )
    db.commit()
    #SENDING AN EMAIL NA
    mycursor.execute("SELECT DISTINCT Email FROM users WHERE RFID = %s;", (RFID,))
    result = mycursor.fetchone()
    send_Borrow_Info(result[0])
def returnBook(RFID, Book_ID, Date_returned):
    # Update the borrowed_books table to set Date_returned where RFID and Book_ID match
    mycursor.execute(
        "UPDATE borrowed_books SET Date_returned = %s WHERE RFID = %s AND Book_ID = %s",
        (Date_returned, RFID, Book_ID)
    )

    # Update the books table to set availability back to 1 (available)
    mycursor.execute(
        "UPDATE books SET availability = 1 WHERE Book_ID = %s",
        (Book_ID,)
    )
    
    # Commit both operations
    db.commit()
def showWhoToEmail():
    listGmail = []
    
    # Fetch overdue borrowed books
    mycursor.execute("SELECT RFID FROM borrowed_books WHERE date_returned IS NULL AND DATE(Deadline) = CURDATE();")
    borrow_IDs = mycursor.fetchall()

    for row in borrow_IDs: 
        rfid = row[0]  # Assuming RFID is in the second column

        # Secure query to fetch email
        mycursor.execute("SELECT DISTINCT Email FROM users WHERE RFID = %s;", (rfid,))
        result = mycursor.fetchone()  # Get the single email result
        
        if result:  # Ensure result is not None
            listGmail.append(result[0])  # Append the email to the list

    print(listGmail)
    return listGmail
print (getUserInfo("0010516239")[1])
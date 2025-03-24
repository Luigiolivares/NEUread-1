import mysql.connector
from sendEmail import *
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
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
        mycursor.execute("SELECT Title, Author, Book_Cover FROM books WHERE book_ID = %s", (book_id,))
        book_info = mycursor.fetchone()  # Fetch one book's info
        if book_info:  # If book info is found, combine data
            title, author, book_cover = book_info
            allBooks.append([book_cover, title, author, date_borrowed, date_returned, book_id])
    return allBooks
def penalty(RFID, num):
    mycursor.execute("UPDATE users SET Penalty = %s WHERE RFID = %s", (num, RFID))
    db.commit()
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
        "UPDATE books SET availability = 0 WHERE Book_ID = %s",
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
        penalty(rfid, 1)
        # Secure query to fetch email
        mycursor.execute("SELECT DISTINCT Email FROM users WHERE RFID = %s;", (rfid,))
        result = mycursor.fetchone()  # Get the single email result
        
        if result:  # Ensure result is not None
            listGmail.append(result[0])  # Append the email to the list

    print(listGmail)
    return listGmail
def getUserAndBookNum():
        # Query 1: Count all rows in the table
        mycursor.execute("SELECT COUNT(*) FROM users;")
        total_UserRows = mycursor.fetchone()[0]
        mycursor.execute("SELECT COUNT(*) FROM books;")
        total_BookRows = mycursor.fetchone()[0]
        mycursor.execute("SELECT COUNT(*) FROM users where Penalty = '1';")
        total_PenaltyRows = mycursor.fetchone()[0]
        return total_UserRows, total_BookRows, total_PenaltyRows

def BnRcount_rows(start_date, end_date):
    query = """
    SELECT COUNT(*) 
    FROM borrowed_books 
    WHERE Date_borrowed BETWEEN %s AND %s;
    """
    mycursor.execute(query, (start_date, end_date))
    filtered_BorrowData = mycursor.fetchone()[0]

    query = """
    SELECT COUNT(*) 
    FROM borrowed_books 
    WHERE Date_returned BETWEEN %s AND %s;
    """
    mycursor.execute(query, (start_date, end_date))
    filtered_ReturnedData = mycursor.fetchone()[0]

    return filtered_BorrowData, filtered_ReturnedData
def export_to_excel(start_date, end_date):
    query = """
    SELECT * FROM borrowed_books
    WHERE Date_borrowed BETWEEN %s AND %s;
    """
    mycursor.execute(query, (start_date, end_date))
    
    # Fetch data
    rows = mycursor.fetchall()
    
    # Get column names
    column_names = [desc[0] for desc in mycursor.description]

    # Convert to DataFrame
    df = pd.DataFrame(rows, columns=column_names)

    # Define file name
    filename = "borrowed_books_export.xlsx"

    # Export to Excel (in the same directory as the script)
    df.to_excel(filename, index=False)

    return filename

def send_email_with_attachment(RECIPIENT_EMAIL, start_date, end_date):
    # Email Credentials
    SENDER_EMAIL = "neuread.neuis@gmail.com"
    SENDER_PASSWORD = "agiv uhqq tlhg sjre"

    subject = "Borrowed Books Data Export"
    body = f"Here is the exported data of borrowed books from {start_date} to {end_date}."

    # Export the data
    filename = export_to_excel(start_date, end_date)
    print(filename)
    if filename is None:
        print("❌ Failed to export data. Email not sent.")
        return

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Attach the Excel file
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(filename)}")
    msg.attach(part)

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        server.quit()

        print(f"✅ Email with attachment sent successfully to {RECIPIENT_EMAIL}!")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from email.mime.image import MIMEImage
# Function to send an email
def send_Borrow_Info(RECIPIENT_EMAIL, title, author, Date_Borrowed, Deadline):
    # Email Credentials
    SENDER_EMAIL = "neuread.neuis@gmail.com"
    SENDER_PASSWORD = "agiv uhqq tlhg sjre"

    subject = "📚 NEURead Borrowing Confirmation"
    body = f"""\
<html>
    <body>
        <p><b>Hello, Eranian! 👋</b></p>
        <p>You have successfully borrowed <b>"{title}"</b> through the <b>NEURead System</b>! Here are more details:</p>
        <ul>
            <li><b>📖 Book:</b> {title} by {author}</li>
            <li><b>📅 Borrowed On:</b> {Date_Borrowed}</li>
            <li><b>⏳ Due Date:</b> {Deadline}</li>
        </ul>
        <p><b>⚠️ Make sure to return the book within the given deadline to avoid penalties.</b></p>
        <p><b>Enjoy your reading! 📚</b></p>

        <!-- Footer Section -->
        <hr style="border: 1px solid #ccc; margin-top: 20px;">
        <div style="text-align: center; padding-top: 10px;">
            <img src="cid:footer_img" style="display: block; width: 100%; height: auto; margin: 0 auto;">
            <p style="color: gray; font-size: 14px;">NEURead Library System | © 2025 New Era University</p>
        </div>
    </body>
</html>
"""

    emailSend(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, subject, body)

def send_Deadline_Info(RECIPIENT_EMAIL, title, deadline):
    # Email Credentials
    SENDER_EMAIL = "neuread.neuis@gmail.com"
    SENDER_PASSWORD = "agiv uhqq tlhg sjre"

    subject = "malapit na deadline"
    body = f"""\
<html>
    <body>
        <p><b>Hello, Eranian! 👋</b></p>
        <p>You currently have <b>"{title}"</b> on your account, due to be returned by:</p>

        <p style="font-size: 30px;"><b>[{deadline}]</b></p>
        <p><b>Make sure to return the book within the given deadline to avoid penalties. 📚</b></p>
        <p>Enjoy your reading! 📚</p>

        <!-- Footer Section -->
        <hr style="border: 1px solid #ccc; margin-top: 20px;">
        <div style="text-align: center; padding-top: 10px;">
            <img src="cid:footer_img" style="display: block; width: 100%; height: auto; margin: 0 auto;">
            <p style="color: gray; font-size: 14px;">NEURead Library System | © 2025 New Era University</p>
        </div>
    </body>
</html>
"""
    emailSend(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, subject, body)

def emailSend(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, subject, body):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    with open("footer.png", "rb") as img:
        footer_img = MIMEImage(img.read())
        footer_img.add_header("Content-ID", "<footer_img>")  # Reference in HTML
        msg.attach(footer_img)

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        server.quit()
        print("Email sent successfully at 4 PM!")

    except Exception as e:
        print(f"Failed to send email: {e}")
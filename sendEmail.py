import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send an email
def send_Borrow_Info(RECIPIENT_EMAIL):
    # Email Credentials
    SENDER_EMAIL = "neuread.neuis@gmail.com"
    SENDER_PASSWORD = "agiv uhqq tlhg sjre"

    subject = "New Borrow"
    body = "nag borrow ka ng book noh?"
    emailSend(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, subject, body)

def send_Deadline_Info(RECIPIENT_EMAIL):
    # Email Credentials
    SENDER_EMAIL = "neuread.neuis@gmail.com"
    SENDER_PASSWORD = "agiv uhqq tlhg sjre"
    RECIPIENT_EMAIL = "yourFranzkafka@gmail.com"

    subject = "New Borrow"
    body = "nag borrow ka ng book noh?"
    emailSend(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, subject, body)

def emailSend(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, subject, body):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
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
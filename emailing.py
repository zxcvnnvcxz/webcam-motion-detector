import os
import imghdr
import smtplib
from email.message import EmailMessage

PASSWORD = os.getenv("GMAIL_PW")
SENDER = os.getenv("GMAIL_USER")
RECEIVER = os.getenv("GMAIL_USER")


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer has showed up."
    email_message.set_content("To the reception please.")

    with open(image_path, "rb") as file: # read binary
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/19.png")

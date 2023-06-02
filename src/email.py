# Relative path
import os

# Email modules
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.credentials import getCredentials


directory = os.path.dirname(os.path.abspath(__file__))


def getContents(fileName):
    with open(os.path.join(directory, fileName), "r", encoding="utf8") as file:
        return file.read()


class Email():
    def __init__(self):
        self.password = getCredentials()
        self.subject = getContents('../email/subject.txt')
        self.sender = getContents('../email/from.txt')
        self.to = [i.split(',') for i in getContents('../email/to.txt').split('\n')]
        self.bcc = getContents('../email/bcc.txt')
        self.text = getContents('../email/text.txt')
        self.html = getContents('../email/html.txt')
        self.message = None
        self.counter = 0

    def createMessage(self, text=None, html=None):
        self.message = MIMEMultipart("alternative")
        self.addContent(text, html)
        self.addFiles()

    def addContent(self, text=None, html=None):
        self.message['Subject'] = self.subject
        self.message['From'] = self.sender
        self.message['Bcc'] = self.bcc
        if text is not None and html is not None:
            self.message.attach(MIMEText(text, "plain"))
            self.message.attach(MIMEText(html, "html"))
        else:
            self.message.attach(MIMEText(self.text, "plain"))
            self.message.attach(MIMEText(self.html, "html"))

    def addFiles(self):
        fileDirectory = os.path.join(directory, "../files")
        files = [f for f in os.listdir(fileDirectory) if os.path.isfile(os.path.join(fileDirectory, f))]

        for file in files:
            with open(os.path.join(fileDirectory, file), 'rb') as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {file}",
                )
            
            self.message.attach(part)

    def send(self):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.sender, self.password)
            smtp.send_message(self.message)
            self.counter += 1
            print(f"Sent email {self.counter} to {self.message['To']}")

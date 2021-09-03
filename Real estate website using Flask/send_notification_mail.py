from openpyxl.workbook import Workbook
from openpyxl import load_workbook
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as p
import smtplib


def send_notification_mail():
    data = p.read_excel('SubscribersList.xlsx')
    emailcol = data.get("Emails")
    list_of_mails = list(emailcol)
    print(list_of_mails)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("Email address", "password")  # Put email address and password
        from_ = "Email address"       # Put email address
        to_ = list_of_mails
        message = MIMEMultipart("alternative")
        message['Subject'] = 'Sombody just posted'
        html='''
        <html>
        <head>

        </head>
        <body>
            <h1>New Post Notification</h1>
            <h2> Do visit  </h2>
            <p>Thanks for Subscribe us!! PropertyFY</p>

        </body>
        </html>

        '''

        text = MIMEText(html, "html")

        message.attach(text)
        server.sendmail(from_, to_, message.as_string())
        print("message has been to the emails.")
    
    except Exception as e:
        print(e)
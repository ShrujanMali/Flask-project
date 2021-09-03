from email import message
import smtplib
from email.mime.text import MIMEText

def send_mail(name, email, description):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'Mailtrap user id'
    password = 'Mailtrap password'
    message = f"<h3>Contact us notification</h3><ul><li>Name: {name}</li><li>Email address: {email}</li><li>Description: {description}</li>"

    sender_email = 'PropertyFy.com'
    receiver_email = 'PropertyFY.mailtrap.io'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Contact us'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())    
    

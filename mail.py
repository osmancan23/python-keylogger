import smtplib
from email.message import EmailMessage

outlook_server = 'smtp-mail.outlook.com'
outlook_user = 'bsgproje1@outlook.com'
outlook_password = 'bsgbsg2323'
server_port = 587
to_User= 'bsgproje1@outlook.com'

def sendMail(message):

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'Test Mesajı'
    msg['From'] = outlook_user
    msg['To'] = to_User

    server = smtplib.SMTP(outlook_server, server_port)

    server.starttls()

    server.login(outlook_user, outlook_password)

    server.send_message(msg)

    server.quit()

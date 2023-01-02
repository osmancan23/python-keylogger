import smtplib
from email.message import EmailMessage

# Outlook SMTP sunucusunun adresini ve giriş bilgilerini belirtin
outlook_server = 'smtp-mail.outlook.com'
outlook_user = 'bsgproje1@outlook.com'
outlook_password = 'bsgbsg2323'


def sendMail(message):

    # E-posta mesajını oluşturun
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'Test Mesajı'
    msg['From'] = outlook_user
    msg['To'] = 'bsgproje1@outlook.com'

    # SMTP sunucusunu başlatın
    server = smtplib.SMTP(outlook_server, 587)

    # Sunucuya bağlanın (güvenliği artırmak için SSL kullanabilirsiniz)
    server.starttls()

    # Sunucuya giriş yapın
    server.login(outlook_user, outlook_password)

    # E-postayı gönderin
    server.send_message(msg)

    # Sunucudan çıkış yapın
    server.quit()

from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'vidheshkhanna@gmail.com'
email_password = 'ifmrznovxmancylh'
email_receiver = 'tariqmodi01@gmail.com'

subject = 'Bhai Ye mail wala task ho gaya'
body = """
I will post it on linkedIn complete my task 2 of day 2 and then will help you out.
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
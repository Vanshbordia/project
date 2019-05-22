import smtplib, ssl
import pandas as pd

data=pd.read_csv('mail.csv')
rmail=data['Emails'].values

port = 465  # For SSL
smtp_server = "smtp.yandex.com"
sender_email = "interns@littlelove.org.in"  # Enter your address
receiver_email = rmail  # Enter receiver address
password = str(input("Enter Password"))
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print("Done")

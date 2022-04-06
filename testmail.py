import smtplib

def sending_mail(receiver_email, subject, message):

    port = int(587)
    smtp_server = "smtp.gmail.com"
    sender_email = "pythonpractice826@gmail.com"  # Enter your address
    password = "Temp@1234"
    msg = "Subject: "+subject+"\n"+message
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg)
    print("Mail Sent")

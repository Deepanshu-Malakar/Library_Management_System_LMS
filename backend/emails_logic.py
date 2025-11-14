import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(reciever):
    sender_email = "your_email@gmail.com"
    app_password = "your_app_password"
    receiver_email = "receiver@gmail.com"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Test Email from Python"

    body = "Hello! This is a test email sent from Python."
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
        server.quit()
    except Exception as e:
        print("Error:", e)

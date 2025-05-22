import os
import smtplib,ssl

def send_email(message_p):
    host ="smtp.gmail.com"
    port = 465

    username = "mohamedfarveez1810@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "mohamedfarveez1@gmail.com"

    context = ssl.create_default_context()

    message = message_p

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

if __name__ == "__main__":
    message = input("Type the message that you want to mail: ")
    send_email( message)


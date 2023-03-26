import smtplib
from email.mime.text import MIMEText

from messages import Message
import settings


text = Message()


def send_email(message):
    receiver = text.get_receiver()
    sender = settings.get_sender()
    password = settings.get_key()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        message = MIMEText(message, 'plain', 'utf-8')
        message["Subject"] = text.get_subject()
        server.sendmail(sender, receiver, message.as_string())

        return "The message was sent successfully!"

    except Exception as _ex:
        return f"{_ex}\nSomething went wrong... Please, check your settings!"


def main():
    message = text.get_message()
    print(send_email(message=message))


if __name__ == '__main__':
    main()

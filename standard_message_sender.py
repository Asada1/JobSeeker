import smtplib
from email.mime.text import MIMEText

import settings
import standard_message as sm


def send_email(message):
    sender = settings.get_sender()
    password = settings.get_key()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        tolist = sm.get_receiver()
        server.login(sender, password)
        message = MIMEText(message, 'plain', 'utf-8')
        message["Subject"] = sm.get_subject()
        message["From"] = sender
        message["To"] = ', '.join(tolist)
        server.sendmail(sender, tolist, message.as_string())

        return "The message was sent successfully!"

    except Exception as _ex:
        return f"{_ex}\nSomething went wrong... Please, check your settings!"


def main():
    message = sm.get_message()
    print(send_email(message=message))


if __name__ == '__main__':
    main()

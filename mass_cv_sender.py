import smtplib
from email.mime.text import MIMEText

import settings
import mass_messages as mm


def get_set_messages():
    message_receivers = mm.mass_receiver()
    message_subject = mm.mass_subject()
    message_text = mm.mass_message()

    message_list = list(zip(message_receivers, message_subject, message_text))

    return message_list


def send_email():
    sender = settings.get_sender()
    password = settings.get_key()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    message_set = get_set_messages()
    for a_set in message_set:
        try:
            receiver = a_set[0]
            server.login(sender, password)
            message = a_set[2]
            message = MIMEText(message, 'plain', 'utf-8')
            message["Subject"] = a_set[1]
            message["From"] = sender
            message["To"] = a_set[0]
            server.sendmail(sender, receiver, message.as_string())

            return "The message was sent successfully!"

        except Exception as _ex:
            return f"{_ex}\nSomething went wrong... Please, check your settings!"


def main():
    print(send_email())


if __name__ == '__main__':
    main()

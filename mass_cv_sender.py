import smtplib
from email.mime.text import MIMEText

import settings
import mass_messages as mm


def get_set_messages():
    message_text = mm.mass_message()
    message_subject = mm.mass_subject()
    message_receivers = mm.mass_receiver()

    message_list = list(zip(message_text, message_subject, message_receivers))

    return message_list


def send_email(message):
    message_set = get_set_messages()
    for set in message_set:
        sender = settings.get_sender()
        password = settings.get_key()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        try:
            receiver = set[0]
            server.login(sender, password)
            message = MIMEText(message, 'plain', 'utf-8')
            message["Subject"] = messages.get_subject()
            message["From"] = sender
            message["To"] = ', '.join(tolist)
            server.sendmail(sender, receiver, message.as_string())

            return "The message was sent successfully!"

        except Exception as _ex:
            return f"{_ex}\nSomething went wrong... Please, check your settings!"


def main():
    message = messages.get_message()
    print(send_email(message=message))


if __name__ == '__main__':
    main()

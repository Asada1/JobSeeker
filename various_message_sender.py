import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import settings
import various_messages as vm
import standard_message as sm


def get_set_messages():
    message_receivers = vm.mass_receiver()
    message_subject = vm.mass_subject()
    message_text = vm.mass_message()

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
            # message = MIMEText(message, 'plain', 'utf-8')
            message = MIMEMultipart()
            message["From"] = sender
            message["To"] = a_set[0]
            message["Subject"] = a_set[1]
            message_text = a_set[2]
            message.attach(MIMEText(message_text, 'plain', 'utf-8'))
            file = sm.get_file()
            filename = os.path.basename(file)
            file.add_header('content-disposition', 'attachment', filename=filename)
            message.attach(file)
            server.sendmail(sender, receiver, message.as_string())
            print(a_set)
            print("The message was sent successfully!")

        except Exception as _ex:
            return f"{_ex}\nSomething went wrong... Please, check your settings!"


def main():
    print(send_email())


if __name__ == '__main__':
    main()

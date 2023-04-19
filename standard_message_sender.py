import mimetypes
import os
import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from tqdm import tqdm

import settings
import standard_message as sm


def send_email():
    sender = settings.get_sender()
    password = settings.get_key()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        tolist = sm.get_receiver()
        server.login(sender, password)
        # message = MIMEText(message, 'plain', 'utf-8')
        message = MIMEMultipart()
        message["Subject"] = sm.get_subject()
        message["From"] = sender
        message["To"] = ', '.join(tolist)
        message_text = sm.get_message()
        message.attach(MIMEText(message_text, 'plain', 'utf-8'))

        for file in tqdm(os.listdir("attachments")):
            filename = os.path.basename(file)
            ftype, encoding = mimetypes.guess_type(file)
            file_type, subtype = ftype.split("/")
            with open(f"attachments/{file}", "rb") as f:
                file = MIMEBase(file_type, subtype)
                file.set_payload(f.read())
                encoders.encode_base64(file)
            file.add_header('content-disposition', 'attachment', filename=filename)
            message.attach(file)

        server.sendmail(sender, tolist, message.as_string())
        print(tolist)
        return "The message was sent successfully!"

    except Exception as _ex:
        return f"{_ex}\nSomething went wrong... Please, check your settings!"


def main():
    print(send_email())


if __name__ == '__main__':
    main()

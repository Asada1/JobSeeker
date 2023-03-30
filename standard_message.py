import os
import mimetypes
from tqdm import tqdm
from email import encoders
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase


def get_message():
    with open('email_stuff/standard/message_text.txt', 'r') as message_text:
        message = message_text.read()
    return message


def get_subject():
    with open('email_stuff/standard/message_subject.txt', 'r') as letter_subject:
        subject = letter_subject.read()
    return subject


def get_receiver():
    with open('email_stuff/standard/receivers.txt', 'r') as receivers:
        receiver = receivers.readlines()
    return receiver


def get_file():
    for file in tqdm(os.listdir("attachments")):
        filename = os.path.basename(file)
        ftype, encoding = mimetypes.guess_type(file)
        file_type, subtype = ftype.split("/")

        if file_type == "text":
            with open(f"attachments/{file}") as f:
                file = MIMEText(f.read())

        elif file_type == "application":
            with open(f"attachments/{file}", "rb") as f:
                file = MIMEApplication(f.read(), subtype)

        else:
            with open(f"attachments/{file}", "rb") as f:
                file = MIMEBase(file_type, subtype)
                file.set_payload(f.read())
                encoders.encode_base64(file)

        file.add_header('content-disposition', 'attachment', filename=filename)
        msg.attach(file)

    return file

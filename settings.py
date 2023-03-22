import smtplib


def get_sender():
    with open('keybox/sender.txt', 'r') as senders:
        sender = str(senders.read())

    return sender


def get_key():
    with open('keybox/key.txt', 'r') as keylock:
        key = str(keylock.read())

    return key


def get_settings():
    sender = get_sender()
    password = get_key()
    server = smtplib.SMTP("smtp.gmail.com", 587)

    setting_tuple = (sender, password, server)

    return setting_tuple

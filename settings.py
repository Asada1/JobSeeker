import smtplib


def get_sender():
    with open('sender.txt', 'r') as senders:
        sender = str(senders.read())

    return sender


def get_key():
    with open('keys.txt', 'r') as keylock:
        key = str(keylock.read())

    return key


def get_settings():
    sender = get_sender()
    password = "##whatever**"

    server = smtplib.SMTP("smtp.gmail.com", 587)

    setting_tuple = (sender, password, server)

    return setting_tuple


if __name__ == '__main__':
    get_sender()

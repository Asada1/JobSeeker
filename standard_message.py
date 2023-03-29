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

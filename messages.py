from .keybox import texts


def get_message():
    message = texts.compose_my_letter()

    return message


def get_subject():
    subject = texts.make_my_header()

    return subject


def get_receiver():
    with open('keybox/receivers.txt', 'r') as receivers_list:
        for line in receivers_list:
            receiver = line

    return receiver


def get_header():
    header = ''

    return header

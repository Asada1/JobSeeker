def get_message():
    message = ''

    return message


def get_subject():
    subject = ''

    return subject


def get_receiver():
    with open('receivers.txt', 'r') as receivers_list:
        for line in receivers_list:
            receiver = line

    return receiver


def get_header():
    header = ''

    return header

def get_message():
    with open('tools/texts.txt', 'r') as texts:
        text = texts.read()
    return text


def get_subject():
    with open('tools/subjects.txt', 'r') as subjects:
        subject = subjects.read()
    return subject


def get_receiver():
    with open('tools/receivers.txt', 'r') as receivers:
        receiver = receivers.readlines()

    return receiver

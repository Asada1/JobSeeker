def mass_message():
    with open('tools/text.txt', 'r') as message_text:
        message = message_text.readlines()
    return message


def mass_subject():
    with open('tools/subjects.txt', 'r') as subjects:
        subject = subjects.readlines()
    return subject


def mass_receiver():
    with open('tools/receivers.txt', 'r') as receivers:
        receiver = receivers.readlines()
    return receiver

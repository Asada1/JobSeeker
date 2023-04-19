def mass_message():
    with open('email/various/message_texts.txt', 'r') as message_texts:
        message = message_texts.readlines()
    return message


def mass_subject():
    with open('email/various/message_subjects.txt', 'r') as letter_subjects:
        subject = letter_subjects.readlines()
    return subject


def mass_receiver():
    with open('email/various/receivers.txt', 'r') as receivers:
        receiver = receivers.readlines()
    return receiver

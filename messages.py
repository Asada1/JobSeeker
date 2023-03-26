import texts


class Message:
    def __init__(self, message, subject, receiver):
        self.message = message
        self.subject = subject
        self.receiver = receiver

    def get_message():
        message = texts.compose_my_letter()
        return message

    def get_subject():
        subject = texts.make_my_header()
        return subject

    def get_receiver():
        receiver = texts.get_receiver()
        return receiver


def get_header():
    header = ''

    return header

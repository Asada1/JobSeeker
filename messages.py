import texts


class Message:
    def __init__(self, message, subject, receiver):
        self.message = message
        self.subject = subject
        self.receiver = receiver

    def get_message(self):
        self.message = texts.compose_my_letter()
        return self.message

    def get_subject(self):
        self.subject = texts.make_my_header()
        return self.subject

    def get_receiver(self):
        self.receiver = texts.get_receiver()
        return self.receiver


def get_header():
    header = ''

    return header

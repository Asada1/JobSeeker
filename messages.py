class Message:
    def get_message(self):
        with open('keybox/texts.txt', 'r') as texts:
            text = texts.read()
        return text

    def get_subject(self):
        with open('keybox/subjects.txt', 'r') as subjects:
            subject = subjects.read()
        return subject

    def get_receiver(self):
        with open('keybox/receivers.txt', 'r') as receivers:
            receiver = receivers.read()
        return receiver

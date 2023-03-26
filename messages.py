class Message:
    def get_message(self):
        with open('tools/texts.txt', 'r') as texts:
            for line in texts.read():
                text = line
                return text

    def get_subject(self):
        with open('tools/subjects.txt', 'r') as subjects:
            subject = subjects.read()
        return subject

    def get_receiver(self):
        with open('tools/receivers.txt', 'r') as receivers:
            receiver = receivers.read()
        return receiver

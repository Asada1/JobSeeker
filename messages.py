class Message:
    def get_message(self):
        with open('tools/texts.txt', 'r') as texts:
            for line in texts.read():
                text = line
                return text

    def get_subject(self):
        with open('tools/subjects.txt', 'r') as subjects:
            for line in subjects.read():
                subject = line
                return subject

    def get_receiver(self):
        with open('tools/receivers.txt', 'r') as receivers:
            for line in receivers.read():
                receiver = line
                return receiver

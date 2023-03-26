import texts


class Message:
    def get_message(self):
        message = 'hello'
        return message

    def get_subject(self):
        self.subject = 'subject'
        return self.subject

    def get_receiver(self):
        self.receiver = 'receiver'
        return self.receiver


message = Message()


if __name__ == '__main__':
    print(message.get_message())

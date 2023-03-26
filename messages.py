import texts


class Message:
    def get_message(self):
        message = 'hello'
        return message

    def get_subject(self):
        subject = 'subject'
        return subject

    def get_receiver(self):
        receiver = 'receiver'
        return receiver


message = Message()


if __name__ == '__main__':
    print(message.get_message(), message.get_receiver(), message.get_subject())

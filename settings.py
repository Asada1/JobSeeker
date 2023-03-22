def get_sender():
    with open('keybox/sender.txt', 'r') as senders:
        sender = senders.read()

    return sender


def get_key():
    with open('keybox/key.txt', 'r') as keylock:
        key = keylock.read()

    return key

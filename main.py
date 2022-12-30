import smtplib


def send_email(message):
    sender = "whatever"
    password = "whatever"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, sender, message)

        return "The message was sent successfully!"

    except Exception as _ex:
        return f"{_ex}\nCheck your login/pass or do whatever you need to fix this bug, please!"



def main():
    ...


if __name__ == '__main__':
    main()

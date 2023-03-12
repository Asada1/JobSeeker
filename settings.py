import smtplib


def get_settings():
    sender = "your.email@isegal.de"
    password = "##whatever**"

    server = smtplib.SMTP("smtp.gmail.com", 587)

    setting_tuple = (sender, password, server)

    return setting_tuple

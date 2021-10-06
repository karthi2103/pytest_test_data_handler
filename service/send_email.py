import re

from exceptions.email import InvalidMessageBodyException, InvalidEmailException
from model.email import Message, EmailResponse


def connect_to_server():
    print("connecting to email server")


def validate_email(email):
    if not email or not bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)):
        raise InvalidEmailException(f"email: {email} is not a valid email address")


def validate_message(message: Message):
    if not message.body or not message.subject:
        raise InvalidMessageBodyException("message body and (or) subject is empty")


def email_validator(func):
    def _processor(from_: str, to: str, message: Message):
        validate_email(from_)
        validate_email(to)
        validate_message(message)
        return func(from_, to, message)

    return _processor


@email_validator
def send_email(from_: str, to: str, message: Message):
    connect_to_server()
    print("sending email \n")
    print(f"FROM: {from_}")
    print(f"TO: {to}")
    print(f"TITLE: {message.subject}")
    print(f"{message.body}")
    if message.signature:
        print(f"{message.signature.salutation},")
        print(f"{message.signature.firstname} {message.signature.lastname}")
    return EmailResponse(sent=True, error=None)

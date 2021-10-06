from dataclasses import dataclass


@dataclass
class Signature:
    firstname: str
    lastname: str
    salutation: str


@dataclass
class Message:
    subject: str
    body: str
    signature: Signature


class EmailError:
    message: str


@dataclass
class EmailResponse:
    sent: bool
    error: EmailError

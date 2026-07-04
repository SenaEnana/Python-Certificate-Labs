class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True
        
class User:
    def __init__(self, name, inbox):
        self.name = name
        self.inbox = Inbox()
        
    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)

class Inbox:
    def __init__(self):
        self.emails = []
    def receive_email(self, email):
        self.emails.append(email)    
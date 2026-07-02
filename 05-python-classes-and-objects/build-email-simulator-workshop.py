class Email:
    def __init__(self, sender, receiver, subject, body, read):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False
        
email_obj = Email('alice@example.com', 'bob@example.com', 'Hello', 'Hi Bob!', False)
print(email_obj.sender)
print(email_obj.subject)
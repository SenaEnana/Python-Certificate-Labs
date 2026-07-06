class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

    def display_full_email(self):
        self.mark_as_read()    
        
class User:
    def __init__(self, name, inbox):
        self.name = name
        self.inbox = Inbox()
        
    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)  
        print("\n--- Email ---") 
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')    
        print(f'Subject: {self.subject}')
        print(f'Body: {self.body}')
        print('------------\n')     

    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f'[{status}] From: {self.sender.name} | Subject: {self.subject}' 

class Inbox:
    def __init__(self):
        self.emails = []
    def receive_email(self, email):
        self.emails.append(email)    

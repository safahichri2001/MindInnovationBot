from utils.email_utils import send_email

class NotifierAgent:
    def notify(self, summary):
        send_email(summary)

# agents/notifier.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import yaml
from datetime import date

class NotifierAgent:
    def __init__(self, config_path="config/settings.yaml"):
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)["EMAIL_CONFIG"]

        self.sender = config["sender"]
        self.recipient = config["recipient"]
        self.smtp_server = config["smtp_server"]
        self.port = config["port"]
        self.username = config["username"]
        self.password = config["password"]

    def notify(self, summary):
        today = date.today().strftime("%B %d, %Y")
        subject = f"🩺 MindInnovationBot Digest – {today}"

        msg = MIMEMultipart()
        msg["From"] = self.sender
        msg["To"] = self.recipient
        msg["Subject"] = subject

        # Format summary as plain text or HTML
        msg.attach(MIMEText(summary, "plain"))

        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.send_message(msg)

        print(f"📧 Email sent to {self.recipient}")

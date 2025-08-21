import smtplib
from email.mime.text import MIMEText
import yaml

with open("config/settings.yaml", "r") as f:
    config = yaml.safe_load(f)
EMAIL_CONFIG = config["EMAIL_CONFIG"]

def send_email(summary):
    msg = MIMEText(summary)
    msg["Subject"] = "🩺 Daily Health Update: Qatar & Saudi Arabia"
    msg["From"] = EMAIL_CONFIG["sender"]
    msg["To"] = EMAIL_CONFIG["recipient"]

    with smtplib.SMTP(EMAIL_CONFIG["smtp_server"], EMAIL_CONFIG["port"]) as server:
        server.starttls()
        server.login(EMAIL_CONFIG["username"], EMAIL_CONFIG["password"])
        server.send_message(msg)

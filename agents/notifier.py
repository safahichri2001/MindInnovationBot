import requests

class NotifierAgent:
    def notify(self, summary):
        webhook_url = "https://your-n8n-instance.com/webhook/notify"
        payload = {"message": summary}
        requests.post(webhook_url, json=payload)

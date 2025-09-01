# run_scheduler.py
import schedule
import time
from agents.notifier import NotifierAgent
from agents.summarizer import get_daily_summary

def job():
    summary = get_daily_summary()
    notifier = NotifierAgent()
    notifier.notify(summary)

schedule.every().day.at("07:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)

from email import message
from twilio.rest import Client
from datetime import datetime

def notify_me():
    content="its been a while"
    client=Client("AC8ad2a78399a48d65352f78c29960d359","ef8c76d40dd4412b5cd34f3f410038a1")
    message=client.messages.create(body=content,from_="whatsapp:+14155238886",to="whatsapp:+254798338168")
def send():
    time=datetime.now()
    t=time.strftime("%H:%M:%S")
    limit=7
    for x in range(4):
        notify_me()
send()
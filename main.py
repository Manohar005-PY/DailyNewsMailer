import requests
from email.message import EmailMessage
import smtplib
import time
import schedule
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
email_sender = os.getenv("EMAIL_SENDER")
email_password = os.getenv("EMAIL_PASSWORD")
email_receiver = os.getenv("EMAIL_RECEIVER")

def email_msg(head_line):
    msg = EmailMessage()
    msg['from'] = email_sender
    msg['to'] = email_receiver
    msg['subject'] = "This Is The Todays Top 5 Headline"
    msg.set_content(head_line)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(email_sender,email_password)
            smtp.send_message(msg)
            print("the email has been sent")
    except Exception as e:
        print("The mail cant be sent" ,e)


def headline():
    url = f"https://newsapi.org/v2/everything?q=technology&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    if(response.status_code == 200 and 'articles' in data):
        head_lines = []
        for i, article in enumerate(data['articles'][:5],start=1):
            print(f"{i}. {article['title']}")
            title = article['title']
            head_lines.append(f"{i}. {title}\n")

        head_line = "\n".join(head_lines)
        return head_line
    else:
        print("No Head line was fleatched")
        return None

def main():
    head_line = headline()
    if(head_line):
        email_msg(head_line)
    else:
        print("There is no headlines sent")

schedule.every().day.at("06:00").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)


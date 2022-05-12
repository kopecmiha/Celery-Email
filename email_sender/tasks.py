from email_sender.utils import EmailSender
from main.celery import app


@app.task
def send_email_task(email_template, msg, recipient_list):
    EmailSender().send_email(
        email_template=email_template,
        msg=msg,
        recipient_list=recipient_list,
    )

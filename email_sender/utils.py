from django.core.mail import send_mail

from main import settings


class EmailSender:
    def __init__(self):
        self.templates_dict = {
            "user_registration": {
                "subject": "Confirm your email",
                "from_email": "G&H <{}>".format(settings.EMAIL_HOST_USER),
            }
        }

    def send_email(self, email_template=None, msg=None, recipient_list=None):
        email_template = self.templates_dict[email_template]
        email_template["html_message"] = msg
        email_template["message"] = msg
        email_template["recipient_list"] = recipient_list
        send_mail(**email_template)

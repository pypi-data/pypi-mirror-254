from novu.api import EventApi

class Email:
    def __init__(self, url, api_key):
        self.novu = EventApi(url, api_key)

    def send_email(self, to, subject, body):
        self.novu.trigger(
            name="email-workflow-example",
            recipients=to,
            payload={
                "subject": subject,
                "body": body
            }
        )

    def receive_email(self):
        # Email receiving logic here
        pass

class SMS:
    def __init__(self, url, api_key):
        self.novu = EventApi(url, api_key)

    def send_sms(self, to, message):
        self.novu.trigger(
            name="sms-workflow-example",
            recipients=to,
            payload={
                "message": message
            }
        )

    def receive_sms(self):
        # SMS receiving logic here
        self.novu.trigger(
            name="sms-workflow-example",
            recipients=to,
            payload={
                "message": message
            }
        )

class SNSDM:
    def __init__(self, url, api_key):
        self.novu = EventApi(url, api_key)

    def send_sns_dm(self, recipient, message):
        self.novu.trigger(
            name="sns-dm-workflow-example",
            recipients=recipient,
            payload={
                "message": message
            }
        )

    def receive_sns_dm(self):
        # SNS direct message receiving logic here
        self.novu.trigger(
            name="sns-dm-workflow-example",
            recipients=recipient,
            payload={
                "message": message
            }
        )
        pass

class Notification:
    def __init__(self, url, api_key):
        self.novu = EventApi(url, api_key)

    def send_notification(self, recipient, message):
        self.novu.trigger(
            name="notification-workflow-example",
            recipients=recipient,
            payload={
                "message": message
            }
        )

    def receive_notification(self):
        # Generic notification receiving logic here
        self.novu.trigger(
            name="notification-workflow-example",
            recipients=recipient,
            payload={
                "message": message
            }
        )
        pass

class MailAPI:
    def __init__(self, smtp_server, port, username, password):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, to_address, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = to_address

        server = smtplib.SMTP(self.smtp_server, self.port)
        server.login(self.username, self.password)
        server.send_message(msg)
        server.quit()
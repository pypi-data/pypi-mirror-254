import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import webcolors
import datetime


class Zonotify:
    def __init__(self, discord_webhook_url=None, gmail_credentials=None):
        self.discord_webhook_url = discord_webhook_url
        self.gmail_credentials = gmail_credentials

    def notify_discord(self, title, description, color=0x00ff00, webhook_url=None):
        webhook = webhook_url or self.discord_webhook_url
        if not webhook:
            raise ValueError("Discord webhook URL is not set.")
        try:
            if color.startswith('#'):
                color = "0x" + color[1:]
            elif color.startswith('0x'):
                pass
            else:
                color = webcolors.name_to_hex(color)
                color = "0x" + color[1:]
        except:
            color = "#00ff00"
            color = "0x" + color[1:]
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "username": "ZO Notifier",
            "avatar_url": "https://media.licdn.com/dms/image/C4E0BAQHJUgN07GjmJQ/company-logo_200_200/0/1647259672635?e=2147483647&v=beta&t=4--RRBgN736z56CbZp-WdUnvUb3GN5zLeD-zz_PRfdM",
            "embeds": [{
                "title": title,
                "description": description + "\n\n",
                "color": int(color, 16),
                "fields": [{

                    "name": "Made by",
                    "value": "[Zero&One Developers](https://zodevelopers.com/)",
                    "inline": True
                }, ],
                "footer": {
                    "text": f"Sent at {timestamp}"
                },
            }]
            ,

        }
        response = requests.post(webhook, json=data)
        return response.status_code

    def notify_email(self, recipient_email, subject, message, sender_email=None, smtp_server=None, smtp_port=None,
                     smtp_username=None, smtp_password=None):
        if self.gmail_credentials:
            sender_email = sender_email or self.gmail_credentials['email']
            smtp_server = smtp_server or self.gmail_credentials['smtp_server']
            smtp_port = smtp_port or self.gmail_credentials['smtp_port']
            smtp_username = smtp_username or self.gmail_credentials['username']
            smtp_password = smtp_password or self.gmail_credentials['password']

        if not all([sender_email, smtp_server, smtp_port, smtp_username, smtp_password]):
            raise ValueError("Email credentials are not fully set.")

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()

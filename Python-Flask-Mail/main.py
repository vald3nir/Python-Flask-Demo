import os

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Google Config
# https://myaccount.google.com/lesssecureapps?pli=1
# https://accounts.google.com/b/0/DisplayUnlockCaptcha
# https://www.twilio.com/blog/2018/03/send-email-programmatically-with-gmail-python-and-flask.html

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['vald3nir@gmail.com'],
    "MAIL_PASSWORD": os.environ['87831151']
}

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
    with app.app_context():
        msg = Message(
            subject="Hello",
            sender=app.config.get("MAIL_USERNAME"),
            recipients=["valdenirseverino2010@edu.unifor.br"],
            body="This is a test email I sent with Gmail and Python!"
        )
        mail.send(msg)

from flask_mail import Mail,Message
from user.verify.emailverify import get_my_item
import random
def sendverifycode(subject,email,time = 60):
    verifycode = str(random.randint(100000, 999999))
    mail = Mail()
    message = Message(subject=subject,
                      recipients=[email],
                      body=verifycode)
    get_my_item(email,verifycode,time)
    mail.send(message)

def sendinfo(subject,email,body):
    mail = Mail()
    message = Message(subject=subject,
                      recipients=[email],
                      body=body)
    mail.send(message)
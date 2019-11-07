import random
from flask_mail import Mail,Message

def sendemail(email):
    verifycode = str(random.randint(100000,999999))
    mail = Mail()
    message = Message(subject="图书馆注册验证码",
                      recipients=[email],
                      body=verifycode)
    mail.send(message)
    return verifycode

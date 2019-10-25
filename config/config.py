#encoding:utf-8
from datetime import timedelta
import os

# 邮箱
class email_config():
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = "587"
    MAIL_USE_TLS = True
    MAIL_USERNAME = "374652530@qq.com"
    MAIL_PASSWORD = "qjrlnuwjzbjicadd"
    MAIL_DEFAULT_SENDER = "374652530@qq.com"



# session
class session_config():
    SECRET_KEY = os.urandom(24)
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)


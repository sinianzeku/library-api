#encoding:utf-8
from datetime import timedelta
import os

# 邮箱
class email_config():
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = "587"
    MAIL_USE_TLS = True
    MAIL_USERNAME = "374652530@qq.com"
    MAIL_PASSWORD = "qjrlnuwjzbjicadd" #生成的授权码
    MAIL_DEFAULT_SENDER = "374652530@qq.com"
    # MAIL_SERVER	localhost	电子邮件服务器的主机名或IP地址
    # MAIL_PORT	587	电子邮件服务器的端口
    # MAIL_USE_TLS	False	启用传输层安全协议
    # MAIL_USE_SSL	False	启用安全套接层协议
    # MAIL_USERNAME	None	邮件账户的用户名
    # MAIL_PASSWORD	None	邮件账户的密码


# session
class session_config():
    SECRET_KEY = os.urandom(24)
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

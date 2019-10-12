from config import mail_config

from flask_mail import Mail
from flask import Flask,session
from flask_cors import *
import api
import os
from datetime import timedelta

# import os
# path = os.path.dirname(__file__)

mail = Mail()

app = Flask(__name__)
app.config.from_object(mail_config)
mail.init_app(app)

app.config['SECRET_KEY']=os.urandom(24)   #设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7) #设置session的保存时间。

app.register_blueprint(api.user.view.user, url_prefix ="/user")
CORS(app, supports_credentials=True)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
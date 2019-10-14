from config import mail_config

from flask_mail import Mail
from flask import Flask
from flask_cors import *
import api


mail = Mail()

app = Flask(__name__)
app.config.from_object(mail_config)
mail.init_app(app)

app.register_blueprint(api.user.view.user, url_prefix = "/user")
app.register_blueprint(api.book.view.book, url_prefix = "/book")
CORS(app, supports_credentials=True)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
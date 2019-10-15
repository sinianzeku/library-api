from config import email_config
import user,book,user_activity
from flask_mail import Mail
from flask import Flask
from flask_cors import *

mail = Mail()

app = Flask(__name__)
app.config.from_object(email_config)
mail.init_app(app)

app.register_blueprint(user.view.user, url_prefix ="/user")
app.register_blueprint(book.view.book, url_prefix ="/book")
app.register_blueprint(user_activity.view.user_activity, url_prefix ="/user_activity")

CORS(app, supports_credentials=True)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
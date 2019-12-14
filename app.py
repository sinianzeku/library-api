from config import config
import user, user_activity, administrators
from flask_mail import Mail
from flask import Flask
from flask_cors import *

mail = Mail()
app = Flask(__name__)

app.config.from_object(config.email_config)
app.config.from_object(config.session_config)
mail.init_app(app)

app.register_blueprint(user.user_private.view.user, url_prefix="/user")
app.register_blueprint(user.user_public.view.user, url_prefix="/user")
app.register_blueprint(user_activity.activity_public.view.user_activity, url_prefix="/user_activity")
app.register_blueprint(user_activity.activity_private.view.user_activity, url_prefix="/user_activity")
app.register_blueprint(administrators.manage_info.view.admin, url_prefix="/admin")
app.register_blueprint(administrators.book.view.book, url_prefix="/book")

CORS(app, supports_credentials=True)

if __name__ == "__main__":
    app.logger.info("my first logging")
    app.run(debug=True, host="0.0.0.0", port=5000)

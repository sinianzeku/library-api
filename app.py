from flask import Flask
from flask_cors import *
import api

app = Flask(__name__)

app.register_blueprint(api.user.view.user, url_prefix ="/user")
CORS(app, supports_credentials=True)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
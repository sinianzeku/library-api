from flask import Blueprint,jsonify,request
from models.user import UserRegister
from db.user import into_register_info
import json

user = Blueprint("user",__name__)

@user.route("register",methods = ["post"])
def user_register():
    data = json.loads(request.get_data("").decode("utf-8"))
    username = data["username"]
    password = data["password"]
    user = UserRegister(username,password)
    password_result = user.password
    username_result = user.username
    if not username_result[0]:
        return jsonify({"status": -1, "message": username_result[1]})
    if not password_result[0]:
        return jsonify({"status": -1, "message": password_result[1]})
    into_resutl = into_register_info(username_result[1],password_result[1])
    if not into_resutl[0]:
        return jsonify({"status": -1, "message": into_resutl[1]})
    return jsonify({"status": 0, "message": "注册成功"})


@user.route("login",methods = ["post"])
def user_login():
    return jsonify({"status":0,"message":"login success"})


@user.route("UpdatePassword",methods = ["post"])
def user_change_password():
    return jsonify({"status":0,"message":"update  password success"})


@user.route("UpdateInformation",methods = ["post"])
def user_update_information():
    return jsonify({"status":0,"message":"undate information success"})


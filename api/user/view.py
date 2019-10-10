from flask import Blueprint,jsonify

user = Blueprint("user",__name__)

@user.route("register",methods = ["post"])
def UserRegister():
    return jsonify({"status":0,"message":"register success"})


@user.route("login",methods = ["post"])
def UserLogin():
    return jsonify({"status":0,"message":"login success"})


@user.route("UpdatePassword",methods = ["post"])
def UserChangePassword():
    return jsonify({"status":0,"message":"update  password success"})


@user.route("UpdateInformation",methods = ["post"])
def UserUpdateInformation():
    return jsonify({"status":0,"message":"undate information success"})


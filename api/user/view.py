from flask import Blueprint,jsonify,request,session,escape
from models.user import UserRegister
from db.user import into_register_info,user_login
from flask_mail import Mail,Message
import json,random
from models.emailverify import dict_Verify

user = Blueprint("user",__name__)

@user.route("register",methods = ["post"])
def user_verify_register():
    try:
        data = json.loads(request.get_data("").decode("utf-8"))
        username = data["username"]
        password = data["password"]
        cpassword = data["cpassword"]
        verifycode = data["verifycode"]
        email = data["email"]

        if password != cpassword:
            return jsonify({"status": -1, "message": "两次密码不一致"})

        user = UserRegister(username,password)
        password_result = user.password
        username_result = user.username

        if email and verifycode != dict_Verify[email]:
            return jsonify({"status": -1, "message": "验证码错误"})
        if not username_result[0]:
            return jsonify({"status": -1, "message": username_result[1]})
        if not password_result[0]:
            return jsonify({"status": -1, "message": password_result[1]})
        into_resutl = into_register_info(username_result[1],password_result[1])
        if not into_resutl[0]:
            return jsonify({"status": -1, "message": into_resutl[1]})
        return jsonify({"status": 0, "message": into_resutl[1]})
    except:
        return jsonify({"status": -1, "message": "服务器出错"})

@user.route("email_verify",methods = ["post"])
def email_verify():
    try:
        data = json.loads(request.get_data("").decode("utf-8"))
        email = data["email"]
        verifycode = str(random.randint(100000,999999))
        mail = Mail()
        message = Message(subject="验证码",
                          recipients=[email],
                          body=verifycode)
        dict_Verify[email] = verifycode
        mail.send(message)
        return jsonify({"status": 0, "message": "验证码发送成功"})
    except:
        return jsonify({"status": -1, "message": "验证码发送失败"})


@user.route("login",methods = ["post"])
def user_verify_login():
    try:
        data = json.loads(request.get_data("").decode("utf-8"))
        username = data["username"]
        password = data["password"]
        user = UserRegister(username,password)
        username_result = user.username
        password_result = user.password
        if not username_result[0]:
            return jsonify({"status": -1, "message": username_result[1]})
        if not password_result[0]:
            return jsonify({"status": -1, "message": "密码错误"})
        into_resutl = user_login(username_result[1],password_result[1])
        if not into_resutl[0]:
            return jsonify({"status": -1, "message": into_resutl[1]})
        if "username"in session :
            return jsonify({"status": -1, "message": "用户已经登入"})
        session["username"] = username
        return jsonify({"status": 0, "message": into_resutl[1],"data":escape(session['username'])})
    except:
        return jsonify({"status": -1, "message": "服务器出错"})


@user.route("logout", methods = ["post"])
def logout():
    session.pop("username",None)
    return jsonify({"status": 0, "message": "退出成功"})

@user.route("UpdatePassword",methods = ["post"])
def user_change_password():
    return jsonify({"status":0,"message":"update  password success"})


@user.route("UpdateInformation",methods = ["post"])
def user_update_information():
    return jsonify({"status":0,"message":"undate information success"})


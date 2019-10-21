from flask import Blueprint,jsonify,request,session
from user.verify.userverify import UserVerify
from user.db.db_user import into_register_info,user_login
from flask_mail import Mail,Message
import json,random
from user.verify.emailverify import dict_Verify

user = Blueprint("user_public",__name__)


"""
注册
邮箱验证
登入
"""

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
        user = UserVerify(username,
                            password)
        password_result = user.password
        username_result = user.username
        if email not in dict_Verify.keys() or verifycode != dict_Verify[email]:
            return jsonify({"status": -1, "message": "验证码错误"})
        if not username_result[0]:
            return jsonify({"status": -1, "message": username_result[1]})
        if not password_result[0]:
            return jsonify({"status": -1, "message": password_result[1]})
        into_resutl = into_register_info(username_result[1],
                                         password_result[1],
                                         email)
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
        username = 'zpgzpg'
        password = '1234567'
        # customer_type = data["customer_type"]
        user = UserVerify(username,password)
        username_result = user.username
        password_result = user.password
        if not username_result[0]:
            return jsonify({"status": -1, "message": username_result[1]})
        if not password_result[0]:
            return jsonify({"status": -1, "message": password_result[1]})
        verify_resutl = user_login(username_result[1],password_result[1])
        if not verify_resutl[0]:
            return jsonify({"status": -1, "message": verify_resutl[1]})
        session["username"] = username
        session["user_id"] = verify_resutl[1]
        session.permanent = True
        return jsonify({"status": 0, "message": "success"})
    except:
        return jsonify({"status": -1, "message": "服务器出错"})


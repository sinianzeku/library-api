from flask import Blueprint,jsonify,request,session
from user.verify.userverify import UserVerify
from user.db.db_user import into_register_info,user_login
from flask_mail import Mail,Message
import json,random
from user.verify.emailverify import get_my_item


user = Blueprint("user_public",__name__)



@user.route("register",methods = ["post"])
def user_verify_register():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_account = data["useraccount"]
    user_phone = data["userphone"]
    username = data["username"]
    password = data["password"]
    cpassword = data["cpassword"]
    verifycode = data["verifycode"]
    email = data["email"]
    if password != cpassword:
        return jsonify({"status": -1, "message": "两次密码不一致"})
    user = UserVerify()
    username_result = user.username(username)
    if not username_result[0]:
        return jsonify({"status": -1, "message": username_result[1]})
    password_result = user.password(password)
    if not password_result[0]:
        return jsonify({"status": -1, "message": password_result[1]})
    if  verifycode != get_my_item(email):
        return jsonify({"status": -1, "message": "验证码错误"})
    into_resutl = into_register_info(user_account,
                                     user_phone,
                                     username_result[1],
                                     password_result[1],
                                     email)
    if not into_resutl[0]:
        return jsonify({"status": -1, "message": into_resutl[1]})
    return jsonify({"status": 0, "message": into_resutl[1]})



@user.route("email_verify",methods = ["post"])
def email_verify():
    data = json.loads(request.get_data("").decode("utf-8"))
    email = data["email"]
    verifycode = str(random.randint(100000,999999))
    mail = Mail()
    message = Message(subject="图书馆注册验证码",
                      recipients=[email],
                      body=verifycode)
    get_my_item(email,verifycode)
    mail.send(message)
    return jsonify({"status": 0, "message": "验证码发送成功"})


@user.route("login",methods = ["post","get"])
def user_verify_login():
    data = json.loads(request.get_data("").decode("utf-8"))
    username = data["username"]
    password = data["password"]
    # code = data["code"]#admin:1     user:0
    code = 0
    user = UserVerify()
    username_result = user.username(username)
    password_result = user.password(password)
    if not username_result[0]:
        return jsonify({"status": -1, "message": username_result[1]})
    if not password_result[0]:
        return jsonify({"status": -1, "message": password_result[1]})
    verify_resutl = user_login(username_result[1],password_result[1],code)
    if not verify_resutl[0]:
        return jsonify({"status": -1, "message": verify_resutl[1]})
    session["username"] = username
    session["id"] = verify_resutl[1]
    return jsonify({"status": 0, "message": "success"})



from flask import Blueprint,jsonify,session,request
import json
from user.db.db_user import sql_feedbacks,sql_verify_old_password,sql_update_password,sql_update_info
from user.module.module import save_feedbacks
from user.verify import userverify

user = Blueprint("user_private",__name__)

@user.before_request
def before_user():
    if 'username' not in session:
        print(session)
        return jsonify({"status": -1, "message": "未登入"})



@user.route("get_session")
def get_session():
    session
    return jsonify({"status":0})


@user.route("feedback",methods = ["post"])
def feedback():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_id = session["user_id"]
    feedbacks = data["feedbacks"]
    reader = data["reader"]
    phone = data["phone"]
    path = save_feedbacks(feedbacks,reader)
    result = sql_feedbacks(user_id,reader,phone,path)
    if not result:
        return jsonify({"status":-1,"message":"fail"})
    return jsonify({"status":0,"message":"success"})


@user.route("update_password", methods = ["post"])
def update_password():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_account = session["username"]
    old_password = data["old_password"]
    new_password = data["new_password"]
    new_cpassword = data["new_cpassword"]
    verify_password = userverify.password_encryption(old_password)
    result = sql_verify_old_password(user_account,verify_password)
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    if new_password != new_cpassword:
        return jsonify({"status":-1,"meaasge":"两次密码输入不一致"})
    ver = userverify.UserVerify()
    password = ver.password(new_password)
    if not password[0]:
        return jsonify({"status":-1,"message":password[1]})
    result = sql_update_password(user_account,password[1])
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":"success"})


@user.route("update_info",methods = ["post"])
def update_info():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_id = session["id"]
    email = data["email"]
    phone = data["phone"]
    address = data["address"]
    result = sql_update_info(user_id,email,phone,address)
    return jsonify({"status":0,"message":"success"})



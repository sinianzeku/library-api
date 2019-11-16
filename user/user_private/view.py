from flask import Blueprint, jsonify, request
from module import token
from user.db import db_user
from user.verify import userverify
from administrators.book.db_book import sql_query_user_id
from user.verify.emailverify import get_my_item
from module.activity_set import Condition
from module.send_email import sendverifycode as se
import json

user = Blueprint("user_private", __name__)


# 意见反馈
@user.route("feedback", methods=["post"])
def feedback():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_name = data["user_name"]
    feedbacks = data["feedbacks"]
    reader = data["reader"]
    phone = data["phone"]
    tokens = data["tokens"]
    if not token.certify_token(user_name, tokens):
        return jsonify({"status": -1, "message": "not login", "data": ""})
    user_id = sql_query_user_id(user_name)
    result = db_user.sql_feedbacks(user_id, reader, phone, feedbacks)
    if not result:
        return jsonify({"status": -1, "message": "fail"})
    return jsonify({"status": 0, "message": "success"})


# 自动获取反馈信息
@user.route("get_feedback", methods=["post"])
def get_feedback():
    data = json.loads(request.get_data("").decode("utf-8"))
    if not data["user_name"]:
        return jsonify({"status": -1, "message": "fail"})
    user_name = data["user_name"]
    user_id = sql_query_user_id(user_name)
    result = db_user.sql_get_feedback(user_id)
    if not result[0]:
        return jsonify({"status": -1, "message": "fail"})
    C = Condition()
    if result[1]:
        for i in range(len(result[1])):
            result[1][i]["state"] = C.feed(result[1][i]["state"])
    return jsonify({"status": 0, "message": "success", "data": result[1]})


# 更新密码
@user.route("update_password", methods=["post"])
def update_password():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_account = data["user_account"]
    old_password = data["old_password"]
    new_password = data["new_password"]
    new_cpassword = data["new_cpassword"]
    verify_password = userverify.password_encryption(old_password)
    result = db_user.sql_verify_old_password(user_account, verify_password)
    if not result[0]:
        return jsonify({"status": -1, "message": result[1]})
    if new_password != new_cpassword:
        return jsonify({"status": -1, "message": "两次密码输入不一致"})
    ver = userverify.UserVerify()
    password = ver.password(new_password)
    if not password[0]:
        return jsonify({"status": -1, "message": password[1]})
    result = db_user.sql_update_password(user_account, password[1])
    if not result[0]:
        return jsonify({"status": -1, "message": result[1]})
    return jsonify({"status": 0, "message": "success"})


# 发送验证码
@user.route("update_info_email_verify", methods=["post"])
def update_info_email_verify():
    data = json.loads(request.get_data("").decode("utf-8"))
    email = data["email"]
    subject = '图书馆更新密码验证码'
    se(subject, email, 60)
    return jsonify({"status": 0, "message": "验证码发送成功"})


# 查看个人信息
@user.route("query_user_info", methods=["post"])
def query_user_info():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_account = data["user_account"]
    tokens = data["tokens"]
    if not token.certify_token(user_account, tokens):
        return jsonify({"status": -1, "message": "not login", "data": ""})
    user_id = sql_query_user_id(user_account)
    result = db_user.sql_query_user_info(user_id)
    C = Condition()
    result[1][0]['user_sex'] = C.sex(result[1][0]['user_sex'])
    if not result:
        return jsonify({"status": -1, "message": "fail"})
    return jsonify({"status": 0, "message": "success", "data": result[1]})


# 修改个人信息
@user.route("update_info", methods=["post"])
def update_info():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_account = data["user_account"]
    user_name = data["user_name"]
    user_sex = data["user_sex"]
    email = data["email"]
    phone = data["phone"]
    verifycode = data["verifycode"]
    if verifycode != get_my_item(email):
        return jsonify({"status": -1, "message": "验证码错误"})
    db_user.sql_update_info(user_account, user_name, user_sex, email, phone)
    return jsonify({"status": 0, "message": "success"})

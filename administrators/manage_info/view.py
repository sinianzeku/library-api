from flask import Blueprint,jsonify,request
from user.verify.userverify import UserVerify
from administrators.manage_info.db_manage import sql_add_manager,sql_query_user_info,sql_query_book_info,sql_add_book_category
import json

admin = Blueprint("admin",__name__)

@admin.route("add_manager",methods = ["post"])
def add_manager():
    data = json.loads(request.get_data("").decode("utf-8"))
    work_id = data["work_id"]
    worker_name = data["worker_name"]
    work_passwords = data["work_password"]
    user = UserVerify()
    work_password = user.password(work_passwords)
    if not work_password[0]:
        return jsonify({"status":-1,"message":"密码格式错误"})
    result = sql_add_manager(work_id,worker_name,work_password[1])
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":result[1]})


@admin.route("query_user_info",methods = ["post"])
def query_user_info():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_name = data["user_name"]
    result = sql_query_user_info(user_name)
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":"success","data":result[1]})


@admin.route("query_book_info",methods = ["post"])
def query_book_info():
    data = json.loads(request.get_data("").decode("utf-8"))
    book_name = data["book_name"]
    result = sql_query_book_info(book_name)
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":"success","data":result[1]})


@admin.route("add_book_category",methods = ["post"])
def add_book_category():
    data = json.loads(request.get_data("").decode("utf-8"))
    category1 = data["category1"]
    category2 = data["category2"]
    result = sql_add_book_category(category1,category2)
    if not result[0]:
        return jsonify({"status": -1, "message": result[1]})
    return jsonify({"status": 0, "message": "success"})

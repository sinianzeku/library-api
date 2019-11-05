from flask import Blueprint,jsonify,request
from user.verify.userverify import UserVerify
from administrators.manage_info import db_manage
from administrators.book.db_book import sql_query_user_id
import json
import  os

admin = Blueprint("admin",__name__)

#增加管理员
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
    result = db_manage.sql_add_manager(work_id,worker_name,work_password[1])
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":result[1]})


#查询借书者信息
@admin.route("query_user_info",methods = ["post"])
def query_user_info():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_name = ''
    if "user_name" in data:
        user_name = data["user_name"]
    result = db_manage.sql_query_user_info(user_name)
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":"success","data":result[1]})


#借-查询被借书籍信息
@admin.route("query_borrow_book_info",methods = ["post"])
def query_borrow_book_info():
    data = json.loads(request.get_data("").decode("utf-8"))
    book_name = ""
    if "book_name" in data:
        book_name = data["book_name"]
    result = db_manage.sql_query_book_info_0(book_name)
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    for i in range(len(result[1])):
        result[1][i]["book_img_path"] = os.path.abspath('.')+'/data/img/book-010.png'
    return jsonify({"status":0,"message":"success","data":result[1]})

#还-查询被借书籍信息
@admin.route("query_return_book_info",methods = ["post"])
def query_return_book_info():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_name = data["user_name"]
    book_name = data["book_name"]
    user_id = sql_query_user_id(user_name)
    result = db_manage.sql_query_book_info_1(book_name,user_id)
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    for i in range(len(result[1])):
        result[1][i]["book_img_path"] = os.path.abspath('.')+'/data/img/book-010.png'
    return jsonify({"status":0,"message":"success","data":result[1]})

#增加书籍类别
@admin.route("add_book_category",methods = ["post"])
def add_book_category():
    data = json.loads(request.get_data("").decode("utf-8"))
    category1 = data["category1"]
    category2 = data["category2"]
    result = db_manage.sql_add_book_category(category1,category2)
    if not result[0]:
        return jsonify({"status": -1, "message": result[1]})
    return jsonify({"status": 0, "message": "success"})


@admin.route("user_info",methods = ["post"])
def user_info():
    result = db_manage.sql_user_info()
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    return jsonify({"status":0,"message":"success","data":result[1]})

@admin.route("conditional_user_info",methods = ["post"])
def conditional_user_info():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_name = data["user_name"]
    result = db_manage.sql_conditional_user_info(user_name)
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    return jsonify({"status":0,"message":"success","data":result[1]})

@admin.route("delete_user",methods = ["post"])
def delete_user():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_name = data["user_name"]
    result = db_manage.sql_delete_user(user_name)
    if not result[0]:
        return jsonify({"status": 0, "message": "success"})
    return jsonify({"status":0,"message":"success"})

@admin.route("book_info",methods = ["post"])
def book_info():
    result = db_manage.sql_book_info()
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    state = {
        "0":"在馆",
        "1":"已借出"
    }
    for i in range(len(result[1])):
        result[1][i]["book_state"] = state[result[1][i]["book_state"]]
    return jsonify({"status":0,"message":"success","data":result[1]})


@admin.route("conditional_book_info",methods = ["post"])
def conditional_book_info():
    data = json.loads(request.get_data("").decode("utf-8"))
    book_id = data["book_id"]
    result = db_manage.sql_conditional_book_info(book_id)
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    state = {
        "0":"在馆",
        "1":"已借出"
    }
    for i in range(len(result[1])):
        result[1][i]["book_state"] = state[result[1][i]["book_state"]]
    return jsonify({"status":0,"message":"success","data":result[1]})

@admin.route("borrowing_book",methods = ["post"])
def borrowing_book():
    result = db_manage.sql_borrowing_book()
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    return jsonify({"status":0,"message":"success","data":result[1]})








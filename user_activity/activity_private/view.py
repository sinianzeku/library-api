from flask import Blueprint,jsonify,request
from user_activity.db import db_user_activity
from administrators.book.db_book import sql_query_user_id
from module.send_email import sendinfo
from module import token
import json

user_activity = Blueprint("activity_private",__name__)


@user_activity.route("count_book", methods=["post"])
def count_book():
    data = json.loads(request.get_data("").decode("utf-8"))
    if not data["user_account"]:
        return jsonify({"status": -1, "message": "fail", "data": []})
    account = data["user_account"]
    tokens = data["tokens"]
    if not token.certify_token(account, tokens):
        return jsonify({"status": -1, "message": "not login", "data": ""})
    user_id = sql_query_user_id(account)
    result = {}
    result["bookshelf"], result["borrowing"], result["borrow"] = db_user_activity.sql_count_book(user_id)
    return jsonify({"status": 0, "message": "success", "data": result})


#借书记录
@user_activity.route("borrowed_records", methods=["post"])
def borrowed_records():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_account = data["user_account"]
    tokens = data["tokens"]
    if not token.certify_token(user_account, tokens):
        return jsonify({"status": -1, "message": "not login", "data": ""})
    user_id = sql_query_user_id(user_account)
    result = db_user_activity.sql_borrowed_records(user_id)
    if not result[0]:
        return jsonify({"status": -1, "message": result[1]})
    return jsonify({"status": 0, "message": "success", "data": result[1]})


# 在借书籍
@user_activity.route("borrowing_books", methods=["post"])
def borrowing_books():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_account = data["user_account"]
    tokens = data["tokens"]
    if not token.certify_token(user_account, tokens):
        return jsonify({"status": -1, "message": "not login", "data": ""})
    user_id = sql_query_user_id(user_account)
    result = db_user_activity.sql_borrowing_books(user_id)
    if not result[0]:
        return jsonify({"status": -1, "message": result[1]})
    return jsonify({"status": 0, "message": "success", "data": result[1]})


# 我的书架
@user_activity.route("my_bookshelf", methods=["post"])
def my_bookshelf():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_account = data["user_account"]
    tokens = data["tokens"]
    if not token.certify_token(user_account, tokens):
        return jsonify({"status": -1, "message": "not login", "data": ""})
    user_id = sql_query_user_id(user_account)
    result = db_user_activity.sql_my_bookshelf(user_id)
    if not result[0]:
        return jsonify({"status": -1, "message": result[1]})
    return jsonify({"status": 0, "message": "success", "data": result[1]})


# 收藏书籍
@user_activity.route("collect_book", methods=["post"])
def collect_book():
    data = json.loads(request.get_data("").decode("utf-8"))
    book_id = data["book_id"]
    user_name = data["user_name"]
    result = db_user_activity.sql_collect_book(user_name, book_id)
    if not result[0]:
        return jsonify({"status": -1, "message": result[1]})
    return jsonify({"status": 0, "message": "success"})


# 三行情书活动
@user_activity.route("thematic_activities", methods=["post"])
def thematic_activities():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_name = data["user_name"]
    contestant = data["contestant"]
    phone = data["phone"]
    works = data["works"]
    email = data["email"]
    result = db_user_activity.sql_thematic_activities(contestant,phone,works,user_name)
    if not result[0]:
        return jsonify({"status": -1, "message":result[1]})
    subject="图书馆活动报名",
    body='您已成功报名图书馆‘三行情书’活动'
    sendinfo(subject,email,body)
    return jsonify({"status":0,"message":"success"})

#志愿服务活动
@user_activity.route("voluntary_activities",methods = ["post"])
def voluntary_activities():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_name = data["user_name"]
    contestant = data["contestant"]
    phone = data["phone"]
    email = data["email"]
    days = data["days"]
    times = data["times"]
    result = db_user_activity.sql_voluntary_activities(contestant,user_name,phone,email,days,times)
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    subject="图书馆活动报名"
    body='您已成功报名图书馆‘社会实践志愿服务’活动'
    sendinfo(subject, email, body)
    return jsonify({"status":0,"message":"success"})





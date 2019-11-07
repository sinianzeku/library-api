from flask import Blueprint,jsonify,session,request
from user_activity.db import db_user_activity
from flask_mail import Mail,Message

user_activity = Blueprint("activity_private",__name__)
import json
# @user_activity.before_request
# def before_user():
#     if 'username' not in session:
#         return jsonify({"status": -1, "message": "未登入"})

#借书记录
@user_activity.route("borrowed_records", methods = ["post"])
def borrowed_records():
    user_id = session["id"]
    result = db_user_activity.sql_borrowed_records(user_id)
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":"success","data":result[1]})

#在借书籍
@user_activity.route("borrowing_books", methods = ["post"])
def borrowing_books():
    user_id = session["id"]
    result = db_user_activity.sql_borrowing_books(user_id)
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":"success","data":result[1]})

#我的书架
@user_activity.route("my_bookshelf", methods = ["post"])
def my_bookshelf():
    user_id = session["id"]
    result = db_user_activity.sql_my_bookshelf(user_id)
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":"success","data":result[1]})

#收藏书籍
@user_activity.route("collect_book",methods = ["post"])
def collect_book():
    data = json.loads(request.get_data("").decode("utf-8"))
    book_id = data["book_id"]
    user_id = data["user_id"]
    result = db_user_activity.sql_collect_book(user_id,book_id)
    if not result[0]:
        return jsonify({"status":0,"message":"fail"})
    return jsonify({"status":0,"message":"success"})

#三行情书活动
@user_activity.route("thematic_activities",methods=["post"])
def thematic_activities():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_id = session['id']
    contestant = data["contestant"]
    phone = data["phone"]
    works = data["works"]
    result = db_user_activity.sql_thematic_activities(contestant,phone,works)
    if not result[0]:
        return jsonify({"status":0,"message":"fail"})
    email = db_user_activity.sql_email(user_id)
    mail = Mail()
    message = Message(subject="图书馆活动报名",
                      recipients=[email],
                      body='您已成功报名图书馆‘三行情书’活动')
    mail.send(message)
    return jsonify({"status":0,"message":"success"})

#志愿服务活动
@user_activity.route("voluntary_activities",methods = ["post"])
def voluntary_activities():
    data = json.loads(request.get_data("").decode("utf-8"))
    contestant = data["contestant"]
    phone = data["phone"]
    email = data["email"]
    time_of_appointment_start = data["time_of_appointment_start"]
    time_of_appointment_end = data["time_of_appointment_end"]
    if time_of_appointment_start > time_of_appointment_end:
        return jsonify({"status": -1, "message": "起始时间不能大于结束时间"})
    result = db_user_activity.sql_voluntary_activities(contestant,phone,email,time_of_appointment_start,time_of_appointment_end)
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    mail = Mail()
    message = Message(subject="图书馆活动报名",
                      recipients=[email],
                      body='您已成功报名图书馆‘社会实践志愿服务’活动')
    mail.send(message)
    return jsonify({"status":0,"message":"success"})
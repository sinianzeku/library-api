from flask import Blueprint,jsonify,session,request
from user_activity.db import db_user_activity
user_activity = Blueprint("activity_private",__name__)
import json
@user_activity.before_request
def before_user():
    if 'username' not in session:
        return jsonify({"status": -1, "message": "未登入"})


@user_activity.route("borrowed_records", methods = ["post"])
def borrowed_records():
    user_id = session["id"]
    result = db_user_activity.sql_borrowed_records(user_id)
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":"success","data":result[1]})


@user_activity.route("borrowing_books", methods = ["post"])
def borrowing_books():
    user_id = session["id"]
    result = db_user_activity.sql_borrowing_books(user_id)
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":"success","data":result[1]})


@user_activity.route("my_bookshelf", methods = ["post"])
def my_bookshelf():
    user_id = session["id"]
    result = db_user_activity.sql_my_bookshelf(user_id)
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":"success","data":result[1]})

@user_activity.route("collect_book",methods = ["post"])
def collect_book():
    data = json.loads(request.get_data("").decode("utf-8"))
    book_id = data["book_id"]
    user_id = session["id"]
    result = db_user_activity.sql_collect_book(user_id,book_id)
    if not result[0]:
        return jsonify({"status":0,"message":"fail"})
    return jsonify({"status":0,"message":"success"})



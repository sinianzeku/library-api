from flask import Blueprint,request,jsonify
from . import db_user_activity
import json
user_activity = Blueprint("user_activity",__name__)

@user_activity.route("book_enquiry",methods = ["post"])
def book_enquiry():
    try:
        data = json.loads(request.get_data("").decode("utf-8"))
        txt = data["txt"]
        query_mode = data["query_mode"]
        result = db_user_activity.search_book(query_mode,txt)
        if not result[0]:
            return jsonify({"status": -1, "massage": "失败", "data": result[1]})
        return jsonify({"status":"0","massage":"成功","data":result[1]})
    except:
        return jsonify({"status": -1, "massage": "失败", "data": "服务器出错"})

@user_activity.route("query_book_info",methods = ["post"])
def query_book_info():
    try:
        data = json.loads(request.get_data("").decode("utf-8"))
        book_name = data["book_name"]
        book_auther = data["book_auther"]
        book_publisher = data["book_publisher"]
        book_category_name = data["book_category_name"]

        result = db_user_activity.search_book_info(book_name,
                                                   book_auther,
                                                   book_publisher,
                                                   book_category_name)
        if not result[0]:
            return jsonify({"status":-1,"massage":"失败","data":result[1]})
        return jsonify({"status":-1,"massage":"成功","data":result[1]})
    except:
        return jsonify({"status":-1,"massage":"失败"})



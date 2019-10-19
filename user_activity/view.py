from flask import Blueprint,request,jsonify
from . import db_user_activity
import json
user_activity = Blueprint("user_activity",__name__)


@user_activity.route("query_book",methods = ["post"])
def book_enquiry():
    try:
        data = json.loads(request.get_data("").decode("utf-8"))
        txt = data["txt"]
        query_mode = data["query_mode"]
        result = db_user_activity.search_book(query_mode,txt)
        if not result[0]:
            return jsonify({"status": -1, "massage": "fail", "data": result[1]})
        return jsonify({"status":"0","massage":"success","data":result[1]})
    except:
        return jsonify({"status": -1, "massage": "fail", "data": "Server error"})

@user_activity.route("query_book_info",methods = ["post"])
def query_book_info():
    try:
        data = json.loads(request.get_data("").decode("utf-8"))
        book_id = data["book_id"]
        result = db_user_activity.search_book_info(book_id)
        if not result[0]:
            return jsonify({"status":-1,"massage":"fail","data":result[1]})
        return jsonify({"status":-1,"massage":"success","data":result[1]})
    except:
        return jsonify({"status":-1,"massage":"fail","data": "Server error"})



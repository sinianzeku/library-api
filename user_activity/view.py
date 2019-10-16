from flask import Blueprint,request,jsonify
from .db_user_activity import search_book
import json
user_activity = Blueprint("user_activity",__name__)

@user_activity.route("book_enquiry",methods = ["post"])
def book_enquiry():
    try:
        data = json.loads(request.get_data("").decode("utf-8"))
        txt = data["txt"]
        query_mode = data["query_mode"]
        result = search_book(query_mode,txt)
        if not result[0]:
            return jsonify({"status": -1, "massage": "失败", "data": result[1]})
        return jsonify({"status":"0","massage":"成功","data":result})
    except:
        return jsonify({"status": -1, "massage": "失败", "data": "服务器出错"})



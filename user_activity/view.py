from flask import Blueprint,request
import json
user_activity = Blueprint("user_activity",__name__)

@user_activity.route("book_enquiry",methods = ["psot"])
def book_enquiry():
    data = json.loads(request.get_data("").decode("utf-8"))
    txt = data["text"]
    query_mode = data["query_mode"]




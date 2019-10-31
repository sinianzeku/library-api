from flask import Blueprint,request,jsonify
from user_activity.db import db_user_activity
import json
from config.defaulttime import set_time
user_activity = Blueprint("activity_public",__name__)


@user_activity.route("query_book",methods = ["post"])
def query_book():
    data = json.loads(request.get_data("").decode("utf-8"))
    txt = data["txt"]
    query_mode = data["query_mode"]
    result = db_user_activity.sql_query_book(query_mode, txt)
    if not result[0]:
        return jsonify({"status": -1, "massage": "fail", "data": result[1]})
    return jsonify({"status":"0","massage":"success","data":result[1]})


@user_activity.route("query_book_info",methods = ["post"])
def query_book_info():
    data = json.loads(request.get_data("").decode("utf-8"))
    book_id = data["book_id"]
    result = db_user_activity.sql_query_book_info(book_id)
    if not result[0]:
        return jsonify({"status":-1,"massage":"fail","data":result[1]})
    return jsonify({"status":-1,"massage":"success","data":result[1]})


#热门推荐
@user_activity.route("popular_recommendation",methods = ["post"])
def popular_recommendation():
    data = json.loads(request.get_data("").decode("utf-8"))
    dict_time = {
        "week":["past",7],
        "month":["past",30],
        "season":["past",90],
        "half_a_year":["past",180],
        "year":["past",365]
    }
    st = set_time()
    today_time = st.today()
    past_time = st.time_frame(dict_time[data["time"]])

    result = db_user_activity.sql_popular_recommendation(today_time,past_time)
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    return jsonify({"status":0,"message":"success","data":result[1]})


#新书推荐
@user_activity.route("new_arrivals",methods = ["post"])
def new_arrivals():
    data = json.loads(request.get_data("").decode("utf-8"))
    dict_time = {
        "week":["past",7],
        "month":["past",30],
        "season":["past",90],
        "half_a_year":["past",180],
        "year":["past",365]
    }
    st = set_time()
    today_time = st.today()
    past_time = ''
    if "time" in data:
        past_time = st.time_frame(dict_time[data["time"]])
        print(today_time,past_time)
    result = db_user_activity.sql_new_arrivals(today_time,past_time)
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    return jsonify({"status":0,"message":"success","data":result[1]})


@user_activity.route("class_lookup",methods = ["post"])
def class_lookup():
    data = json.loads(request.get_data("").decode("utf-8"))
    language_dict = {
        "中文图书":0,
        "外文图书":1
    }
    category1 = ""
    category2 = ""
    language = ""
    if "category1" in data:
        category1 = data["category1"]
    if "category2" in data:
        category2 = data["category2"]
    if "language" in data:
        language = language_dict[data["language"]]
    result = db_user_activity.sql_class_lookup(category1,category2,language)
    if not result[0]:
        jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":"success","data":result[1]})





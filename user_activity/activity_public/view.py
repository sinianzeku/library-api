from flask import Blueprint,request,jsonify
from user_activity.db import db_user_activity
import json
from config.defaulttime import set_time
from user_activity.module.activity_set import Condition
import os

user_activity = Blueprint("activity_public",__name__)


#查找书籍
@user_activity.route("query_book",methods = ["post"])
def query_book():
    data = json.loads(request.get_data("").decode("utf-8"))
    dict_query_mode = {
        "书名":"book_name",
        "作者":"book_auther"
    }
    txt = data["txt"]
    query_mode = "book_name"
    if "query_mode" in data:
        query_mode = dict_query_mode[ data["query_mode"]]#
    result = db_user_activity.sql_query_book(query_mode, txt)
    dict_book_language = {
        "0":"中文图书",
        "1":"西文图书"
    }
    if not result[0]:
        return jsonify({"status": -1, "massage": "fail", "data": result[1]})
    for i in range(len(result[1])):
        result[1][i]["book_language"] = dict_book_language[result[1][i]["book_language"]]
    result1 =  db_user_activity.sql_add_key_works(txt,query_mode)
    if not result1:
        return jsonify({"status": -1, "massage": "fail"})
    return jsonify({"status":"0","massage":"success","data":result[1]})

#查询书籍详细信息
@user_activity.route("query_book_info",methods = ["post"])
def query_book_info():
    data = json.loads(request.get_data("").decode("utf-8"))
    book_id = data["book_id"]
    result = db_user_activity.sql_query_book_info(book_id)
    if not result[0]:
        return jsonify({"status":-1,"massage":"fail","data":result[1]})
    for i in range(len(result[1])):
        result[1][i]["book_img_path"] = os.path.abspath('.')+'/data/img/book-010.png'
    return jsonify({"status":-1,"massage":"success","data":result[1]})


@user_activity.route("book_name_query",methods = ['post'])
def book_name_query():
    data = json.loads(request.get_data("").decode("utf-8"))
    book_name = data['book_name']
    result = db_user_activity.sql_book_name_query(book_name)
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    return jsonify({"status":0,"message":"success","data":result[1]})

#热门推荐
@user_activity.route("popular_recommendation",methods = ["post"])
def popular_recommendation():
    data = json.loads(request.get_data("").decode("utf-8"))
    past_time = ''
    language = ''
    category1 = ''
    C = Condition()
    st = set_time()
    today_time = st.today()
    if "time" in data:
        past_time = st.time_frame(C.where_time(data["time"]))
    if "language" in data:
        language = C.language(data["language"])
    if "category1" in data:
        category1  = data["category1"]
    result = db_user_activity.sql_popular_recommendation(today_time,past_time,language,category1)
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    return jsonify({"status":0,"message":"success","data":result[1]})


#新书推荐
@user_activity.route("new_arrivals",methods = ["post"])
def new_arrivals():
    data = json.loads(request.get_data("").decode("utf-8"))
    past_time = ''
    language = ''
    category1 = ''
    C = Condition()
    st = set_time()
    today_time = st.today()
    if "time" in data:
        past_time = st.time_frame(C.where_time(data["time"]))
    if "language" in data:
        language = C.language(data["language"])
    if "category1" in data:
        category1 = data["category1"]
    result = db_user_activity.sql_new_arrivals(today_time,past_time,language,category1)
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    return jsonify({"status":0,"message":"success","data":result[1]})

#分类查询
@user_activity.route("class_lookup",methods = ["post"])
def class_lookup():
    data = json.loads(request.get_data("").decode("utf-8"))
    C = Condition()
    category1 = ""
    category2 = ""
    language = ""
    if "category1" in data:
        category1 = data["category1"]
    if "category2" in data:
        category2 = data["category2"]
    if "language" in data:
        language = C.language(data["language"])
    result = db_user_activity.sql_class_lookup(category1,category2,language)
    if not result[0]:
        jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":"success","data":result[1]})



#查找分类1数据
@user_activity.route("category1",methods=["post"])
def category1():
    result = db_user_activity.sql_category1()
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    return jsonify({'status':0,"message":"success","data":result[1]})
#查询分类2数据
@user_activity.route("category2",methods=["post"])
def category2():
    data = json.loads(request.get_data("").decode("utf-8"))
    category_1 = data["category1"]
    result = db_user_activity.sql_category2(category_1)
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    return jsonify({'status':0,"message":"success","data":result[1]})

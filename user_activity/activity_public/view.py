from flask import Blueprint,request,jsonify
from user_activity.db import db_user_activity
from flask_mail import Mail,Message
from user.verify.emailverify import get_my_item
from user.verify import userverify
from config.defaulttime import set_time
from module.activity_set import Condition
import os, random,json

user_activity = Blueprint("activity_public",__name__)


#查找书籍
@user_activity.route("query_book",methods = ["post"])
def query_book():
    C = Condition()
    data = json.loads(request.get_data("").decode("utf-8"))
    txt = data["txt"]
    query_mode = "book_name"
    if "query_mode" in data and data["query_mode"]:
        query_mode = C.books(data["query_mode"])
    result = db_user_activity.sql_query_book(query_mode, txt)
    if not result[0]:
        return jsonify({"status": -1, "massage": "fail", "data": result[1]})
    for i in range(len(result[1])):
        result[1][i]["book_language"] = C.language(result[1][i]["book_language"] )
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
    result[1][0]["book_category"] = db_user_activity.sql_query_category(result[1][0]["book_category"])
    C = Condition()
    result[1][0]["book_state"] = C.state(result[1][0]["book_state"])
    result[1][0]["book_language"] = C.language(result[1][0]["book_language"])
    if not result[0]:
        return jsonify({"status":-1,"massage":"fail","data":result[1]})
    for i in range(len(result[1])):
        result[1][i]["book_img_path"] = os.path.abspath('.')+'/data/img/book-010.png'
    return jsonify({"status":0,"massage":"success","data":result[1]})

#热门书籍信息
@user_activity.route("popular_book_info",methods = ['post'])
def popular_book_info():
    data = json.loads(request.get_data("").decode("utf-8"))
    book_id = data['book_id']
    result = db_user_activity.sql_book_name_query(book_id)
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

#热门推荐
@user_activity.route("aut_popular_recommendation",methods = ["post"])
def aut_popular_recommendation():
    result  = db_user_activity.sql_aut_popular_recommendation()
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

#新书推荐
@user_activity.route("aut_new_arrivals",methods = ["post"])
def aut_new_arrivals():
    result  = db_user_activity.sql_aut_new_arrivals()
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
    if "language" in data and data["language"]:
        language = C.language(data["language"])
    result = db_user_activity.sql_class_lookup(category1,category2,language)
    if not result[0]:
        jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":"success","data":result[1]})

#分类查询自动获取
@user_activity.route("aut_class_lookup",methods = ["post"])
def aut_class_lookup():
    result = db_user_activity.sql_aut_class_lookup()
    if not result[0]:
        jsonify({"status": -1, "message": result[1]})
    return jsonify({"status": 0, "message": "success", "data": result[1]})

#发送验证码
@user_activity.route("send_email",methods = ["post"])
def send_email():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_name = data["user_name"]
    sql_email = db_user_activity.sql_email(user_name)
    if not sql_email[0]:
        return jsonify({"status": -1, "message": sql_email[1]})
    email = sql_email[1]
    verifycode = str(random.randint(100000,999999))
    mail = Mail()
    message = Message(subject="图书馆找回密码验证码",
                      recipients=[email],
                      body=verifycode)
    get_my_item(email,verifycode)
    mail.send(message)
    return jsonify({"status": 0, "message": "验证码发送成功","data":email})


#验证码验证
@user_activity.route("verify_code",methods = ["post"])
def verify_code():
    data = json.loads(request.get_data("").decode("utf-8"))
    email = data["email"]
    verifycode = data["code"]
    if  verifycode != get_my_item(email):
        return jsonify({"status": -1, "message": "验证码错误"})
    return jsonify({"status": 0, "message": "success"})

#设置密码
@user_activity.route("make_password",methods = ["post"])
def make_password():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_name = data["user_name"]
    password = data["password"]
    cpassword = data["cpassword"]
    if password != cpassword:
        return jsonify({"status": -1, "message": "您输入的两次密码不一致"})
    ver = userverify.UserVerify()
    password = ver.password(password)
    if not password[0]:
        return jsonify({"status":-1,"message":password[1]})
    result = db_user_activity.sql_update_password(user_name,password[1])
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":"success"})



from flask import Blueprint,request,jsonify
from administrators.book import books
from administrators.book import db_book
import json

book = Blueprint("book",__name__)

#新书入馆
@book.route("new_book_entry",methods = ["POST"])
def new_book_entry():
    data = json.loads(request.get_data("").decode("utf-8"))
    NBE = books.NewBookEntry(data)
    NBE.language()
    result = NBE.query_book_category()#查询类别id
    if not result[0]:
        return jsonify({"status": -1, "message": result[1]})
    result = NBE.verify_book_code()#验证条码号是否存在
    if result:
        return jsonify({"status": -1, "message": "条码号已存在"})
    update_result = NBE.data_access_to_database()  # 存储数据
    if not update_result[0]:
        return jsonify({"status": -1, "message" : update_result[1]})
    return jsonify({"status" : 0, "message" : "success"})

#借书
@book.route("borrow_book",methods = ["post"])
def borrow_book():
    data = json.loads(request.get_data("").decode("utf-8"))
    book_id = data["book_id"]
    user_name = data["user_name"]
    user_id = db_book.sql_query_user_id(user_name)
    result = db_book.sql_borrow_book(user_id,book_id)
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    return jsonify({"status":0,"message":"success"})

@book.route("borrow_limit",methods = ["post"])
def borrow_limit():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_account = data["user_account"]
    user_id = db_book.sql_query_user_id(user_account)
    sum = db_book.sql_borrow_limit(user_id)
    if sum ==7 :
        return jsonify({"status": -1, "message": "该用户借书数量已达7本，借书失败"})
    return jsonify({"status": 0, "message": "success"})
#还书
@book.route("return_book",methods = ["post"])
def return_book():
    data = json.loads(request.get_data("").decode("utf-8"))
    book_id = data["book_id"]
    user_name = data["user_name"]
    user_id = db_book.sql_query_user_id(user_name)
    result = db_book.sql_return_book(book_id,user_id)
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    return jsonify({"status":0,"message":"success"})







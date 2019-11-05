from flask import Blueprint,request,jsonify
from administrators.book import books
from administrators.book.db_book import sql_borrow_book,sql_return_book,sql_query_user_id,sql_query_borrower,sql_query_book
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
    user_id = sql_query_user_id(user_name)
    result = sql_borrow_book(user_id,book_id)
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    return jsonify({"status":0,"message":"success"})

#还书
@book.route("return_book",methods = ["post"])
def return_book():
    data = json.loads(request.get_data("").decode("utf-8"))
    book_id = data["book_id"]
    user_name = data["user_name"]
    user_id = sql_query_user_id(user_name)
    result = sql_return_book(book_id,user_id)
    if not result[0]:
        return jsonify({"status":-1,"message":"fail"})
    return jsonify({"status":0,"message":"success"})


# @book.route("query_borrower",methods = ["post"])
# def query_borrower():
#     data = json.loads(request.get_data("").decode("utf-8"))
#     user_name = data["user_name"]
#     result = sql_query_borrower(user_name)
#     if not result[0]:
#         return jsonify({"status":-1,"message":result[1]})
#     return jsonify({"status":0,"message":"success","data":result[1]})
#
#
# @book.route("query_book",methods = ["post"])
# def query_book():
#     data = json.loads(request.get_data("").decode("utf-8"))
#     book_name = data["book_name"]
#     result = sql_query_book(book_name)
#     if not result[0]:
#         return jsonify({"status":-1,"message":result[1]})
#     return jsonify({"status":0,"message":"success","data":result[1]})





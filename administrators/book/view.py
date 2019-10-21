from flask import Blueprint,request,jsonify
from administrators.book import books
from administrators.book.db_book import sql_borrow_book,sql_return_book
import json

book = Blueprint("book",__name__)

@book.route("new_book_entry",methods = ["POST"])
def new_book_entry():
    data = json.loads(request.get_data("").decode("utf-8"))
    NBE = books.NewBookEntry(data)
    save_result = NBE.save_synopsis()  # 存储图书简介
    if not save_result:
        return jsonify({"status": -1, "message": "数据存储失败,请求终止"})
    update_result = NBE.data_access_to_database()  # 存储数据
    if not update_result[0]:
        return jsonify({"status": -1, "message" : update_result[1]})
    return jsonify({"status" : 0, "message" : "新书入库成功"})

@book.route("borrow_book",methods = ["post"])
def borrow_book():
    data = json.loads(request.get_data("").decode("utf-8"))
    book_id = data["book_id"]
    user_id = data["user_id"]
    result = sql_borrow_book(book_id,user_id)
    if not result[0]:
        return jsonify({"status":-1,"message":"请求出错"})
    return jsonify({"status":0,"message":"借书成功"})

@book.route("return_book",methods = ["post"])
def return_book():
    data = json.loads(request.get_data("").decode("utf-8"))
    book_id = data["book_id"]
    user_id = data["user_id"]
    borrow_time = data["borrow_time"]
    result = sql_return_book(book_id,user_id,borrow_time)
    if not result[0]:
        return jsonify({"status":-1,"message":"请求出错"})
    return jsonify({"status":0,"message":"还书成功"})







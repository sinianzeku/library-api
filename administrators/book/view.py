from flask import Blueprint,request,jsonify
from administrators.book import books
import json


book = Blueprint("book",__name__)

@book.route("new_book_entry",methods = ["POST"])
def new_book_entry():
    try:
        data = json.loads(request.get_data("").decode("utf-8"))
        QRC = books.NewBookEntry(data)
        save_result = QRC.save_synopsis()  # 存储图书简介
        if not save_result:
            return jsonify({"status": -1, "message": "数据存储失败,请求终止"})
        update_result = QRC.data_access_to_database()  # 存储数据
        if not update_result:
            return jsonify({"status": -1, "message": update_result[1]})
        return jsonify({"status": 0, "message": "新书入库成功"})
    except:
        return jsonify({"status": -1, "message": "服务器出错"})







from flask import Blueprint,request,jsonify
from models.book import books
import json


book = Blueprint("book",__name__)

@book.route("new_book_entry",methods = ["POST"])
def new_book_entry():
    try:
        data = json.loads(request.get_data("").decode("utf-8"))
        QRC = books.NewBookEntry(data)
        QR_result = QRC.generate_QR_code()  #生成二维码
        if not QR_result[0]:
            return jsonify({"status": -1, "message": "二维码生成失败,请求终止"})

        update_result = QRC.data_access_to_database()   #存储数据
        if not update_result[0]:
            return jsonify({"status": -1, "message": update_result[1]})
        return jsonify({"status": 0, "message": update_result[1]})
    except:
        return jsonify({"status": -1, "message": "服务器出错"})






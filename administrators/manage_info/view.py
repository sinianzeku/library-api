from flask import Blueprint,jsonify,request
from user.verify.userverify import UserVerify
from administrators.manage_info.db_manage import sql_add_manager
import json

admin = Blueprint("admin",__name__)

@admin.route("add_manager",methods = ["post"])
def add_manager():
    data = json.loads(request.get_data("").decode("utf-8"))
    work_id = data["work_id"]
    worker_name = data["worker_name"]
    work_passwords = data["work_password"]
    user = UserVerify()
    work_password = user.password(work_passwords)
    if not work_password[0]:
        return jsonify({"status":-1,"message":"密码格式错误"})
    result = sql_add_manager(work_id,worker_name,work_password[1])
    if not result[0]:
        return jsonify({"status":-1,"message":result[1]})
    return jsonify({"status":0,"message":result[1]})






@admin.route("test",methods = ['post'])
def test():
    return jsonify({"status":0,"manager":"admin success"})


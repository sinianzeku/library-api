from flask import Blueprint,jsonify,session,request
import json
from user.db.db_user import sql_update_infos,sql_reset_password,sql_feedbacks
from user.module.module import save_feedbacks

user = Blueprint("user_private",__name__)

@user.before_request
def before_user():
    if 'username' not in session:
        return jsonify({"status": -1, "message": "未登入"})




@user.route("feedback",methods = ["post"])
def feedback():
    try:
        data = json.loads(request.get_data("").decode("utf-8"))
        user_id = data["user_id"]
        feedbacks = data["feedbacks"]
        reader = data["reader"]
        phone = data["phone"]
        path = save_feedbacks(feedbacks,reader)
        result = sql_feedbacks(user_id,reader,phone,path)
        if not result:
            return jsonify({"status":-1,"message":"fail"})
        return jsonify({"status":0,"message":"success"})
    except:
        return jsonify({"status":-1,"message":"fail","data":"Server error"})


"""
更新信息
"""
@user.route("update_info",methods = ["post"])
def update_info():
    data = json.loads(request.get_data("").decode("utf-8"))
    user_name = data["user_name"]
    user_sex = data["user_sex"]
    user_phone_number = ["user_phone_number"]
    result = sql_update_infos()
    return jsonify({"status":0,"message":"success"})

"""
重置密码
"""
@user.route("reset_password",methods = ["post"])
def reset_password():
    data = json.loads(request.get_data("").decode("utf-8"))
    username = data["username"]
    password = data["password"]
    cpassword = data["cpassword"]
    result = sql_reset_password()
    return jsonify({"status":0,"message":"success"})



"""
退出登入
"""
@user.route("logout",methods = ["post"])
def logout():
    session.pop('username',None)
    return jsonify({"status": 0, "message": "退出成功"})

@user.route("test",methods = ["post"])
def test():
    return jsonify({"status": 0, "message": "success"})

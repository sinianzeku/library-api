from flask import Blueprint,jsonify,session


user = Blueprint("user_private",__name__)

@user.before_request
def before_user():
    if 'username' not in session:
        print(session)
        return jsonify({"status": -1, "message": "未登入"})


@user.route("text",methods = ["post"])
def text():
    return jsonify({"status": 0, "message": "响应成功"})


@user.route("logout", methods = ["post"])
def logout():
    session.pop('username')
    return jsonify({"status": 0, "message": "退出成功"})
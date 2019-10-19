from flask import Blueprint,jsonify

admin = Blueprint("admin",__name__)



@admin.route("test",methods = ['post'])
def test():
    return jsonify({"status":0,"manager":"admin success"})


from config.db_config import mysql_module


def sql_add_manager(work_id,worker_name,work_password):
    sql = "insert into admin (work_id,worker_name,work_password) values ('{}','{}','{}')".format(work_id,worker_name,work_password)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"管理员注册失败"]
    return [True,"管理员注册成功"]
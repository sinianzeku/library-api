from config.db_config import mysql_module
def into_register_info(username,password,email):
        select_user = "select count(user_account) as count from user where user_account = '{}'".format(username)
        result = mysql_module(select_user)
        if result[1][0]["count"]:
            return [False,"该用户已存在"]
        into_user = 'INSERT INTO user(user_account,user_password,user_email) VALUES("{}","{}","{}")'.format(username,password,email)
        result = mysql_module(into_user)
        if not result[0]:
            return [False,"注册失败"]
        return [True,"注册成功"]



def user_login(username,password):
    try:
        # if customer_type == "ordinaryusers":
        sql = 'select user_id from user where user_account = "{}" and user_password = "{}"'.format(username,password)
        # elif customer_type == "administrators":
        #     sql = 'select count(*) as count from user where work_id = "{}" and work_password = "{}"'.format(username, password)
        result = mysql_module(sql)
        if not result[1]:
            return [False, "账号或密码错误"]
        return [True,result[1][0]["user_id"]]
    except:
        return [False,"系统出错，登入失败"]


def sql_feedbacks(user_id,readers,phone,path):
    sql = "insert into feedback(user_id,readers,phone,feedbacks) value ('{}','{}','{}','{}')".format(user_id,readers,phone,path)
    result = mysql_module(sql)
    if not result[0]:
        return False
    return True


def sql_verify_old_password(user_account,verify_password):
    sql = "select user_account from user where user_account = '{}' and  user_password = '{}'".format(user_account,verify_password)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"查询出错"]
    if not result[1]:
        return [False,'旧密码错误']
    return [True]

def sql_update_password(user_account,new_password):
    sql = "update user set user_password = '{}' where user_account = '{}'".format(new_password,user_account)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"密码更改失败"]
    return [True]


def sql_borrowing_books(user_id):
    sql = ""


from config.db_config import mysql_module
from administrators.module.defaulttime import set_time
def into_register_info(username,password,email):
        st = set_time()
        select_user = "select user_id from user where user_account = '{}'".format(username)
        result = mysql_module(select_user)
        if result[1]:
            return [False,"该昵称已存在"]
        select_user = "select work_id from admin where work_id = '{}'".format(username)
        result = mysql_module(select_user)
        if result[1]:
            return [False,"该昵称已存在"]
        into_user = 'INSERT INTO user(user_account,user_password,user_email,user_registration_time) VALUES("{}","{}","{}","{}")'.format(username,password,email,st.today())
        result = mysql_module(into_user)
        if not result[0]:
            return [False,"注册失败"]
        return [True,"注册成功"]


def user_login(username,password,code):
    if code == 0:
        sql = 'select user_id from user where user_account = "{}" and user_password = "{}"'.format(username,password)
        result = mysql_module(sql)
        if not result[1]:
            return [False, "账号或密码错误"]
        return [True, result[1][0]["user_id"]]
    elif code == 1:
        sql = 'select work_id from admin where work_id = "{}" and work_password = "{}"'.format(username, password)
        result = mysql_module(sql)
        if not result[1]:
            return [False, "账号或密码错误"]
        return [True,result[1][0]["work_id"]]



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


def sql_update_info( user_id,email,phone,address):
    sql = "UPDATE USER SET user_email = '{}', user_phone = '{}',user_address = '{}' WHERE user_id = {}".format(email,phone,address,user_id)
    print(sql)
    # result = mysql_module(sql)
    # if not result[0]:
    #     return [False,"信息更新失败"]
    # return [True]




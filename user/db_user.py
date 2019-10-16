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
        sql = 'select count(*) as count from user where user_account = "{}" and user_password = "{}"'.format(username,password)
        result = mysql_module(sql)
        if not result[1][0]["count"]:
            return [False, "账号或密码错误"]
        return [True,"登入成功"]
    except:
        return [False,"系统出错，登入失败"]

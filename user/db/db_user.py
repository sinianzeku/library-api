from config.db_config import mysql_module
from config.defaulttime import set_time


def into_register_info(user_account, user_phone, username, password, email):
    st = set_time()
    select_user = "select user_id from user where user_account = '{}'".format(username)
    result = mysql_module(select_user)
    if result[1]:
        return [False, "该昵称已存在"]
    select_user = "select work_id from admin where work_id = '{}'".format(username)
    result = mysql_module(select_user)
    if result[1]:
        return [False, "该昵称已存在"]
    into_user = 'INSERT INTO user(user_account,user_password,user_name,user_email,user_phone,user_registration_time) VALUES("{}","{}","{}","{}","{}","{}")'.format(
        user_account, password, username, email, user_phone, st.today())
    result = mysql_module(into_user)
    if not result[0]:
        return [False, "注册失败"]
    return [True, "注册成功"]


def user_login(username, password, code):
    if code == '0':
        sql = 'select user_id from user where user_account = "{}" and user_password = "{}"'.format(username, password)
        result = mysql_module(sql)
        if not result[1]:
            return [False, "账号或密码错误"]
        return [True, result[1][0]["user_id"]]
    elif code == '1':
        sql = 'select work_id from admin where work_id = "{}" and work_password = "{}"'.format(username, password)
        result = mysql_module(sql)
        if not result[1]:
            return [False, "账号或密码错误"]
        return [True, result[1][0]["work_id"]]


def sql_feedbacks(user_id, readers, phone, feedbacks):
    st = set_time()
    sql = "insert into feedback(user_id,readers,phone,feedbacks,state,time) value ('{}','{}','{}','{}','1','{}')".format(
        user_id, readers, phone, feedbacks, st.today())
    result = mysql_module(sql)
    if not result[0]:
        return False
    return True


def sql_verify_old_password(user_account, verify_password):
    sql = "select user_account from user where user_account = '{}' and  user_password = '{}'".format(user_account,
                                                                                                     verify_password)
    result = mysql_module(sql)
    if not result[0]:
        return [False, "查询出错"]
    if not result[1]:
        return [False, '原密码错误']
    return [True]


def sql_update_password(user_account, new_password):
    sql = "update user set user_password = '{}' where user_account = '{}'".format(new_password, user_account)
    result = mysql_module(sql)
    if not result[0]:
        return [False, "密码更改失败"]
    return [True]


def sql_update_info(user_account, user_name, user_sex, email, phone):
    sql = "UPDATE user SET user_email = '{}', user_phone = '{}',user_name = '{}',user_sex = '{}' WHERE user_account = '{}'".format(
        email, phone, user_name, user_sex, user_account)
    result = mysql_module(sql)
    if not result[0]:
        return [False, "信息更新失败"]
    return [True]


def sql_query_user_info(user_id):
    sql = "select user_account,user_name,user_phone,user_email,user_sex from user where user_id = '{}'".format(user_id)
    result = mysql_module(sql)
    return result


def sql_get_feedback(user_id):
    st = set_time()
    sql = 'select feedbacks,cast(time as char) time,state from feedback where user_id = "{}" and time >="{}"'.format(
        user_id, st.time_frame(["past", 30]))
    result = mysql_module(sql)
    return result


def sql_change_photo(img, username):
    sql = "update user set user_photo = '{}' where user_account = '{}'".format(img, username)
    mysql_module(sql)
    return True


def sql_query_photo(username):
    sql1 = 'select user_photo from user where user_account = "{}"'.format(username)
    result1 = mysql_module(sql1)
    if result1[1]:
        return result1[1][0]["user_photo"]
    return None




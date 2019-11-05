from config.db_config import mysql_module


def sql_add_manager(work_id,worker_name,work_password):
    sql = "insert into admin (work_id,worker_name,work_password) values ('{}','{}','{}')".format(work_id,worker_name,work_password)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"管理员注册失败"]
    return [True,"管理员注册成功"]


def sql_query_user_info(user_name):
    if user_name:
        sql = "select user_id,user_account, user_email, cast(user_registration_time as char) as user_registration_time  from user where instr(user_account,'{}')".format(user_name)
    else:
        sql = "select user_id,user_account, user_email, cast(user_registration_time as char) as user_registration_time  from user"
    result = mysql_module(sql)
    if not result[0]:
        return [False,"用户信息查询失败"]
    return [True,result[1]]

def sql_query_book_info_0(book_name):
    sql = "select book_id,book_name from book_info where book_state = '0'"
    if book_name:
        sql = "select book_id,book_name from book_info where instr(book_name,'{}')  and book_state = '0'".format(book_name)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"用户信息查询失败"]
    return [True,result[1]]

def sql_query_book_info_1(book_name,user_id):
    sql = "select book_id,book_name from book_info where instr(book_name,'{}')  and book_state = '1' and book_id in ( select book_id from borrow_info where user_id = {})".format(book_name,user_id)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"用户信息查询失败"]
    return [True,result[1]]

def sql_add_book_category(category1,category2):
    sql = "select id from book_category where category1 = '{}' and category2 = '{}'".format(category1,category2)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"信息查询失败"]
    if result[1]:
        return [False,"该分类已存在"]
    sql = "insert into book_category(category1,category2) values ('{}','{}')".format(category1,category2)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"分类保存失败"]
    return [True,"分类保存成功"]


def sql_user_info():
    sql = "select user_account,user_name,user_phone,cast(user_registration_time as char) as user_registration_time  from user"
    result = mysql_module(sql)
    return result

def sql_conditional_user_info(user_name):
    sql = "select user_account,user_name,user_phone,cast(user_registration_time as char) as user_registration_time  from user where instr(user_account,'{}')".format(user_name)
    result = mysql_module(sql)
    return result

def sql_delete_user(user_name):
    sql_id = "select user_id from user where user_account = '{}'".format(user_name)
    user_id = mysql_module(sql_id)[1][0]["user_id"]
    sql_de_bookshelf = "delete from my_bookshelf where user_id = '{}'".format(user_id)
    sql_de_bookshelf = "delete from my_bookshelf where user_id = '{}'".format(user_id)







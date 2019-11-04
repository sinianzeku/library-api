from config.db_config import mysql_module


def sql_add_manager(work_id,worker_name,work_password):
    sql = "insert into admin (work_id,worker_name,work_password) values ('{}','{}','{}')".format(work_id,worker_name,work_password)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"管理员注册失败"]
    return [True,"管理员注册成功"]


def sql_query_user_info(user_name):
    sql = "select user_account, user_email, user_registration_time  from user where instr(user_account,'{}')".format(user_name)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"用户信息查询失败"]
    if not result[1]:
        return [False,"查无数据"]
    return [True,result[1]]

def sql_query_book_info(book_name):
    sql = "select book_id,book_name,book_auther from book_info where instr(book_name,'{}')".format(book_name)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"用户信息查询失败"]
    if not result[1]:
        return [False,"查无数据"]
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











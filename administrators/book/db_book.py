from config.db_config import mysql_module,mysql_modules
from config.defaulttime import set_time

def insertnewbook(**kwargs):
    list_key = list(kwargs.keys())
    list_value = list(kwargs.values())
    sql = "insert into book_info ({},{},{},{},{},{},{},{},{},{},{}) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
        list_key[0],list_key[1],list_key[2],list_key[3],list_key[4],list_key[5],list_key[6],list_key[7],list_key[8],list_key[9],list_key[10],
        list_value[0],list_value[1],list_value[2],list_value[3],list_value[4],list_value[5],list_value[6],list_value[7],list_value[8],list_value[9],list_value[10])
    into_result = mysql_module(sql)
    if not into_result[0]:
        return [False,"数据存储失败"]
    return [True]


def sql_borrow_book(book_name,user_name):

    time = set_time()

    sql = "insert into borrow_info (user_name,book_name,borrow_time,return_time,state) values ('{}','{}','{}','{}','{}')".format(user_name,book_name,time.today(),time.next_month(),1)
    sql2 = "UPDATE book_info set book_state = '1' where book_name = '{}'".format(book_name)
    result = mysql_modules(sql,sql2)
    return result


def sql_return_book(book_name,user_name):
    time = set_time()
    sql = "UPDATE borrow_info set state = '0',actual_return_time = '{}' where book_name = {} and book_name = {} ".format(time.today(),book_name,user_name)
    sql2 = "UPDATE book_info set book_state = '0' where user_name = '{}'".format(user_name)
    result = mysql_modules(sql,sql2)
    return result


def sql_query_book_category(category1,category2):
    sql = "select id from book_category where category1 = '{}' and category2 = '{}'".format(category1, category2)
    result = mysql_module(sql)
    if not result[1]:
        return [False,"无此分类"]
    return [True,result[1][0]["id"]]


def sql_verify_book_code(book_code):
    sql = "select book_id from book_info where book_code = '{}'".format(book_code)
    result =mysql_module(sql)
    if result[1]:
        return [False,"条码号已存在"]


def sql_query_borrower(user_account):
    sql = "select user_id,user_account,user_email,cast(user_registration_time as char) as user_registration_time from user where instr(user_account,'{}')".format(user_account)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"查询出错"]
    return [True,result[1]]

def sql_query_book(book_name):
    sql = "select book_id,book_name from book_info where instr(book_name,'{}')".format(book_name)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"查询出错"]
    return [True,result[1]]



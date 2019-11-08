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


def sql_borrow_book(user_id,book_id):
    time = set_time()
    sql = "insert into borrow_info (user_id,book_id,borrow_time,return_time,state) values ({},{},'{}','{}','{}')".format(user_id,book_id,time.today(),time.next_month(),1)
    sql2 = "UPDATE book_info set book_state = '1' where book_id = {}".format(book_id)
    print(sql)
    print(sql2)
    result = mysql_modules(sql,sql2)
    return result

def sql_query_user_id(user_name):
    sql = "select user_id from user where user_account = '{}'".format(user_name)
    result = mysql_module(sql)
    if not result[1]:
        return [False,'fail']
    return result[1][0]["user_id"]

def sql_Verify(book_id, user_id):
    sql = "select count(*) count from borrow_info where user_id = {} and book_id = {}".format(user_id,book_id)
    result = mysql_module(sql)
    if not result[1][0]["count"]:
        return False
    return True

def sql_return_book(book_id,user_id):
    time = set_time()
    sql = "UPDATE borrow_info set state = '0',actual_return_time = '{}' where book_id = {} and user_id = {} ".format(time.today(),book_id,user_id)
    sql2 = "UPDATE book_info set book_state = '0' where book_id = '{}'".format(book_id)
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

def sql_borrow_limit(user_id):
    sql = "select count(*) count from borrow_info where state = '1' and user_id = {}".format(user_id)
    result = mysql_module(sql)
    return result[1][0]["count"]



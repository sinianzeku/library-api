from config.db_config import mysql_module,mysql_modules
from administrators.module.defaulttime  import set_time

def insertnewbook(**kwargs):
    list_key = list(kwargs.keys())
    list_value = list(kwargs.values())
    sql = "insert into book_info ({},{},{},{},{},{},{},{},{}) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
        list_key[0],list_key[1],list_key[2],list_key[3],list_key[4],list_key[5],list_key[6],list_key[7],list_key[8],
        list_value[0],list_value[1],list_value[2],list_value[3],list_value[4],list_value[5],list_value[6],list_value[7],list_value[8])
    into_result = mysql_module(sql)
    if not into_result[0]:
        return [False,"数据存储失败"]
    return [True]



def sql_borrow_book(book_id,user_id):
    time = set_time()
    sql = "insert into borrow_info (user_id,book_id,borrow_time,return_time,state) values ('{}','{}','{}','{}','{}')".format(user_id,book_id,time.today(),time.next_month(),1)
    sql2 = "UPDATE book_info set book_state = '1' where book_id = {}".format(book_id)
    result = mysql_modules([sql,sql2])
    return result


def sql_return_book(book_id,user_id,borrow_time):
    time = set_time()
    sql = "UPDATE borrow_info set state = '0',actual_return_time = '{}' where book_id = {} and user_id = {} and borrow_time = '{}'".format(time.today(),book_id,user_id,borrow_time)
    sql2 = "UPDATE book_info set book_state = '0' where book_id = {}".format(book_id)
    result = mysql_modules([sql,sql2])
    return result









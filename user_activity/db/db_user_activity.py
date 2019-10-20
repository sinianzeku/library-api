from config.db_config import mysql_module
from user_activity.module import activity_set


def search_book(query_criteria,query_content):
    sql = "select book_id, book_name, book_auther, book_publisher from book_info where instr({},'{}')".format(query_criteria,query_content)
    result = mysql_module(sql)
    if not result[1]:
        return [False,"查无数据"]
    return result


def search_book_info(book_id):
    sql = "select * from book_info where book_id = '{}' ".format(book_id)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"查询出错"]
    if not result[1]:
        return [False,"查无数据"]
    final_result = activity_set.processing_data(result)
    return final_result

def sql_borrowed_records(user_id):
    sql = ''
    result = mysql_module(sql)
    if not result[0]:
        return [False,"查询出错"]
    if not result[1]:
        return [False,"查无数据"]
    return [True,result[1]]

def sql_borrowing_books(user_id):
    sql = ''
    result = mysql_module(sql)
    if not result[0]:
        return [False,"查询出错"]
    if not result[1]:
        return [False,"查无数据"]
    return [True,result[1]]

def sql_my_bookshelf(user_id):
    sql = ''
    result = mysql_module(sql)
    if not result[0]:
        return [False,"查询出错"]
    if not result[1]:
        return [False,"查无数据"]
    return [True,result[1]]




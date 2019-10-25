from config.db_config import mysql_module
from user_activity.module import activity_set


def sql_query_book(query_criteria,query_content):
    sql = "select book_id, book_name, book_auther, book_publisher from book_info where instr({},'{}')".format(query_criteria,query_content)
    result = mysql_module(sql)
    if not result[1]:
        return [False,"查无数据"]
    return result


def sql_query_book_info(book_id):
    sql = "select book_id,book_name,book_auther,book_category,book_publisher,book_room,book_bookshelf,book_synopsis_path,book_state,book_publication_date,cast(books_add_time as char) as books_add_time from book_info where book_id = '{}' ".format(book_id)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"查询出错"]
    if not result[1]:
        return [False,"查无数据"]
    final_result = activity_set.processing_data(result)
    return final_result

#历史借书记录
def sql_borrowed_records(user_id):
    sql = 'SELECT	book.book_id,	book_name,	book_auther,	cast(borrow_time as char) as borrow_time,	cast(actual_return_time as char) as actual_return_time,	book_room FROM	( SELECT book_id, book_name, book_auther, book_room FROM book_info WHERE book_id IN ( SELECT book_id FROM borrow_info WHERE user_id = {} ) ) AS book LEFT JOIN borrow_info borrow ON borrow.book_id = book.book_id'.format(user_id)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"查询出错"]
    if not result[1]:
        return [False,"查无数据"]
    return [True,result[1]]

#在借书籍
def sql_borrowing_books(user_id):
    sql = "select book.book_id,book_name,cast(borrow_time as char) borrow_time,cast(return_time as char) return_time,book_room from  (select book_id,book_name,book_room from book_info where book_id in (select book_id from borrow_info where user_id = {} and state = 1)) book LEFT JOIN (select borrow_time,return_time,book_id from borrow_info where user_id = {} and state = 1) borrow on book.book_id = borrow.book_id ".format(user_id,user_id)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"查询出错"]
    if not result[1]:
        return [False,"查无数据"]
    return result

#书架
def sql_my_bookshelf(user_id):
    sql = 'SELECT book_id,	book_name,	book_auther, book_room FROM book_info WHERE	book_id IN ( SELECT book_id FROM my_bookshelf WHERE user_id = {} )'.format(user_id)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"查询出错"]
    if not result[1]:
        return [False,"查无数据"]
    return [True,result[1]]

def sql_collect_book(user_id,book_id):
    sql = "insert into my_bookshelf values('{}','{}')".format(user_id,book_id)
    result = mysql_module(sql)
    return [True,"收藏成功"]

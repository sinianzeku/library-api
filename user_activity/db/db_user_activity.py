from config.db_config import mysql_module
from user_activity.module import activity_set


def sql_query_book(query_criteria,query_content):
    sql = "select book_id, book_name, book_auther, book_language, book_publisher from book_info where instr({},'{}')".format(query_criteria,query_content)
    result = mysql_module(sql)
    return result


def sql_query_book_info(book_id):
    sql = "select book_id,book_name,book_auther,book_category,book_publisher,book_room,book_bookshelf,book_synopsis,book_state,book_publication_date,cast(books_add_time as char) as books_add_time from book_info where book_id = '{}' ".format(book_id)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"查询出错"]
    return result

#历史借书记录
def sql_borrowed_records(user_id):
    sql = 'SELECT	book.book_id,	book_name,	book_auther,	cast(borrow_time as char) as borrow_time,	cast(actual_return_time as char) as actual_return_time,	book_room FROM	( SELECT book_id, book_name, book_auther, book_room FROM book_info WHERE book_id IN ( SELECT book_id FROM borrow_info WHERE user_id = {} ) ) AS book LEFT JOIN borrow_info borrow ON borrow.book_id = book.book_id'.format(user_id)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"查询出错"]
    return [True,result[1]]

#在借书籍
def sql_borrowing_books(user_id):
    sql = "select book.book_id,book_name,cast(borrow_time as char) borrow_time,cast(return_time as char) return_time,book_room from  (select book_id,book_name,book_room from book_info where book_id in (select book_id from borrow_info where user_id = {} and state = 1)) book LEFT JOIN (select borrow_time,return_time,book_id from borrow_info where user_id = {} and state = 1) borrow on book.book_id = borrow.book_id ".format(user_id,user_id)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"查询出错"]
    return result

#书架
def sql_my_bookshelf(user_id):
    sql = 'SELECT book_id,	book_name,	book_auther, book_room FROM book_info WHERE	book_id IN ( SELECT book_id FROM my_bookshelf WHERE user_id = {} )'.format(user_id)
    result = mysql_module(sql)
    if not result[0]:
        return [False,"查询出错"]
    return [True,result[1]]

def sql_collect_book(user_id,book_id):
    sql = "insert into my_bookshelf values('{}','{}')".format(user_id,book_id)
    mysql_module(sql)
    return [True,"收藏成功"]

def sql_popular_recommendation(today_time,past_time,language,category1):
    sql1 = "where 1 = 1"
    if today_time:
        sql1 = sql1 + " and books_add_time<='{}'".format(today_time)
    if past_time:
        sql1 = sql1 + " and books_add_time >='{}' ".format(past_time)
    if language:
        sql1 = sql1 + " and book_language = '{}'".format(language)
    if category1:
        sql1 = sql1 + " and book_category in (select id from book_category where category1 = '{}' )".format(category1)

    sql2 = "select distinct book.book_id,book.book_name,book_auther, count(book.book_id) as count from borrow_info borrow left join book_info book on borrow.book_id = book.book_id {} group by book_id order by count desc ".format(sql1)
    result = mysql_module(sql2)
    return [True,result[1]]


def sql_new_arrivals(today_time,past_time,language,category1):
    sql1 = "where 1 = 1"
    if today_time:
        sql1 = sql1 + " and books_add_time<='{}'".format(today_time)
    if past_time:
        sql1 = sql1 + " and books_add_time >='{}' ".format(past_time)
    if language:
        sql1 = sql1 + " and book_language = '{}'".format(language)
    if category1:
        sql1 = sql1 + " and book_category in (select id from book_category where category1 = '{}' )".format(category1)

    sql2 = 'select book_id,book_name,book_auther from book_info  {}  order by books_add_time '.format(sql1)
    result = mysql_module(sql2)
    return [True,result[1]]


def sql_class_lookup(category1,category2,language):
    sql1 = " where 1 = 1 "
    if category1:
        sql1 = sql1 + " and category1 = '{}'".format(category1)
    if category2:
        sql1 = sql1 + " and category2 = '{}'".format(category2)
    sql2 = "select * from book_info where book_category in (select id from book_category {}) and book_language = '{}'".format(sql1,language)
    result = mysql_module(sql2)
    if not result[0]:
        return [False,"查询失败"]
    if not result[1]:
        return [False,"查无数据"]
    return [True,result[1]]


def sql_category1():
    sql = "select distinct category1 from book_category"
    result = mysql_module(sql)
    return result


def sql_category2(category1):
    sql = "select category2 from book_category where category1 = '{}'".format(category1)
    result = mysql_module(sql)
    return result


def sql_thematic_activities(contestant,phone,works):
    sql = "insert into thematic_activities values('{}','{}','{}')".format(contestant,phone,works)
    result = mysql_module(sql)
    return result


def sql_email(user_id):
    sql = "select user_email from user where user_id = '{}'".format(user_id)
    result = mysql_module(sql)
    return result[1][0]["user_email"]

def sql_add_key_works(txt,query_mode):
    sql = "select words from key_word where words = '{}'".format(txt)
    result = mysql_module(sql)
    if result[1]:
        sql2 = "update key_word set count=count+1 where words = '{}'".format(txt)
    else:
        sql2 = "insert into key_word value ('{}','{}',1)".format(txt,query_mode)
    mysql_module(sql2)
    return True
from config.db_config import mysql_module


def sql_query_book(query_criteria, query_content):
    sql = "select book_id, book_name, book_auther, book_language, book_publisher from book_info where instr({},'{}')".format(
        query_criteria, query_content)
    result = mysql_module(sql)
    return result


def sql_query_book_info(book_id):
    sql = "select book_id,book_name,book_auther,book_category,book_publisher,book_room,book_bookshelf,book_synopsis,book_state,cast(book_publication_date as char) as book_publication_date ,cast(books_add_time as char) as books_add_time, book_language,book_img_path from book_info where book_id = '{}' ".format(
        book_id)
    result = mysql_module(sql)
    if not result[0]:
        return [False, "查询出错"]
    return result


def sql_count_book(user_id):
    sql = "SELECT * from ( select count(*) count  from my_bookshelf where user_id = {} UNION ALL select count(*) count  from borrow_info where user_id = {} and state = '1' UNION ALL select count(*) count  from borrow_info where user_id = {} UNION ALL select user_photo from user where user_id = '{}') as counts".format(
        user_id, user_id, user_id, user_id)
    result = mysql_module(sql)
    return result[1][0]["count"], result[1][1]["count"], result[1][2]["count"], result[1][3]["count"]


# 历史借书记录
def sql_borrowed_records(user_id):
    sql = 'SELECT book.book_id,book_name,book_auther,book.book_publisher,	cast(borrow_time as char) as borrow_time,cast(actual_return_time as char) as actual_return_time,book_room FROM ( SELECT book_id,book_publisher, book_name, book_auther, book_room FROM book_info WHERE book_id IN ( SELECT book_id FROM borrow_info WHERE user_id = {} ) ) AS book LEFT JOIN borrow_info borrow ON borrow.book_id = book.book_id and borrow.user_id = 21'.format(
        user_id)
    result = mysql_module(sql)
    if not result[0]:
        return [False, "查询出错"]
    return [True, result[1]]


# 在借书籍
def sql_borrowing_books(user_id):
    sql = "select book.book_id,book_name,book.book_publisher,cast(borrow_time as char) borrow_time,cast(return_time as char) return_time,book_room from  (select book_id,book_name,book_publisher,book_room from book_info where book_id in (select book_id from borrow_info where user_id = {} and state = 1)) book LEFT JOIN (select borrow_time,return_time,book_id from borrow_info where user_id = {} and state = 1) borrow on book.book_id = borrow.book_id ".format(
        user_id, user_id)
    result = mysql_module(sql)
    if not result[0]:
        return [False, "查询出错"]
    return result


# 书架
def sql_my_bookshelf(user_id):
    sql = 'SELECT book_id,	book_name,book_publisher,book_auther, book_room FROM book_info WHERE	book_id IN ( SELECT book_id FROM my_bookshelf WHERE user_id = {} )'.format(
        user_id)
    result = mysql_module(sql)
    if not result[0]:
        return [False, "查询出错"]
    return [True, result[1]]


def sql_collect_book(user_name, book_id):
    sql_user_id = "select user_id from user where user_account = '{}'".format(user_name)
    user_id = mysql_module(sql_user_id)[1][0]['user_id']

    sql_select = "select id from my_bookshelf where user_id = {} and book_id = {}".format(user_id, book_id)
    if mysql_module(sql_select)[1]:
        return [False, "该书已在您的书架中"]
    sql = "insert into my_bookshelf(user_id,book_id) values('{}','{}')".format(user_id, book_id)
    mysql_module(sql)
    return [True, "收藏成功"]

def cancel_collect_book(user_name, book_id):
    sql_user_id = "select user_id from user where user_account = '{}'".format(user_name)
    user_id = mysql_module(sql_user_id)[1][0]['user_id']
    sql = "DELETE from my_bookshelf where user_id = {} and book_id = '{}'".format(user_id,book_id)
    mysql_module(sql)
    return [True, "删除成功"]

def sql_popular_recommendation(today_time, past_time, language, category1, category2):
    sql1 = "where 1 = 1"
    sql_cate = "select id from book_category where 1 = 1"
    if today_time:
        sql1 = sql1 + " and books_add_time<='{}'".format(today_time)
    if past_time:
        sql1 = sql1 + " and books_add_time >='{}' ".format(past_time)
    if language:
        sql1 = sql1 + " and book_language = '{}'".format(language)
    if category1:
        sql_cate = sql_cate + " and category1 = '{}'".format(category1)
    if category2:
        sql_cate = sql_cate + " and category2 = '{}'".format(category2)

    sql2 = "select distinct book.book_id,book.book_name,book_auther, count(book.book_id) as count, book.book_img_path from borrow_info borrow left join book_info book on borrow.book_id = book.book_id {} and book.book_category in ({}) group by book_id order by count desc limit 50".format(
        sql1, sql_cate)
    result = mysql_module(sql2)
    return [True, result[1]]


def sql_aut_popular_recommendation():
    sql = "select distinct book.book_id,book.book_name,book_auther, book.book_img_path, count(book.book_id) as count from borrow_info borrow left join book_info book on borrow.book_id = book.book_id  group by book_id order by count desc limit 50"
    result = mysql_module(sql)
    return [True, result[1]]


def sql_index_popular_recommendation():
    sql = "select distinct book.book_id,book.book_name, count(book.book_id) as count from borrow_info borrow left join book_info book on borrow.book_id = book.book_id  group by book_id order by count desc limit 7"
    result = mysql_module(sql)
    return [True, result[1]]


def sql_new_arrivals(today_time, past_time, language, category1, category2):
    sql1 = "where 1 = 1"
    sql_cate = "select id from book_category where 1 = 1"
    if today_time:
        sql1 = sql1 + " and books_add_time<='{}'".format(today_time)
    if past_time:
        sql1 = sql1 + " and books_add_time >='{}' ".format(past_time)
    if language:
        sql1 = sql1 + " and book_language = '{}'".format(language)
    if category1:
        sql_cate = sql_cate + " and category1 = '{}'".format(category1)
    if category2:
        sql_cate = sql_cate + " and category2 = '{}'".format(category2)

    sql2 = 'select book_id,book_name,book_auther, book_img_path from book_info {} and book_category in ({}) order by books_add_time desc limit 50 '.format(
        sql1, sql_cate)
    result = mysql_module(sql2)
    return [True, result[1]]


def sql_aut_new_arrivals():
    sql = "select book_id,book_name,book_auther, book_img_path from book_info order by books_add_time desc limit 50"
    result = mysql_module(sql)
    return [True, result[1]]


def sql_index_new_arrivals():
    sql = "select book_id,book_name,cast(books_add_time as char)books_add_time from book_info order by books_add_time desc limit 7"
    result = mysql_module(sql)
    return [True, result[1]]


def sql_class_lookup(category1, category2, language):
    sql1 = "select id from book_category where 1 = 1 "
    if category1:
        sql1 = sql1 + " and category1 = '{}'".format(category1)
    if category2:
        sql1 = sql1 + " and category2 = '{}'".format(category2)
    sql2 = "select book_id,book_name,book_auther,book_img_path from book_info where book_category in ({}) ".format(sql1)
    if language:
        sql2 = sql2 + " and book_language = '{}'".format(language)
    result = mysql_module(sql2)
    return result


def sql_aut_class_lookup():
    sql = "select book_id,book_name,book_auther,book_img_path from book_info "
    result = mysql_module(sql)
    return result


def sql_category1():
    sql = "select distinct category1 from book_category"
    result = mysql_module(sql)
    return result


def sql_category2(category1):
    sql = "select category2 from book_category where category1 = '{}'".format(category1)
    result = mysql_module(sql)
    return result


def sql_thematic_activities(contestant, phone, works, user_name):
    sql_user_id = "select user_id from user where user_account = '{}'".format(user_name)
    user_id = mysql_module(sql_user_id)[1][0]['user_id']
    sql_select = "select id from thematic_activities where user_id = {}".format(user_id)
    if mysql_module(sql_select)[1]:
        return [False, "您已报名过该活动"]
    sql = "insert into thematic_activities(contestant,phone,works,user_id) values('{}','{}','{}',{})".format(contestant,
                                                                                                             phone,
                                                                                                             works,
                                                                                                             user_id)
    result = mysql_module(sql)
    return result


def sql_voluntary_activities(contestant, user_name, phone, email, days, times):
    sql_user_id = "select user_id from user where user_account = '{}'".format(user_name)
    user_id = mysql_module(sql_user_id)[1][0]['user_id']
    sql_select = "select id from voluntary_activities where user_id = {}".format(user_id)
    if mysql_module(sql_select)[1]:
        return [False, "您已报名过该活动"]
    sql = "insert into voluntary_activities(contestant,phone,email,days,times,user_id) values('{}','{}','{}','{}','{}',{})".format(
        contestant, phone, email, days, times, user_id)
    result = mysql_module(sql)
    return result


def sql_book_name_query(book_name):
    sql = "select book_id,book_name,book_auther,book_category,book_publisher,book_room,book_bookshelf,book_synopsis,book_state,cast(book_publication_date as char) as book_publication_date ,cast(books_add_time as char) as books_add_time, book_language from book_info where book_name = '{}' ".format(
        book_name)
    result = mysql_module(sql)
    return result


def sql_query_category(category):
    sql = 'select category1,category2 from book_category where id = {}'.format(category)
    result = mysql_module(sql)
    return result[1][0]["category1"] + "/" + result[1][0]["category2"]


def sql_email(user_name):
    sql = "select user_email from user where user_account = '{}' ".format(user_name)
    result = mysql_module(sql)
    if not result[1]:
        return [False, "用户名不存"]
    return [True, result[1][0]["user_email"]]


def sql_update_password(user_account, new_password):
    sql = "update user set user_password = '{}' where user_account = '{}'".format(new_password, user_account)
    result = mysql_module(sql)
    if not result[0]:
        return [False, "密码更改失败"]
    return [True]

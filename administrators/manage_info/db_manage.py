from config.db_config import mysql_module,mysql_modules
from config.defaulttime import set_time

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
    sql = "select user_account,user_name,user_email,user_phone,cast(user_registration_time as char) as user_registration_time  from user"
    result = mysql_module(sql)
    return result

def sql_conditional_user_info(user_name):
    sql = "select user_account,user_name,user_email,user_phone,cast(user_registration_time as char) as user_registration_time  from user where instr(user_account,'{}')".format(user_name)
    result = mysql_module(sql)
    return result

def sql_delete_user(user_name):
    sql_id = "select user_id from user where user_account = '{}'".format(user_name)
    user_id = mysql_module(sql_id)[1][0]["user_id"]
    sql_de_bookshelf = "delete from my_bookshelf where user_id = '{}'".format(user_id)
    sql_de_feedback = "delete from feedback where user_id = '{}'".format(user_id)
    sql_de_borrow = "delete from borrow_info where user_id = '{}'".format(user_id)
    sql_de_user = "delete from user where user_id = '{}'".format(user_id)
    result = mysql_modules(sql_de_bookshelf,sql_de_feedback,sql_de_borrow,sql_de_user)
    return result


def sql_book_info():
    sql = "select book_id,book_code,book_name,book_auther,category1,category2,book_publisher,book_room,book_bookshelf,book_synopsis,cast(book_publication_date as char) book_publication_date,book_language,book_state from book_info inner JOIN book_category on id = book_category"
    result = mysql_module(sql)
    return result


def sql_conditional_book_info(book_id,book_name,book_publisher,book_room,book_state):
    sql = "1 = 1"
    if book_id:
        sql = sql + " and book_id = {}".format(book_id)
    if book_name:
        sql = sql + " and instr(book_name,'{}')".format(book_name)
    if book_publisher:
        sql = sql + " and instr(book_publisher,'{}')".format(book_publisher)
    if book_room:
        sql = sql + " and instr(book_room,'{}')".format(book_room)
    if book_state:
        sql = sql + " and  book_state = '{}'".format(book_state)
    sql = "select book_id,book_code,book_name,book_publisher,book_room,book_state from book_info where {}".format(sql)
    result = mysql_module(sql)
    return result

def sql_borrowing_book():
    sql = "select book.book_id, book.book_code, book.book_name,book.book_publisher,cast(borrow.borrow_time as char) borrow_time,cast(borrow.return_time as char) return_time,user.user_account from borrow_info borrow inner join book_info book on borrow.book_id = book.book_id inner join user on borrow.user_id = user.user_id where borrow.state = '1'"
    result = mysql_module(sql)
    return result

def sql_conditional_borrowing_book(book_id,book_name,book_publisher,borrow_time_satrt,borrow_time_end,user_name):
    sql = "select book.book_id, book.book_code, book.book_name,book.book_publisher,cast(borrow.borrow_time as char) borrow_time,cast(borrow.return_time as char) return_time,user.user_account from borrow_info borrow inner join book_info book on borrow.book_id = book.book_id inner join user on borrow.user_id = user.user_id where borrow.state = '1'"
    if book_id:
        sql = sql + " and instr(borrow.book_id,'{}')".format(book_id)
    if book_name:
        sql = sql + " and instr(book_name,'{}')".format(book_name)
    if book_publisher:
        sql = sql + " and instr(book_publisher,'{}')".format(book_publisher)
    if borrow_time_satrt:
        sql = sql + " and borrow_time >= '{}'".format(borrow_time_satrt)
    if borrow_time_end:
        sql = sql + " and borrow_time <= '{}'".format(borrow_time_end)
    if user_name:
        sql = sql + " and instr(user_account,'{}')".format(user_name)

    result = mysql_module(sql)
    return result

def sql_delete_book(book_id):
    sql_de_borrow = "delete from borrow_info where book_id = '{}'".format(book_id)
    sql_de_bookshelf = "delete from my_bookshelf where book_id = '{}'".format(book_id)
    sql_de_book = "delete from book_info where book_id = '{}'".format(book_id)
    result = mysql_modules(sql_de_borrow,sql_de_bookshelf,sql_de_book)
    return result


def sql_change_book_info(**kwargs):
    list_key = list(kwargs.keys())
    list_value = list(kwargs.values())
    sql = "UPDATE book_info SET {} = '{}',{} = '{}',{} = '{}',{} = {},{} = '{}',{} = '{}',{} = '{}',{} = '{}',{} = '{}',{} = '{}' where {} = '{}'".format(list_key[0],list_value[0],
                 list_key[1],list_value[1],
                list_key[2],list_value[2],
                 list_key[3],list_value[3],
                list_key[4],list_value[4],
                list_key[5],list_value[5],
                list_key[6],list_value[6],
                list_key[7],list_value[7],
                list_key[8],list_value[8],
                list_key[9],list_value[9],
                list_key[10],list_value[10])
    return mysql_module(sql)


def sql_borrow_record():
    sql = "select borrow_id,book.book_id, book.book_code, book.book_name,book.book_publisher,cast(borrow.borrow_time as char) borrow_time,cast(actual_return_time as char) actual_return_time,user.user_account from borrow_info borrow inner join book_info book on borrow.book_id = book.book_id inner join user on borrow.user_id = user.user_id where borrow.state = '0'"
    result = mysql_module(sql)
    return result


def sql_conditional_borrow_record(book_id, book_name, book_publisher, borrow_time_satrt,borrow_time_end, user_name):
    sql = "select borrow_id,book.book_id, book.book_code, book.book_name,book.book_publisher,cast(borrow.borrow_time as char) borrow_time,cast(actual_return_time as char) actual_return_time,user.user_account from borrow_info borrow inner join book_info book on borrow.book_id = book.book_id inner join user on borrow.user_id = user.user_id where borrow.state = '0'"
    if book_id:
        sql = sql + " and instr(borrow.book_id,'{}')".format(book_id)
    if book_name:
        sql = sql + " and instr(book_name,'{}')".format(book_name)
    if book_publisher:
        sql = sql + " and instr(book_publisher,'{}')".format(book_publisher)
    if borrow_time_satrt:
        sql = sql + " and borrow_time >= '{}'".format(borrow_time_satrt)
    if borrow_time_end:
        sql = sql + " and borrow_time <= '{}'".format(borrow_time_end)
    if user_name:
        sql = sql + " and instr(user_account,'{}')".format(user_name)

    result = mysql_module(sql)
    return result


def sql_delete_borrow_record(borrow_id):
    sql_de_borrow = "delete from borrow_info where borrow_id = {}".format(borrow_id)
    result = mysql_module(sql_de_borrow)
    return result

def sql_user_number():
    sql = "select count(user_id) user_number  from user"
    result = mysql_module(sql)
    return result

def sql_book_number():
    sql = "select count(book_id) book_number  from book_info"
    result = mysql_module(sql)
    return result

def sql_borrowing_number():
    sql = "select count(borrow_id) borrowing_number  from borrow_info where state = '1'"
    result = mysql_module(sql)
    return result

def sql_borrow_record_number():
    sql = "select count(borrow_id) borrow_number  from  borrow_info where state = '0'"
    result = mysql_module(sql)
    return result

def sql_borrowing_condition():
    st = set_time()
    time_dict = st.first_half_year()
    key = list(time_dict.keys())
    times = list(time_dict.values())
    result_list = {}
    number = []
    month = []
    for i in range(len(time_dict)):
        sql = 'select count(borrow_id) borrow_number from borrow_info where instr(borrow_time,"{}")'.format(times[i])
        result = mysql_module(sql)
        number.append(result[1][0]['borrow_number'])
        month.append(str(key[i])+"月")
    result_list["number"] = number
    result_list["month"] = month
    return result_list

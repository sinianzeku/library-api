from config.db_config import mysql_module

def insertnewbook(keys,values):
    try:
        sql = "insert into book_info ({}) values ({})".format(keys, '"' + values + '"')
        into_result = mysql_module(sql)
        if not into_result[0]:
            return [False,"数据存储失败"]
        sql1 = 'SELECT book_id from book_info where book_id = (SELECT max(book_id) FROM book_info)'
        select_result = mysql_module(sql1)
        if not select_result[0]:
            return [False]
        return [True,select_result[1]]
    except:
        return [False,"数据库出错"]








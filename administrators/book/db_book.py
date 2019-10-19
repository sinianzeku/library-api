from config.db_config import mysql_module

def insertnewbook(keys,values):
    try:
        sql = "insert into book_info ({}) values ({})".format(keys, '"' + values + '"')
        into_result = mysql_module(sql)
        if not into_result[0]:
            return [False,"数据存储失败"]
        return [True]
    except:
        return [False,"数据库出错"]










from config.db_config import mysql_module

def insertnewbook(**kwargs):
    try:
        list_key = list(kwargs.keys())
        list_value = list(kwargs.values())
        sql = "insert into book_info ({},{},{},{},{},{},{},{},{}) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
            list_key[0],list_key[1],list_key[2],list_key[3],list_key[4],list_key[5],list_key[6],list_key[7],list_key[8],
            list_value[0],list_value[1],list_value[2],list_value[3],list_value[4],list_value[5],list_value[6],list_value[7],list_value[8])
        print(sql)
        into_result = mysql_module(sql)
        if not into_result[0]:
            return [False,"数据存储失败"]
        return [True]
    except:
        return [False,"数据库出错"]










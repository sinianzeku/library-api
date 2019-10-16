from config.db_config import mysql_module

def search_book(query_criteria,query_content):
    sql = "select * from book_info where instr({},'{}')".format(query_criteria,query_content)
    result = mysql_module(sql)
    if not result[1]:
        return [False,"查无数据"]
    return [True,result]



from config.db_config import mysql_module
from . import activity_set

def search_book(query_criteria,query_content):
    sql = "select book_id, book_name, book_auther, book_publisher from book_info where instr({},'{}')".format(query_criteria,query_content)
    result = mysql_module(sql)
    if not result[1]:
        return [False,"查无数据"]
    return result


def search_book_info(book_id):
    sql = "select * from book_info where book_id = '{}' ".format(book_id)
    result = mysql_module(sql)
    if not result[1]:
        return [False,"查无数据"]
    final_result = activity_set.processing_data(result)
    return final_result


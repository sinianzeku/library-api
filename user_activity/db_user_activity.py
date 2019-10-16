from config.db_config import mysql_module

def search_book(query_criteria,query_content):
    sql = "select * from book_info where instr({},'{}')".format(query_criteria,query_content)
    result = mysql_module(sql)
    if not result[1]:
        return [False,"查无数据"]
    return result


def search_book_info(book_name,book_auther,book_publisher,book_category_name):
    sql = "select * from book_info where book_name ='{}' and book_auther = '{}' and book_publisher = '{}' and book_category_name = '{}'".format(book_name,book_auther,book_publisher,book_category_name)

    result = mysql_module(sql)

    if not result[1]:
        return [False,"查无数据"]
    return result


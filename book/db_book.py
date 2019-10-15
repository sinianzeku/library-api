import pymysql

def insertnewbook(keys,values):
    # try:
        db = pymysql.connect("127.0.0.1", "root", "123456", "library")
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "insert into book_info ({}) values ({})".format(keys,'"'+values+'"')
        print(sql)
        cursor.execute(sql)
        cursor.fetchall()
        db.commit()

        sql1 = 'SELECT book_id from book_info where book_id = (SELECT max(book_id) FROM book_info)'
        cursor.execute(sql1)
        result = cursor.fetchall()
        print(result[0]["book_id"])
        return [result[0]["book_id"]]
    # except:
    #     return [False, "图书入管失败"]
    # finally:
    #     db.close()







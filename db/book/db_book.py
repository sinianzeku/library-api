import pymysql

def insertnewbook(keys,values):
    try:
        db = pymysql.connect("127.0.0.1", "root", "123456", "library")
        sql = "insert into book_info ({}) values ({})".format(keys,'"'+values+'"')
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        cursor.fetchall()
        db.commit()
        return [True,"图书入管成功"]
    except:
        return [False, "图书入管失败"]
    finally:
        db.close()







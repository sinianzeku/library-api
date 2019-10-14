import pymysql

def insertnewbook(auther,bookname,QR_path):
    try:
        db = pymysql.connect("47.96.139.19", "root", "123456", "library")
        sql = 'insert into book (bookname,auther,QR_path)  VALUES ("{}","{}","{}")'.format(bookname,auther,QR_path)
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        cursor.fetchall()
        db.commit()
        return [True,"图书入管成功"]
    except:
        return [False, "图书入管失败"]
    finally:
        db.close()







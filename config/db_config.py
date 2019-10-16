import pymysql

host = "127.0.0.1"
user = "root"
password = "123456"
database = "library"


def mysql_module(sql):
    try:
        db = pymysql.connect(host,user,password,database)
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        result = cursor.fetchall()
        db.commit()
        return [True,result]
    except:
        return [False]
    finally:
        db.close()


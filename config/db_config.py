import pymysql

# host = "47.96.139.19"
host = "127.0.0.1"
user = "root"
password = "123456"
database = "library"


def mysql_module(sql):
    db = pymysql.connect(host,user,password,database)
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    db.commit()
    return [True,result]


def mysql_modules(*arg):
    result = []
    db = pymysql.connect(host, user, password, database)
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    for sql in arg:
        cursor.execute(sql)
        result.append(cursor.fetchall())
    db.commit()
    return [True,result]


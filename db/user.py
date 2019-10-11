import pymysql
def into_register_info(username,password):
    db = pymysql.connect("127.0.0.1", "root", "123456", "library")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        sql = "select count(user_account) as count from user where user_account = '{}'".format(username)
        cursor.execute(sql)
        result = cursor.fetchall()
        if result[0]["count"]:
            return [False,"该用户已存在"]
        else:
            sql = 'INSERT INTO user(user_account,user_password) VALUES("{}","{}")'.format(username,password)
            cursor.execute(sql)
            cursor.fetchall()
            db.commit()
            return [True,"注册成功"]
    except:
        return [False,"注册出错"]
    finally:
        db.close()

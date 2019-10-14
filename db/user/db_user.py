import pymysql
def into_register_info(username,password,email):
    db = pymysql.connect("47.96.139.19", "root", "123456", "library")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        sql = "select count(user_account) as count from user where user_account = '{}'".format(username)
        cursor.execute(sql)
        result = cursor.fetchall()
        if result[0]["count"]:
            return [False,"该用户已存在"]
        else:
            sql = 'INSERT INTO user(user_account,user_password,user_email) VALUES("{}","{}","{}")'.format(username,password,email)
            cursor.execute(sql)
            cursor.fetchall()
            db.commit()
            return [True,"注册成功"]
    except:
        return [False,"注册出错"]
    finally:
        db.close()


def user_login(username,password):
    db = pymysql.connect("47.96.139.19", "root", "123456", "library")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        sql = 'select count(*) as count from user where user_account = "{}" and user_password = "{}"'.format(username,password)
        cursor.execute(sql)
        result = cursor.fetchall()
        if result[0]["count"]:
            return [True,"登入成功"]
        else:
            return [False,"账号或密码错误"]
    except:
        return [False,"系统出错，登入失败"]
    finally:
        db.close()

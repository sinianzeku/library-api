import hashlib
import re

class UserVerify():

    def password(self,password):
        if not re.search(u'^[_a-zA-Z0-9]+$', password) :
            err = "密码含有非法字符"
            password = [False,err]
            return password
        if not (len(password)>=6 and len(password)<=16):
            err = "密码长度必须在6—16之间"
            password = [False, err]
            return password
        password = password_encryption(password)
        return [True,password]


    def username(self,username):
        if not re.search(u'^[_a-zA-Z\u4e00-\u9fa5]+$', username) :
            err = "用户名含有非法字符"
            self.username = [False,err]
            return
        if not (len(username)>=4 and len(username)<=12):
            err = "用户名长度应为4—12个字符"
            self.username = [False, err]
            return
        self.username = [True, username]
        return self.username


def password_encryption(password):
    pwd_hash = hashlib.md5()
    pwd_hash.update(password.encode("utf8"))
    password = pwd_hash.hexdigest()
    return password


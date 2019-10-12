import hashlib
import re

class UserRegister():
    def __init__(self,username,password):
        self.username = username
        self.password = password

    @property
    def password(self):
        if self._password[0]:
            pwd_hash = hashlib.md5()
            pwd_hash.update(self._password[1].encode("utf8"))
            password = pwd_hash.hexdigest()
            return [self._password[0],password]
        else:
            return [self._password[0],self._password[1]]

    @password.setter
    def password(self,password):
        if not re.search(u'^[_a-zA-Z0-9]+$', password) :
            err = "密码含有非法字符"
            self._password = [False,err]
            return
        if not (len(password)>=6 and len(password)<=16):
            err = "密码长度必须在8—16之间"
            self._password = [False, err]
            return
        else:
            self._password = [True,password]
            return

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self,username):
        if not re.search(u'^[_a-zA-Z\u4e00-\u9fa5]+$', username) :
            err = "用户名含有非法字符"
            self._username = [False,err]
            return
        if not (len(username)>=2 and len(username)<=16):
            err = "用户名长度应为4—16个字符"
            self._username = [False, err]
            return
        else:
            self._username = [True, username]
            return



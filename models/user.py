class User():
    def __init__(self,username,password):
        self.username = username
        self.password = password

    @property  #将一个getter方法变成属性
    def password(self):
        #密码的合法性验证
        return self.password

    @property
    def UserName(self):
        #用户名的合法性验证
        return self.username
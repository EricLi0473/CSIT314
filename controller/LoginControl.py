from entity.User import User
class LoginControl:
    def __init__(self):
        pass
    def checkLogin(self,username,password):
        return User().checkLogin(username,password)

'''
参数：用户名，密码
正常成功创建：返回Ture
未成功创建：返回False
可能返回False的情况：
用户名不存在，密码错误，账户被冻结
'''
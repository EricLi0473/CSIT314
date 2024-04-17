from entity.User import User
class CreateUserControl:
    def __init__(self):
        pass
    def createUser(self,username,password,email,userType):
        usernameList = User().findAllUserName()
        if username in usernameList:
            return False
        else:
            return User().addUser(username,password,email,userType)

'''
参数：用户名，密码，邮箱，用户类型
正常成功创建：返回Ture
未成功创建：返回False
可能返回False的情况：
用户名重复，用户类型异常
'''
from entity.User import User
class UpdataUserControl:
    def __init__(self):
        pass

    def updateUser(self,oldUsername,newUsername,password,email,userType,states):
        try:
            usernameList = User().findAllUserName()
            usernameList.remove(oldUsername)
        except Exception:
            return False
        if newUsername in usernameList:
            return False
        else:
            return User().updataUser(oldUsername,newUsername,password,email,userType,states)

'''
参数：旧用户名，新用户名，密码，邮箱，用户类型，用户状态
更新成功创建：返回Ture
未更新冻结：返回False
可能返回False的情况：
旧用户名不存在，新用户名重复
'''


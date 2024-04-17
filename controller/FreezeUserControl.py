from entity.User import User
class FreezeUserControl:
    def __init__(self):
        pass

    def freezeUser(self,username):
        try:
            user = User().searchUser(username)
            return User().updataUser(user.getUsername(), user.getUsername(),user.getPassword(),
                              user.getEmail(), user.getUserType(),'invalid')
        except Exception:
            return False

'''
参数：用户名
冻结成功创建：返回Ture
未成功冻结：返回False
可能返回False的情况：
用户不存在
'''
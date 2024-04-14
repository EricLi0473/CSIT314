from entity.User import User
class UserControl:

    def __init__(self,user = User()):
        self.user = user

    def getUser(self):
        return self.user

    def setUser(self,user):
        self.user = user
    '''
        All user login.
        Parameter: username:string, password:string
        return loginUser:User(if not find, return None)
    '''
    def checkLogin(self,username,password):
        user = self.getUser().searchUser(username)
        userControl = UserControl(user)
        userType = user.getUserType()
        if password == user.getPassword():
            return userControl,userType
        else:
            raise Exception('Password error')

    def findUsernameByUserId(self,userId):
        return self.getUser().findUsernameByUserId(userId)

    def findUserIdByUserName(self,userName):
        return self.getUser().findUserIdByUserName(userName)
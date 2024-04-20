from entity.User import User
class LoginController:
    def __init__(self):
        pass

    def checkLogin(self,username,password):
        return User.checkLogin(username,password)

    def findUserType(self,username):
        return User().findAUser(username).getUserTypeId()


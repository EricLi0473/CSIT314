from entity.User import User
class LoginController:
    def __init__(self):
        pass

    def checkLogin(self,username,passwrod):
        return User.checkLogin(username,passwrod)

    def findUserType(self,username):
        return User().findAUser(username).getUserTypeId()


from entity.User import User
class LoginController:
    def __init__(self):
        pass

    def checkLogin(self,username,password):
        return User().checkLogin(username,password)

    def findUser(self,username)-> User:
        return User().findAUser(username)

print(LoginController().checkLogin('Alice', 'password4977'))
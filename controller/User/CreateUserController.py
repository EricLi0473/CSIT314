from entity.User import User
from entity.Profile import Profile
class CreateUserController:
    def __init__(self):
        pass
    def createUser(self,username,password,email,userType):
        userTypeId = Profile().findProfileIdByName(userType)
        return User().addUser(username,password,email,userTypeId)



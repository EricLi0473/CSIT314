from entity.User import User
from entity.Profile import Profile
class UpdateUserController:
    def __init__(self):
        pass

    def updateUser(self,oldUsername,newUsername,password,email,userType):
        userTypeId = Profile().findAProfile(userType).profileId
        return User().updateUser(oldUsername,newUsername,password,email,userTypeId)

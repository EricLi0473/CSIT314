from entity.User import User
from entity.Profile import Profile
class UpdateUserController:
    def __init__(self):
        pass

    def updateUser(self,oldUsername,newUsername,password,email,userType):
        print(oldUsername,newUsername,password,email,userType)
        userTypeId = Profile().findProfileIdByName(userType)
        print(userTypeId)
        return User().updateUser(oldUsername,newUsername,password,email,userTypeId)

# u1 = UpdateUserController()
# print(u1.updateUser("buyer1","buyer1","buyer123","buyer1@example.com","buyer"))
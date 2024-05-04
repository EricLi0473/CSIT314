from entity.User import User
from entity.Profile import Profile
class ViewUserController:
    def __init__(self):
        pass

    def viewAllUser(self):
        return User().findAllUser()


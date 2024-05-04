from entity.User import User
from entity.Profile import Profile
class SearchUserController:
    def __init__(self):
        pass
    def seachAUser(self,username):
        user = User().findAUser(username)
        return user



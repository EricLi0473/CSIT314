from entity.User import User
class FreezeUserController:
    def __init__(self):
        pass

    def freezeUser(self,username):
        return User().suspendUser(username)


from entity.User import User
class ActivateUserController:
    def __init__(self):
        pass

    def activateUser(self,username):
        return User().activateUser(username)

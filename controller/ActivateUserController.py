from entity.User import User
class ActivateUserController:
    def __init__(self):
        pass

    def activateUser(self,username):
        user = User().searchUser(username)
        return User().updataUser(user.getUsername(),user.getUsername(),user.getPassword(),
                                 user.getEmail(),user.getUserType(),'valid')

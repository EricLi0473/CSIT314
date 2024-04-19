from entity.User import User
class ActivateUserControl:
    def __init__(self):
        pass

    def activateUser(self,username):
        try:
            user = User().searchUser(username)
            return User().updataUser(user.getUsername(),user.getUsername(),user.getPassword(),
                                     user.getEmail(),user.getUserType(),'valid')

        except Exception:
            return False
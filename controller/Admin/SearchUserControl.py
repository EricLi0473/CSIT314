from entity.User import User
class SearchUserControl:
    def __init__(self):
        pass
    def seachAUser(self,username):
        user = User().searchUser(username)
        userText = [[]]
        userText[0].append(user.getUsername())
        userText[0].append(user.getPassword())
        userText[0].append(user.getEmail())
        userText[0].append(user.getUserType())
        userText[0].append(user.getUserStatus())
        return userText
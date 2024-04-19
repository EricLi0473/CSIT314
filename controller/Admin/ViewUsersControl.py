from entity.User import User
class ViewUserControl:
    def __init__(self):
        pass

    def viewAllUser(self):
        userTextList = []
        userList = User().findAllUser()
        for user in userList:
            userText = []
            userText.append(user.getUsername())
            userText.append(user.getPassword())
            userText.append(user.getEmail())
            userText.append(user.getUserType())
            userText.append(user.getUserStatus())
            userTextList.append(userText)
        return userTextList

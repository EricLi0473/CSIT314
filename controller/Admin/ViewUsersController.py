from entity.User import User
from entity.Profile import Profile
class ViewUserController:
    def __init__(self):
        pass

    def viewAllUser(self):
        return User().findAllUser()

    def TransferUserToList(self,userList):
        userTextList = []
        for user in userList:
            userText = []
            userText.append(user.getUsername())
            userText.append(user.getPassword())
            userText.append(user.getEmail())
            userText.append(Profile().findProfileNameById(user.getUserTypeId()))
            userText.append(user.getUserStatus())
            userTextList.append(userText)
        return userTextList

v1 = ViewUserController().viewAllUser()
print(ViewUserController().TransferUserToList(v1))
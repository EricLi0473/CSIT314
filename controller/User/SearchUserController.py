from entity.User import User
from entity.Profile import Profile
class SearchUserController:
    def __init__(self):
        pass
    def seachAUser(self,username):
        user = User().findAUser(username)
        return user

    # def TransferUserToList(self, user):
    #     userText = []
    #     userText.append(user.getUsername())
    #     userText.append(user.getPassword())
    #     userText.append(user.getEmail())
    #     userText.append(Profile().findProfileNameById(user.getUserTypeId()))
    #     userText.append(user.getUserStatus())
    #     return userText


"""返回object，再转换成list"""

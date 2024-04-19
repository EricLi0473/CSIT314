from entity.Property import Property
from entity.User import User
class SavePropertyControl:
    def __init__(self):
        pass
    def saveProperty(self,userName,title):
        userId = User().findUserIdByUserName(userName)
        propertyId = Property().findPropertyIdByName(title)
        pass

# s1 = SavePropertyControl()
# print(s1.saveProperty("buyer1",'Property1'))

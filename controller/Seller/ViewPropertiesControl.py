from entity.Property import Property
from entity.User import User

class ViewPropertiesControl:
    def __init__(self):
        pass

    def viewProperties(self,username):
        userId = User().findAUser(username).userid
        propertiesList = Property().findPropertyBySellerId(userId)
        return propertiesList
'''''
return PropertyList by SellerName
'''''

from entity.Property import Property
from entity.User import User

class ViewPropertiesControl:
    def __init__(self):
        pass

    def viewProperties(self,userId):
        propertiesList = Property().findPropertyBySellerId(userId)
        return propertiesList
'''''
return PropertyList by SellerName
'''''

from entity.Property import Property
from entity.User import User
from entity.NewFavorites import NewFavorites
from entity.OldFavorits import OldFavorites

class AddPropertyIntoFavoritesControl:
    def __init__(self):
        pass

    def addpropertyIntoFavorites(self,username,title):
        try:
            property = Property().findAProperty(title)
            userId = User().findUserIdByUserName(username)
            propertyId = Property().findPropertyIdByTitle(title)
            Property().favoritesCountPlasOne(title)
            if property.status == "available":
                return NewFavorites().addIntoNewFavorities(userId,propertyId)
            else:
                return OldFavorites().addIntoOldFavorities(userId,propertyId)
        except Exception:
            return False



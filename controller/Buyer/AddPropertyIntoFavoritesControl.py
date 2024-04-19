from entity.Property import Property
from entity.User import User
from entity.Favorites import Favorites

class AddPropertyIntoFavoritesControl:
    def __init__(self):
        pass

    def addpropertyIntoFavorites(self,username,title):
        try:
            userId = User().findUserIdByUserName(username)
            propertyId = Property().findPropertyIdByName(title)
            return Favorites().addIntoFavorities(userId,propertyId)
        except Exception:
            return False


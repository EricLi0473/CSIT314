from entity.Property import Property
from entity.User import User
from entity.Favorites import Favorites
class SavePropertyController:
    def __init__(self):
        pass
    def saveProperty(self,userName,title):
        try:
            userId = User().findUserIdByUserName(userName)
            propertyId = Property().findPropertyIdByTitle(title)
            Property().favoritesCountPlasOne(title)
            return Favorites().addIntoFavorities(userId, propertyId)
        except Exception:
            return False

from entity.Property import Property
from entity.User import User
from entity.NewFavorites import NewFavorites
from entity.OldFavorits import OldFavorites

class AddNewPropertyIntoFavoritesControl:
    def __init__(self):
        pass

    def addNewPropertyIntoFavorites(self,userId,propertyId):
        try:
            return NewFavorites().addIntoNewFavorities(userId,propertyId)
        except Exception:
            return False



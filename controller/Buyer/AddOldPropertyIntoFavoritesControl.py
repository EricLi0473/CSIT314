from entity.Property import Property
from entity.User import User
from entity.NewFavorites import NewFavorites
from entity.OldFavorits import OldFavorites

class AddOldPropertyIntoFavoritesControl:
    def __init__(self):
        pass

    def addOldPropertyIntoFavorites(self,userId,propertyId):
        try:
            return OldFavorites().addIntoOldFavorities(userId,propertyId)
        except Exception:
            return False



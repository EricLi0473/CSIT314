from entity.Property import Property
from entity.User import User
from entity.OldFavorits import OldFavorites
class ViewOldFavouritesControl:
    def __init__(self):
        pass

    def viewOldFavorites(self, userId):
        return OldFavorites().FindOldFavouritesByBuyer(userId)

    '''''
    获取用户名下的Old Favourtes List 返回值 list[OldFavorites:object]
    [<entity.OldFavorits.OldFavorites object at 0x0000021FF5238550>, <entity.OldFavorits.OldFavorites object at 0x0000021FF5238610>,
    '''''


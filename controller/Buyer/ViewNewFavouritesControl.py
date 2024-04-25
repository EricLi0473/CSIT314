from entity.Property import Property
from entity.User import User
from entity.NewFavorites import NewFavorites
from entity.OldFavorits import OldFavorites
class ViewNewFavouritesControl:
    def __init__(self):
        pass

    def viewNewFavorites(self, username):
        userId = User().findUserIdByUserName(username)
        return NewFavorites().FindNewFavouritesByBuyer(userId)

    '''''
    获取用户名下的New Favourtes List 返回值 list[NewFavorites:object]
    [<entity.NewFavorites.NewFavorites object at 0x0000019DE4C088E0>, <entity.NewFavorites.NewFavorites object at 0x0000019DE4C08850>]
    '''''

    def transFerNewFavoritesToList(self, newFavorites):
        NewFavoritesList = []

        for newFavorite in newFavorites:
            PropertyTitle = Property().findPropertyTitledById(newFavorite.getPropertyId())
            NewFavoritesList.append(PropertyTitle)
        return NewFavoritesList
    '''''
    将 list[NewFavorites:object] 转换为 list[PropertyTitle:String]
    ['Property6', 'Property7', 'Property10']
    '''''

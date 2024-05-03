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

    # def transFerNewFavoritesToList(self, newFavorites):
    #     NewFavoritesList = []
    #     for newFavorite in newFavorites:
    #         propertyList = []
    #         propertyTitle = Property().findPropertyTitledById(newFavorite.getPropertyId())
    #         property = Property().findAProperty(propertyTitle)
    #         propertyList.append(property.getTitle())
    #         propertyList.append(property.getDescription())
    #         propertyList.append(property.getBedNum())
    #         propertyList.append(property.getBathNum())
    #         propertyList.append(property.getSize())
    #         propertyList.append(property.getPrice())
    #         propertyList.append(property.getStatus())
    #         propertyList.append(property.getViews())
    #         propertyList.append(property.getShortListed())
    #         agentID = property.getAgentId()
    #         agentName = User().findUsernameByUserId(agentID)
    #         propertyList.append(agentName)
    #         NewFavoritesList.append(propertyList)
    #     return NewFavoritesList
    '''''
    将 list[NewFavorites:object] 转换为 list[PropertyTitle:String]
    ['Property6', 'Property7', 'Property10']
    '''''

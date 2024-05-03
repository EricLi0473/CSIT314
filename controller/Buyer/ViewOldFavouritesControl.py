from entity.Property import Property
from entity.User import User
from entity.OldFavorits import OldFavorites
class ViewOldFavouritesControl:
    def __init__(self):
        pass

    def viewOldFavorites(self, username):
        userId = User().findUserIdByUserName(username)
        return OldFavorites().FindOldFavouritesByBuyer(userId)

    '''''
    获取用户名下的Old Favourtes List 返回值 list[OldFavorites:object]
    [<entity.OldFavorits.OldFavorites object at 0x0000021FF5238550>, <entity.OldFavorits.OldFavorites object at 0x0000021FF5238610>,
    '''''

    # def transFerOldFavoritesToList(self, oldFavorites):
    #     OldFavoritesList = []
    #     for oldFavorite in oldFavorites:
    #         propertyList = []
    #         propertyTitle = Property().findPropertyTitledById(oldFavorite.getPropertyId())
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
    #         OldFavoritesList.append(propertyList)
    #     return OldFavoritesList
    '''''
    将 list[OldFavorites:object] 转换为 list[PropertyTitle:String]
    ['Property1', 'Property2', 'Property1']
    '''''
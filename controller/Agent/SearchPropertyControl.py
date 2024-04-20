from entity.User import User
from entity.Property import Property


class SearchPropertyControl:
    def __init__(self):
        pass

    def searchProperty(self, title):
        property = Property().findAProperty(title)
        return property

    '''
    中介按照title搜索房产
    搜索成功返回Property:object，不成功返回 空的 Property:object,
    '''
    def transferPropertyToList(self, property):
        propertyTextList = []
        propertyTextList.append(property.getTitle())
        propertyTextList.append(property.getDescription())
        propertyTextList.append(property.getBathNum())
        propertyTextList.append(property.getBathNum())
        propertyTextList.append(property.getSize())
        propertyTextList.append(property.getPrice())
        propertyTextList.append(property.getStatus())
        propertyTextList.append(property.getViews())
        propertyTextList.append(property.getShortListed())
        try:
            sellerId = property.getSellerId()
            sellerName = User().findUsernameByUserId(sellerId)
            propertyTextList.append(sellerName)
        except Exception:
            propertyTextList.append(None)
        return propertyTextList

    '''
    Property:object -> propertyList:list
    返回PropertyList:
    ['Property1', 'Beautiful house with a garden', 2, 2, 2000, 300000.0, 'available', 0, 0, 'seller1']
    如果PropertyList为空返回
    [None,None....]
    '''

S1 = SearchPropertyControl()
print(S1.transferPropertyToList(S1.searchProperty("P")))
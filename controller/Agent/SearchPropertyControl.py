from entity.User import User
from entity.Property import Property
class SearchPropertyControl:
    def __init__(self):
        pass
    def searchProperty(self,title):
        propertyTextList = []
        if Property().searchProperty(title) is False:
            return False
        property = Property().searchProperty(title)
        propertyTextList.append(property.getTitle())
        propertyTextList.append(property.getDescription())
        propertyTextList.append(property.getBathNum())
        propertyTextList.append(property.getBathNum())
        propertyTextList.append(property.getSize())
        propertyTextList.append(property.getPrice())
        propertyTextList.append(property.getStatus())
        propertyTextList.append(property.getViews())
        propertyTextList.append(property.getShortListed())
        sellerId = property.getSellerId()
        sellerName = User().findUsernameByUserId(sellerId)
        propertyTextList.append(sellerName)
        return propertyTextList

'''
中介按照title搜索房产
搜索成功返回List，不成功返回False,
['Property1', 'Beautiful house with a garden', 2, 2, 2000, 300000.0, 'available', 0, 0, 'seller1']
'''


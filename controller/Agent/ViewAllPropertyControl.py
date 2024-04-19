from entity.User import User
from entity.Property import Property
class ViewAllPropertyControl:
    def __init__(self):
        pass
    def viewAllProperty(self,agentName):
        agentId = User().findUserIdByUserName(agentName)
        propertyTextList = []
        propertyList = Property().findPropertyByAgentId(agentId)
        for property in propertyList:
            propertyText = []
            propertyText.append(property.getTitle())
            propertyText.append(property.getDescription())
            propertyText.append(property.getBathNum())
            propertyText.append(property.getBathNum())
            propertyText.append(property.getSize())
            propertyText.append(property.getPrice())
            propertyText.append(property.getStatus())
            propertyText.append(property.getViews())
            propertyText.append(property.getShortListed())
            sellerId = property.getSellerId()
            sellerName = User().findUsernameByUserId(sellerId)
            propertyText.append(sellerName)
            propertyTextList.append(propertyText)
        return propertyTextList

'''
中介查看名下所有房产
返回二维列表，没有报错信息
'''

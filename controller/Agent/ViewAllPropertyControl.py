from entity.User import User
from entity.Property import Property
class ViewAllPropertyControl:
    def __init__(self):
        pass
    def viewAllProperty(self,agentName):
        agentId = User().findUserIdByUserName(agentName)
        return Property().findPropertyByAgentId(agentId)

    '''
    查看中介名下所有房产,返回list[Property:object]
    [<entity.Property.Property object at 0x0000021151D759A0>, <entity.Property.Property object at 0x0000021151D75970>,]
    '''
    def transferPropertiesToList(self,propertyList):
        propertyTextList = []
        for property in propertyList:
            propertyText = []
            propertyText.append(property.getTitle())
            propertyText.append(property.getDescription())
            propertyText.append(property.getBedNum())
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
    解析list[Property:object]-> list[list[property:string]]
    [['P1', '1', 1, 1, 1, 1.0, 'available', 0, 0, 'seller1'], ['Property3', 'Spacious villa with a pool', 4, 4, 5000, 600000.0, 'available', 0, 0, 'seller1']]
    '''

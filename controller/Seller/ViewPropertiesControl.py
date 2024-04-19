from entity.Property import Property
from entity.User import User

class ViewPropertiesControl:
    def __init__(self):
        pass

    def viewProperties(self,username):
        sellerId = User().findUserIdByUserName(username)
        propertyTextList = []
        propertiesList = Property().findPropertyBySellerId(sellerId)
        for property in propertiesList:
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
            agentId = property.getAgentId()
            agentName = User().findUsernameByUserId(agentId)
            propertyText.append(agentName)
            propertyTextList.append(propertyText)
        return propertyTextList

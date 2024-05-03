from entity.Property import Property
from entity.User import User

class ViewPropertiesController:
    def __init__(self):
        pass

    def viewProperties(self):
        return Property().viewAllProperty()

    # def transferPropertyToList(self,properyList):
    #     propertyTextList = []
    #     for property in properyList:
    #         propertyText = []
    #         propertyText.append(property.getTitle())
    #         propertyText.append(property.getDescription())
    #         propertyText.append(property.getBedNum())
    #         propertyText.append(property.getBathNum())
    #         propertyText.append(property.getSize())
    #         propertyText.append(property.getPrice())
    #         propertyText.append(property.getStatus())
    #         propertyText.append(property.getViews())
    #         propertyText.append(property.getShortListed())
    #         agentId = property.getAgentId()
    #         agentName = User().findUsernameByUserId(agentId)
    #         propertyText.append(agentName)
    #         propertyTextList.append(propertyText)
    #     return propertyTextList

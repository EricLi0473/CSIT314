from entity.Property import Property
from entity.User import User

class ViewPropertiesControl:
    def __init__(self):
        pass

    def viewProperties(self):
        propertyTextList = []
        propertiesList = Property().viewAllProperty()
        for property in propertiesList:
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
            agentId = property.getAgentId()
            agentName = User().findUsernameByUserId(agentId)
            propertyText.append(agentName)
            propertyTextList.append(propertyText)
        return propertyTextList
'''
用法：返回所有房产信息
返回值：二维列表
例子：[['Property1', 'Beautiful house with a garden', 2, 2, 2000, 300000.0, 'available', 0, 0, 'agent1'], 
['Property2', 'Cozy apartment in the city center', 1, 1, 1000, 150000.0, 'available', 0, 0, 'agent2']]
'''

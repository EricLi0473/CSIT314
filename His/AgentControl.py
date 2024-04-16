from control.UserControl import UserControl
from entity.Agent import Agent
from entity.Property import Property

class AgentControl(UserControl):

    def __init__(self,agent = Agent(),property = Property()):
        super().__init__(agent)
        self.property = property

    def getProperty(self):
        return self.property

    def setProperty(self,property):
        self.property = property

    def createProperty(self,title,description,bedNum,bathNum,size,price,
                       Sellername):
        agent = self.getUser().getUserID()
        sellerID = self.findUserIdByUserName(Sellername)
        self.getProperty().addProperty(title=title,description=description,bedNum=bedNum,
                                       bathNum=bathNum,size=size,price=price,agentid=agent,sellerid=sellerID)


    def updatePropertry(self,newTitle,oldTitle,description,bedNum,bathNum,size,price,status,sellerName):
        property = self.getProperty().searchProperty(oldTitle)
        if property.getAgentId() != self.getUser().getUserID():
            raise Exception('not found property')
        sellerID = self.findUserIdByUserName(sellerName)
        self.getProperty().updateProperty(newTitle=newTitle, oldTitle=oldTitle, description=description, bedNum=bedNum, bathNum=bathNum, size=size, price=price, status=status,sellerId=sellerID)


    def removeProperty(self,title):
        property = self.getProperty().searchProperty(title)
        if property.getAgentId() != self.getUser().getUserID():
            raise Exception('not found property')
        self.getProperty().removeProperty(title)

    def searchProperty(self,title):
        propertyTextList = []
        property = self.getProperty().searchProperty(title)
        if property.getAgentId() != self.getUser().getUserID():
            raise Exception('not found property')
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
        sellerName = self.findUsernameByUserId(sellerId)
        propertyText.append(sellerName)
        propertyTextList.append(propertyText)
        return propertyTextList

    def viewReviewsAndRating(self):
        pass
    def viewAllProperty(self):
        agentId = self.getUser().getUserID()
        propertyTextList = []
        propertyList = self.getProperty().findPropertyByAgentId(agentId)
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
            sellerName = self.findUsernameByUserId(sellerId)
            propertyText.append(sellerName)
            propertyTextList.append(propertyText)
        return propertyTextList



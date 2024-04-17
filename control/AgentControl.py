from control.UserControl import UserControl
from entity.Agent import Agent
from entity.Property import Property
from entity.Review import Review
class AgentControl(UserControl):

    def __init__(self,agent = Agent(),property = Property(),review = Review()):
        super().__init__(agent)
        self.property = property
        self.review = review

    def getReview(self):
        return self.review

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
        sellerID = self.findUserIdByUserName(sellerName)
        self.getProperty().updateProperty(newTitle=newTitle, oldTitle=oldTitle, description=description, bedNum=bedNum, bathNum=bathNum, size=size, price=price, status=status,sellerId=sellerID)


    def removeProperty(self,title):
        self.getProperty().removeProperty(title)

    def searchProperty(self,title):
        propertyTextList = []
        property = self.getProperty().searchProperty(title)
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

    def viewReviews(self):
        agentId = self.getUser().getUserID()
        reviewsTextList = []
        reviewsList = self.getReview().findReviewByAgentId(agentId)
        for review in reviewsList:
            senderId = review.getSenderId()
            senderName = self.findUsernameByUserId(senderId)
            reviewsTextList.append(senderName)
            reviewsTextList.append(review.getRating())
            reviewsTextList.append(review.getComment())
        return reviewsList
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

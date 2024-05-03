from entity.User import User
from entity.Rating import Rating
class ViewRatingControl:
    def __init__(self):
        pass
    def viewRating(self,agentName):
        agentId = User().findAUser(agentName).userid
        return Rating().findRatingByAgentId(agentId)
    '''
    查看中介名下所有！！！评分:int！！！,返回list[Reviews:object]
    [<entity.Review.Review object at 0x0000026355B3AD60>, <entity.Review.Review object at 0x0000026355B3ADC0>, <entity.Review.Review object at 0x0000026355B5D340>]
    '''

    # def transferRatingToList(self,reviewsList):
    #     reviewsTextList = []
    #     for review in reviewsList:
    #         reviewsText = []
    #         senderId = review.getSenderId()
    #         senderName = User().findUsernameByUserId(senderId)
    #         reviewsText.append(senderName)
    #         reviewsText.append(review.getRating())
    #         reviewsTextList.append(reviewsText)
    #     return reviewsTextList

    '''
    解析list[Reviews:object]-> list[list[reviews:string]]
    [['buyer1', 5], ['buyer3', 5], ['seller1', 5]]
    '''



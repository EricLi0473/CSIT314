from entity.User import User
from entity.Review import Review
class ViewReviewsAndRatingControl:
    def __init__(self):
        pass
    def viewReviewsAndRating(self,agentName):
        agentId = User().findUserIdByUserName(agentName)
        return Review().findReviewByAgentId(agentId)
    '''
    查看中介名下所有评分,返回list[Reviews:object]
    [<entity.Review.Review object at 0x0000026355B3AD60>, <entity.Review.Review object at 0x0000026355B3ADC0>, <entity.Review.Review object at 0x0000026355B5D340>]
    '''
    def transferReviewsAndRatingToList(self,reviewsList):
        reviewsTextList = []
        for review in reviewsList:
            reviewsText = []
            senderId = review.getSenderId()
            senderName = User().findUsernameByUserId(senderId)
            reviewsText.append(senderName)
            reviewsText.append(review.getRating())
            reviewsText.append(review.getComment())
            reviewsTextList.append(reviewsText)
        return reviewsTextList

    '''
    解析list[Reviews:object]-> list[list[reviews:string]]
    [['buyer1', 5, 'Excellent service from the agent'], ['buyer3', 5, 'Very helpful throughout the process'], ['seller1', 5, 'Agent did a great job selling my property']]
    '''

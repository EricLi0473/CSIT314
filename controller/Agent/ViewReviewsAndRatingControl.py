from entity.User import User
from entity.Review import Review
class ViewReviewsAndRatingControl:
    def __init__(self):
        pass
    def viewReviewsAndRatingControl(self,agentName):
        agentId = User().findUserIdByUserName(agentName)
        reviewsTextList = []
        reviewsList = Review().findReviewByAgentId(agentId)
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
中介查看自己名下的reviews和rating
返回二维列表，没有报错
[['buyer1', 5, 'Excellent service from the agent'], ['buyer3', 5, 'Very helpful throughout the process'], ['seller1', 5, 'Agent did a great job selling my property']]
'''

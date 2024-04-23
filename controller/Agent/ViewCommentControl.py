from entity.User import User
from entity.Comment import Comment
class ViewCommentControl:
    def __init__(self):
        pass
    def viewComment(self,agentName):
        agentId = User().findUserIdByUserName(agentName)
        return Comment().findCommentByAgentId(agentId)
    '''
    查看中介名下所有！！！评论:string！！！,返回list[Reviews:object]
    [<entity.Review.Review object at 0x0000026355B3AD60>, <entity.Review.Review object at 0x0000026355B3ADC0>, <entity.Review.Review object at 0x0000026355B5D340>]
    '''

    def transferCommentToList(self,reviewsList):
        reviewsTextList = []
        for review in reviewsList:
            reviewsText = []
            senderId = review.getSenderId()
            senderName = User().findUsernameByUserId(senderId)
            reviewsText.append(senderName)
            reviewsText.append(review.getComment())
            reviewsTextList.append(reviewsText)
        return reviewsTextList

    '''
    解析list[Reviews:object]-> list[list[reviews:string]]
    [['buyer1', 'Excellent service from the agent'], ['buyer3', 'Very helpful throughout the process'], ['seller1', 'Agent did a great job selling my property']]
    '''
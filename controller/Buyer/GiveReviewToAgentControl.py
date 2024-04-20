from entity.User import User
from entity.Review import Review

class GiveReviewToAgentControl:
    def __init__(self):
        pass

    def giveReviewToAgent(self,senderName,agentName,rating,comment):
        senderId = User().findUserIdByUserName(senderName)
        agentId = User().findUserIdByUserName(agentName)
        return Review().addReview(senderId,agentId,rating,comment)


